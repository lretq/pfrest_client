from enum import Enum


class OpenVPNClientExportConfigUseproxytype(str, Enum):
    HTTP = "http"
    SOCKS = "socks"

    def __str__(self) -> str:
        return str(self.value)
