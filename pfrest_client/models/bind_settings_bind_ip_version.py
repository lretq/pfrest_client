from enum import Enum


class BINDSettingsBindIpVersion(str, Enum):
    VALUE_0 = ""
    VALUE_1 = "-4"
    VALUE_2 = "-6"

    def __str__(self) -> str:
        return str(self.value)
