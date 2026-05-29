from enum import Enum


class BINDZoneType(str, Enum):
    FORWARD = "forward"
    MASTER = "master"
    REDIRECT = "redirect"
    SLAVE = "slave"

    def __str__(self) -> str:
        return str(self.value)
