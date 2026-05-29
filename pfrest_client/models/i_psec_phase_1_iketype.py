from enum import Enum


class IPsecPhase1Iketype(str, Enum):
    AUTO = "auto"
    IKEV1 = "ikev1"
    IKEV2 = "ikev2"

    def __str__(self) -> str:
        return str(self.value)
