from enum import Enum


class NetworkInterfaceAdvDhcpPtValues(str, Enum):
    SAVEDCFG = "SavedCfg"

    def __str__(self) -> str:
        return str(self.value)
