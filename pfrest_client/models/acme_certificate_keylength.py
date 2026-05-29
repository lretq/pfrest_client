from enum import Enum


class ACMECertificateKeylength(str, Enum):
    CUSTOM = "custom"
    EC_256 = "ec-256"
    EC_384 = "ec-384"
    VALUE_0 = "2048"
    VALUE_1 = "3072"
    VALUE_2 = "4096"

    def __str__(self) -> str:
        return str(self.value)
