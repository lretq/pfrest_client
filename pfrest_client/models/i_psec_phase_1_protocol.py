from enum import Enum


class IPsecPhase1Protocol(str, Enum):
    BOTH = "both"
    INET = "inet"
    INET6 = "inet6"

    def __str__(self) -> str:
        return str(self.value)
