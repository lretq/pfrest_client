from enum import IntEnum


class CertificateSigningRequestKeylen(IntEnum):
    VALUE_1024 = 1024
    VALUE_2048 = 2048
    VALUE_3072 = 3072
    VALUE_4096 = 4096
    VALUE_6144 = 6144
    VALUE_7680 = 7680
    VALUE_8192 = 8192
    VALUE_15360 = 15360
    VALUE_16384 = 16384

    def __str__(self) -> str:
        return str(self.value)
