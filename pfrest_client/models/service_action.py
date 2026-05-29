from enum import Enum


class ServiceAction(str, Enum):
    RESTART = "restart"
    START = "start"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
