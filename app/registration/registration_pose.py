from enum import Enum


class RegistrationPose(str, Enum):

    FRONT = "FRONT"

    LEFT = "LEFT"

    RIGHT = "RIGHT"

    UP = "UP"

    DOWN = "DOWN"