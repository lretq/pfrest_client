from enum import Enum


class VirtualIPMode(str, Enum):
    CARP = "carp"
    IPALIAS = "ipalias"
    OTHER = "other"
    PROXYARP = "proxyarp"

    def __str__(self) -> str:
        return str(self.value)
