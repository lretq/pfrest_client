from enum import Enum


class OpenVPNClientPingMethod(str, Enum):
    KEEPALIVE = "keepalive"
    PING = "ping"

    def __str__(self) -> str:
        return str(self.value)
