from enum import Enum


class OpenVPNClientTlsauthKeydir(str, Enum):
    DEFAULT = "default"
    VALUE_1 = "0"
    VALUE_2 = "1"
    VALUE_3 = "2"

    def __str__(self) -> str:
        return str(self.value)
