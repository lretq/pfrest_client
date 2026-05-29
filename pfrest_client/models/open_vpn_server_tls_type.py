from enum import Enum


class OpenVPNServerTlsType(str, Enum):
    AUTH = "auth"
    CRYPT = "crypt"

    def __str__(self) -> str:
        return str(self.value)
