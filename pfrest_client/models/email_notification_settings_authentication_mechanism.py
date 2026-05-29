from enum import Enum


class EmailNotificationSettingsAuthenticationMechanism(str, Enum):
    LOGIN = "LOGIN"
    PLAIN = "PLAIN"

    def __str__(self) -> str:
        return str(self.value)
