from enum import Enum


class FreeRADIUSLDAPServer1AccessAttrUsedForAllow(str, Enum):
    NO = "No"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
