from pydantic import BaseModel
from datetime import datetime

from app.registration.registration_state import RegistrationState
from app.registration.registration_pose import RegistrationPose


class RegistrationSession(BaseModel):

    session_id: str

    employee_id: str

    employee_name: str

    state: RegistrationState

    current_pose: RegistrationPose

    pose_index: int = 0

    countdown: int = 3

    registration_score: float = 0.0

    completed: bool = False

    started_at: datetime

    updated_at: datetime