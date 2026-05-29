from enum import Enum


class FreeRADIUSMACMaxTotalOctetsTimeRange(str, Enum):
    DAILY = "daily"
    FOREVER = "forever"
    MONTHLY = "monthly"
    WEEKLY = "weekly"

    def __str__(self) -> str:
        return str(self.value)
