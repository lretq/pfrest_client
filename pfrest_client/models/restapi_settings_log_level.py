from enum import Enum


class RESTAPISettingsLogLevel(str, Enum):
    LOG_ALERT = "LOG_ALERT"
    LOG_CRIT = "LOG_CRIT"
    LOG_DEBUG = "LOG_DEBUG"
    LOG_EMERG = "LOG_EMERG"
    LOG_ERR = "LOG_ERR"
    LOG_INFO = "LOG_INFO"
    LOG_NOTICE = "LOG_NOTICE"
    LOG_WARNING = "LOG_WARNING"

    def __str__(self) -> str:
        return str(self.value)
