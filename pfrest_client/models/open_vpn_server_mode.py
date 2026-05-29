from enum import Enum


class OpenVPNServerMode(str, Enum):
    P2P_TLS = "p2p_tls"
    SERVER_TLS = "server_tls"
    SERVER_TLS_USER = "server_tls_user"
    SERVER_USER = "server_user"

    def __str__(self) -> str:
        return str(self.value)
