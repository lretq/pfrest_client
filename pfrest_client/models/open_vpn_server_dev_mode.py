from enum import Enum


class OpenVPNServerDevMode(str, Enum):
    TAP = "tap"
    TUN = "tun"

    def __str__(self) -> str:
        return str(self.value)
