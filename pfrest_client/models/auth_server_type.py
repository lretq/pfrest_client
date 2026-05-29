from enum import Enum


class AuthServerType(str, Enum):
    LDAP = "ldap"
    RADIUS = "radius"

    def __str__(self) -> str:
        return str(self.value)
