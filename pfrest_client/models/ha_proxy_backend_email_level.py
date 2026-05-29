from enum import Enum


class HAProxyBackendEmailLevel(str, Enum):
    ALERT = "alert"
    CRIT = "crit"
    DEBUG = "debug"
    DONTLOG = "dontlog"
    EMERG = "emerg"
    ERR = "err"
    INFO = "info"
    NOTICE = "notice"
    VALUE_0 = ""
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
