from enum import Enum


class CertificatePKCS12ExportEncryption(str, Enum):
    HIGH = "high"
    LEGACY = "legacy"
    LOW = "low"

    def __str__(self) -> str:
        return str(self.value)
