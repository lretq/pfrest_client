from enum import Enum


class IPsecPhase2Mode(str, Enum):
    TRANSPORT = "transport"
    TUNNEL = "tunnel"
    TUNNEL6 = "tunnel6"
    VTI = "vti"

    def __str__(self) -> str:
        return str(self.value)
