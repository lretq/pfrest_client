from enum import Enum


class OpenVPNServerAllowCompression(str, Enum):
    ASYM = "asym"
    NO = "no"
    YES = "yes"

    def __str__(self) -> str:
        return str(self.value)
