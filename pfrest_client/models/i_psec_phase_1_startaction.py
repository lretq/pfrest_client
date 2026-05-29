from enum import Enum


class IPsecPhase1Startaction(str, Enum):
    NONE = "none"
    START = "start"
    TRAP = "trap"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
