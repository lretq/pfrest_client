from enum import Enum


class OpenVPNClientCreateGw(str, Enum):
    BOTH = "both"
    V4ONLY = "v4only"
    V6ONLY = "v6only"

    def __str__(self) -> str:
        return str(self.value)
