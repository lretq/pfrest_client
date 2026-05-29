from enum import Enum


class BINDSettingsLogSeverity(str, Enum):
    CRITICAL = "critical"
    DEBUG_1 = "debug 1"
    DEBUG_3 = "debug 3"
    DEBUG_5 = "debug 5"
    DYNAMIC = "dynamic"
    ERROR = "error"
    INFO = "info"
    NOTICE = "notice"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
