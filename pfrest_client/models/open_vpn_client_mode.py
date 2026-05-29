from enum import Enum


class OpenVPNClientMode(str, Enum):
    P2P_TLS = "p2p_tls"

    def __str__(self) -> str:
        return str(self.value)
