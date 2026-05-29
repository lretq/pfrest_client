from enum import Enum


class FirewallAliasType(str, Enum):
    HOST = "host"
    NETWORK = "network"
    PORT = "port"

    def __str__(self) -> str:
        return str(self.value)
