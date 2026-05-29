from enum import Enum


class FreeRADIUSLDAPServer1MsadCompatibilityEnable(str, Enum):
    DISABLE = "Disable"
    ENABLE = "Enable"

    def __str__(self) -> str:
        return str(self.value)
