from enum import Enum


class IPsecPhase1Closeaction(str, Enum):
    NONE = "none"
    START = "start"
    TRAP = "trap"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
