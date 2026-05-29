from enum import Enum


class OpenVPNClientTopology(str, Enum):
    NET30 = "net30"
    SUBNET = "subnet"

    def __str__(self) -> str:
        return str(self.value)
