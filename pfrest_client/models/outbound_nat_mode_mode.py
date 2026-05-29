from enum import Enum


class OutboundNATModeMode(str, Enum):
    ADVANCED = "advanced"
    AUTOMATIC = "automatic"
    DISABLED = "disabled"
    HYBRID = "hybrid"

    def __str__(self) -> str:
        return str(self.value)
