from enum import Enum


class OpenVPNClientDevMode(str, Enum):
    TAP = "tap"
    TUN = "tun"

    def __str__(self) -> str:
        return str(self.value)
