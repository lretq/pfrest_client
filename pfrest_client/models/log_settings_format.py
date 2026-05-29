from enum import Enum


class LogSettingsFormat(str, Enum):
    RFC3164 = "rfc3164"
    RFC5424 = "rfc5424"

    def __str__(self) -> str:
        return str(self.value)
