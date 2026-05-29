from enum import Enum


class IPsecPhase1NatTraversal(str, Enum):
    FORCE = "force"
    ON = "on"

    def __str__(self) -> str:
        return str(self.value)
