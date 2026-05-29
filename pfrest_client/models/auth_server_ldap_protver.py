from enum import IntEnum


class AuthServerLdapProtver(IntEnum):
    VALUE_2 = 2
    VALUE_3 = 3

    def __str__(self) -> str:
        return str(self.value)
