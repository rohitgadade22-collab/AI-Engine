from loguru import logger

from app.registration.registration_state import RegistrationState


class RegistrationPipeline:

    def __init__(
        self,
        registration_manager,
        stable_face_service,
        countdown_service,
        best_frame_collector,
    ):

        self._registration_manager = registration_manager
        self._stable_face_service = stable_face_service
        self._countdown_service = countdown_service
        self._best_frame_collector = best_frame_collector

    def process(
        self,
        face_result,
        session,
    ):

        # -------------------------------------------------
        # No active session
        # -------------------------------------------------

        if session is None:
            return None

        # -------------------------------------------------
        # Face not detected
        # -------------------------------------------------

        if not face_result.detected:

            session.state = RegistrationState.NO_FACE

            self._stable_face_service.reset()
            self._countdown_service.reset()

            logger.debug("Registration : No Face")

            return session

        # -------------------------------------------------
        # Registration quality check
        # -------------------------------------------------

        if face_result.registration_score < 80:

            session.state = RegistrationState.ALIGN_FACE

            self._stable_face_service.reset()
            self._countdown_service.reset()

            logger.debug(
                f"Registration : Align Face ({face_result.registration_score:.2f})"
            )

            return session

        # -------------------------------------------------
        # Face stability
        # -------------------------------------------------

        stable = self._stable_face_service.update(face_result)

        if not stable:

            session.state = RegistrationState.HOLD_STILL

            self._countdown_service.reset()

            logger.debug("Registration : Hold Still")

            return session

        # -------------------------------------------------
        # Countdown
        # -------------------------------------------------

        session.state = RegistrationState.READY_TO_CAPTURE

        completed = self._countdown_service.update()

        session.countdown = self._countdown_service.remaining

        if not completed:

            logger.debug(
                f"Registration : Countdown {session.countdown}"
            )

            return session

        # -------------------------------------------------
        # Capture
        # -------------------------------------------------

        session.state = RegistrationState.CAPTURING

        self._best_frame_collector.add(face_result)

        logger.debug("Registration : Capturing Best Frame")

        # -------------------------------------------------
        # Enough frames?
        # -------------------------------------------------

        if not self._best_frame_collector.is_complete():

            return session

        # -------------------------------------------------
        # Next Pose
        # -------------------------------------------------

        logger.info(
            f"Pose Completed : {session.current_pose}"
        )

        has_next_pose = self._registration_manager.next_pose()

        # -------------------------------------------------
        # Registration Completed
        # -------------------------------------------------

        if not has_next_pose:

            session.state = RegistrationState.COMPLETED

            logger.success(
                f"Registration Completed : {session.person_id}"
            )

            return session

        # -------------------------------------------------
        # Prepare next pose
        # -------------------------------------------------

        self._best_frame_collector.reset()

        self._stable_face_service.reset()

        self._countdown_service.reset()

        session.state = RegistrationState.ALIGN_FACE

        logger.info(
            f"Next Pose : {session.current_pose}"
        )

        return session