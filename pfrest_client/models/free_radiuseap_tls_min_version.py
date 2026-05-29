from enum import Enum


class FreeRADIUSEAPTlsMinVersion(str, Enum):
    VALUE_0 = "1.0"
    VALUE_1 = "1.1"
    VALUE_2 = "1.2"

    def __str__(self) -> str:
        return str(self.value)
