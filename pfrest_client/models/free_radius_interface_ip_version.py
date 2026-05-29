from enum import Enum


class FreeRADIUSInterfaceIpVersion(str, Enum):
    IPADDR = "ipaddr"
    IPV6ADDR = "ipv6addr"

    def __str__(self) -> str:
        return str(self.value)
