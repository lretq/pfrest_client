from enum import Enum


class FreeRADIUSInterfaceType(str, Enum):
    ACCT = "acct"
    AUTH = "auth"
    COA = "coa"
    DETAIL = "detail"
    PROXY = "proxy"
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
