from enum import Enum


class OutboundNATMappingProtocol(str, Enum):
    AH = "ah"
    ESP = "esp"
    GRE = "gre"
    ICMP = "icmp"
    IGMP = "igmp"
    IPV6 = "ipv6"
    OSPF = "ospf"
    PIM = "pim"
    TCP = "tcp"
    TCPUDP = "tcp/udp"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)
