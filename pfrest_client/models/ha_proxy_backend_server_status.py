from enum import Enum


class HAProxyBackendServerStatus(str, Enum):
    ACTIVE = "active"
    BACKUP = "backup"
    DISABLED = "disabled"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
