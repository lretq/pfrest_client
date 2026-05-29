from enum import Enum


class FirewallRuleProtocol(str, Enum):
    AH = "ah"
    CARP = "carp"
    ESP = "esp"
    GRE = "gre"
    ICMP = "icmp"
    IGMP = "igmp"
    IPV6 = "ipv6"
    OSPF = "ospf"
    PFSYNC = "pfsync"
    PIM = "pim"
    TCP = "tcp"
    TCPUDP = "tcp/udp"
    UDP = "udp"

    def __str__(self) -> str:
        return str(self.value)
