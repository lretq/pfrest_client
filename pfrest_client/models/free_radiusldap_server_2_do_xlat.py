from enum import Enum


class FreeRADIUSLDAPServer2DoXlat(str, Enum):
    NO = "No"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
