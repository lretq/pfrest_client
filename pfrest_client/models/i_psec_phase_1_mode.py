from enum import Enum


class IPsecPhase1Mode(str, Enum):
    AGGRESSIVE = "aggressive"
    MAIN = "main"

    def __str__(self) -> str:
        return str(self.value)
