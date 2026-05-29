from enum import Enum


class NetworkInterfaceTypev6(str, Enum):
    DHCP6 = "dhcp6"
    NONE = "none"
    SLAAC = "slaac"
    STATICV6 = "staticv6"
    TRACK6 = "track6"
    VALUE_3 = "6rd"
    VALUE_5 = "6to4"

    def __str__(self) -> str:
        return str(self.value)
