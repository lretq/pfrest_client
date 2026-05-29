from enum import Enum


class FreeRADIUSEAPPeapSohEnable(str, Enum):
    DISABLE = "Disable"
    ENABLE = "Enable"

    def __str__(self) -> str:
        return str(self.value)
