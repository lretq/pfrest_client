from enum import Enum


class FreeRADIUSLDAPFailoverMode(str, Enum):
    LOAD_BALANCE = "load-balance"
    REDUNDANT = "redundant"

    def __str__(self) -> str:
        return str(self.value)
