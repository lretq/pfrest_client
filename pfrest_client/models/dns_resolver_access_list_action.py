from enum import Enum


class DNSResolverAccessListAction(str, Enum):
    ALLOW = "allow"
    ALLOW_SNOOP = "allow snoop"
    DENY = "deny"
    DENY_NONLOCAL = "deny nonlocal"
    REFUSE = "refuse"
    REFUSE_NONLOCAL = "refuse nonlocal"

    def __str__(self) -> str:
        return str(self.value)
