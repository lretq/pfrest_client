from enum import Enum


class FreeRADIUSUserPointOfTime(str, Enum):
    DAILY = "Daily"
    FOREVER = "Forever"
    MONTHLY = "Monthly"
    WEEKLY = "Weekly"

    def __str__(self) -> str:
        return str(self.value)
