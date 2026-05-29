from enum import Enum


class InterfaceLAGGLacptimeout(str, Enum):
    FAST = "fast"
    SLOW = "slow"

    def __str__(self) -> str:
        return str(self.value)
