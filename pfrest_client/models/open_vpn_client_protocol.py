from enum import Enum


class OpenVPNClientProtocol(str, Enum):
    TCP = "TCP"
    TCP4 = "TCP4"
    TCP6 = "TCP6"
    UDP = "UDP"
    UDP4 = "UDP4"
    UDP6 = "UDP6"

    def __str__(self) -> str:
        return str(self.value)
