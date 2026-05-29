from enum import Enum


class PortForwardIpprotocol(str, Enum):
    INET = "inet"
    INET46 = "inet46"
    INET6 = "inet6"

    def __str__(self) -> str:
        return str(self.value)
