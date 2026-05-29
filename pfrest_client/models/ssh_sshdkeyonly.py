from enum import Enum


class SSHSshdkeyonly(str, Enum):
    BOTH = "both"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
