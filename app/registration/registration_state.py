# registration_state.py

from enum import Enum


class RegistrationState(str, Enum):
    IDLE = "IDLE"

    WAIT_FACE = "WAIT_FACE"

    ALIGN_FACE = "ALIGN_FACE"

    HOLD_STILL = "HOLD_STILL"

    READY = "READY"

    READY_TO_CAPTURE = "READY_TO_CAPTURE"

    CAPTURING = "CAPTURING"

    NEXT_POSE = "NEXT_POSE"

    COMPLETED = "COMPLETED"

    CANCELLED = "CANCELLED"