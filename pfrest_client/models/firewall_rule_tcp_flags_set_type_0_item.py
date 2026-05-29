from enum import Enum


class FirewallRuleTcpFlagsSetType0Item(str, Enum):
    ACK = "ack"
    CWR = "cwr"
    ECE = "ece"
    FIN = "fin"
    PSH = "psh"
    RST = "rst"
    SYN = "syn"
    URG = "urg"

    def __str__(self) -> str:
        return str(self.value)
