from enum import Enum


class NTPSettingsDnsresolv(str, Enum):
    AUTO = "auto"
    INET = "inet"
    INET6 = "inet6"

    def __str__(self) -> str:
        return str(self.value)
