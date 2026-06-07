from dataclasses import dataclass
import numpy as np


@dataclass
class BestFrame:

    image: np.ndarray

    score: float

    timestamp: float

    pose: str