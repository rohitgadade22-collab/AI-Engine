from dataclasses import dataclass


@dataclass
class RegistrationResult:

    score: int

    ready: bool

    message: str