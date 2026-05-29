from enum import Enum


class BINDZoneRecordType(str, Enum):
    A = "A"
    AAAA = "AAAA"
    CNAME = "CNAME"
    LOC = "LOC"
    MX = "MX"
    NS = "NS"
    PTR = "PTR"
    SPF = "SPF"
    SRV = "SRV"
    TXT = "TXT"

    def __str__(self) -> str:
        return str(self.value)
