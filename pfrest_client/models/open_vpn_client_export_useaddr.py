from enum import Enum


class OpenVPNClientExportUseaddr(str, Enum):
    OTHER = "other"
    SERVERADDR = "serveraddr"
    SERVERHOSTNAME = "serverhostname"
    SERVERMAGIC = "servermagic"
    SERVERMAGICHOST = "servermagichost"

    def __str__(self) -> str:
        return str(self.value)
