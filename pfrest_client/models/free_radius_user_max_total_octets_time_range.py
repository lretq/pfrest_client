from enum import Enum


class FreeRADIUSUserMaxTotalOctetsTimeRange(str, Enum):
    DAILY = "daily"
    FOREVER = "forever"
    MONTHLY = "monthly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
