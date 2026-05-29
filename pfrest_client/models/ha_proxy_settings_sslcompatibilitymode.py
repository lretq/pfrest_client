from enum import Enum


class HAProxySettingsSslcompatibilitymode(str, Enum):
    AUTO = "auto"
    INTERMEDIATE = "intermediate"
    MODERN = "modern"
    OLD = "old"

    def __str__(self) -> str:
        return str(self.value)
