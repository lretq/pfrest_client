from enum import Enum


class VirtualIPType(str, Enum):
    NETWORK = "network"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
