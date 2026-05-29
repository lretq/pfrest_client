from enum import Enum


class OpenVPNClientTlsType(str, Enum):
    AUTH = "auth"
    CRYPT = "crypt"

    def __str__(self) -> str:
        return str(self.value)
