from enum import Enum


class FreeRADIUSUserMotpAuthmethod(str, Enum):
    GOOGLEAUTH = "googleauth"
    MOTP = "motp"

    def __str__(self) -> str:
        return str(self.value)
