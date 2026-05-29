from enum import Enum


class HAProxyBackendPersistCookieMode(str, Enum):
    INSERT_ONLY = "insert-only"
    INSERT_ONLY_SILENT = "insert-only-silent"
    PASSIVE = "passive"
    PASSIVE_SESSION_PREFIX = "passive-session-prefix"
    PASSIVE_SILENT = "passive-silent"
    RESET = "reset"
    SESSION_PREFIX = "session-prefix"
    SET = "set"
    SET_SILENT = "set-silent"

    def __str__(self) -> str:
        return str(self.value)
