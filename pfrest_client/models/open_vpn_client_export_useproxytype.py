from enum import Enum


class OpenVPNClientExportUseproxytype(str, Enum):
    HTTP = "http"
    SOCKS = "socks"

    def __str__(self) -> str:
        return str(self.value)
