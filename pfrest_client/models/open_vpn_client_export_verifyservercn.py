from enum import Enum


class OpenVPNClientExportVerifyservercn(str, Enum):
    AUTO = "auto"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
