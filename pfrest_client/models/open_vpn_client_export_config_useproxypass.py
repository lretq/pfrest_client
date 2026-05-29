from enum import Enum


class OpenVPNClientExportConfigUseproxypass(str, Enum):
    BASIC = "basic"
    NONE = "none"
    NTLM = "ntlm"

    def __str__(self) -> str:
        return str(self.value)
