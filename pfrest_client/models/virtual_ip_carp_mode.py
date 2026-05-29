from enum import Enum


class VirtualIPCarpMode(str, Enum):
    MCAST = "mcast"
    UCAST = "ucast"

    def __str__(self) -> str:
        return str(self.value)
