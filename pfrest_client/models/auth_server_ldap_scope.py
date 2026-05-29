from enum import Enum


class AuthServerLdapScope(str, Enum):
    ONE = "one"
    SUBTREE = "subtree"

    def __str__(self) -> str:
        return str(self.value)
