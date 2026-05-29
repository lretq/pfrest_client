from enum import Enum


class AuthServerLdapUrltype(str, Enum):
    SSLTLS_ENCRYPTED = "SSL/TLS Encrypted"
    STANDARD_TCP = "Standard TCP"
    STARTTLS_ENCRYPT = "STARTTLS Encrypt"

    def __str__(self) -> str:
        return str(self.value)
