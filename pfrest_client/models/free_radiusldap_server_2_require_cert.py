from enum import Enum


class FreeRADIUSLDAPServer2RequireCert(str, Enum):
    ALLOW = "allow"
    DEMAND = "demand"
    HARD = "hard"
    NEVER = "never"
    TRY = "try"

    def __str__(self) -> str:
        return str(self.value)
