from enum import Enum


class OpenVPNServerPingAction(str, Enum):
    PING_EXIT = "ping_exit"
    PING_RESTART = "ping_restart"

    def __str__(self) -> str:
        return str(self.value)
