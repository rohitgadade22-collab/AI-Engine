from dataclasses import dataclass
from typing import List


@dataclass
class FaceResult:

    confidence: float

    bbox: List[int]

    landmarks: List

    frame_width: int

    frame_height: int

    face_image: any