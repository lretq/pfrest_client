from enum import Enum


class OneToOneNATMappingIpprotocol(str, Enum):
    INET = "inet"
    INET6 = "inet6"

    def __str__(self) -> str:
        return str(self.value)
