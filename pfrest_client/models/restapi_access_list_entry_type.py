from enum import Enum


class RESTAPIAccessListEntryType(str, Enum):
    ALLOW = "allow"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
