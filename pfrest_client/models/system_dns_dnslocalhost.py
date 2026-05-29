from enum import Enum


class SystemDNSDnslocalhost(str, Enum):
    LOCAL = "local"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
