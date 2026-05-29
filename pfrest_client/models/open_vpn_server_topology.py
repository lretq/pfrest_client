from enum import Enum


class OpenVPNServerTopology(str, Enum):
    NET30 = "net30"
    SUBNET = "subnet"

    def __str__(self) -> str:
        return str(self.value)
