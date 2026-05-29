from enum import Enum


class NetworkInterfaceTypev4(str, Enum):
    DHCP = "dhcp"
    NONE = "none"
    STATIC = "static"

    def __str__(self) -> str:
        return str(self.value)
