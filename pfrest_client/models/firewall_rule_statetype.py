from enum import Enum


class FirewallRuleStatetype(str, Enum):
    KEEP_STATE = "keep state"
    NONE = "none"
    SLOPPY_STATE = "sloppy state"
    SYNPROXY_STATE = "synproxy state"

    def __str__(self) -> str:
        return str(self.value)
