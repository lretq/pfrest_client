from enum import Enum


class CertificateSigningRequestType(str, Enum):
    SERVER = "server"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
