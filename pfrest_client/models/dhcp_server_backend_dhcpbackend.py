from enum import Enum


class DHCPServerBackendDhcpbackend(str, Enum):
    ISC = "isc"
    KEA = "kea"

    def __str__(self) -> str:
        return str(self.value)
