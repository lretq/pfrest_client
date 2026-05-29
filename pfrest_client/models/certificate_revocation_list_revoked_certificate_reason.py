from enum import IntEnum


class CertificateRevocationListRevokedCertificateReason(IntEnum):
    VALUE_NEGATIVE_1 = -1
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_9 = 9

    def __str__(self) -> str:
        return str(self.value)
