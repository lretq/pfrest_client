from enum import Enum


class CertificateRevocationListMethod(str, Enum):
    EXISTING = "existing"
    INTERNAL = "internal"

    def __str__(self) -> str:
        return str(self.value)
