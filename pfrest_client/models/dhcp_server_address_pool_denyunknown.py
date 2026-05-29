from enum import Enum


class DHCPServerAddressPoolDenyunknown(str, Enum):
    CLASS = "class"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
