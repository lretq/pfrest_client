from enum import Enum


class HAProxySettingsEmailLevel(str, Enum):
    ALERT = "alert"
    CRIT = "crit"
    DEBUG = "debug"
    EMERG = "emerg"
    ERR = "err"
    INFO = "info"
    NOTICE = "notice"
    VALUE_0 = ""
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
