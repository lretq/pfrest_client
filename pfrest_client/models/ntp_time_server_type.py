from enum import Enum


class NTPTimeServerType(str, Enum):
    PEER = "peer"
    POOL = "pool"
    SERVER = "server"

    def __str__(self) -> str:
        return str(self.value)
