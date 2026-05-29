from enum import Enum


class CertificateGenerateType(str, Enum):
    SERVER = "server"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
