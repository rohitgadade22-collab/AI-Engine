from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class AIEvent:

    event_type: str

    device_id: str

    confidence: float

    data: Dict[str, Any] = field(default_factory=dict)

    timestamp: str = field(
        default_factory=lambda: datetime.now().isoformat()
    )