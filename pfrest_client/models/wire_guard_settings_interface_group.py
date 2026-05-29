from enum import Enum


class WireGuardSettingsInterfaceGroup(str, Enum):
    ALL = "all"
    NONE = "none"
    UNASSIGNED = "unassigned"

    def __str__(self) -> str:
        return str(self.value)
