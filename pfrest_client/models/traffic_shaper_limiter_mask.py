from enum import Enum


class TrafficShaperLimiterMask(str, Enum):
    DSTADDRESS = "dstaddress"
    NONE = "none"
    SRCADDRESS = "srcaddress"

    def __str__(self) -> str:
        return str(self.value)
