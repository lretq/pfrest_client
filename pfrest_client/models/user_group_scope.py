from enum import Enum


class UserGroupScope(str, Enum):
    LOCAL = "local"
    REMOTE = "remote"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
