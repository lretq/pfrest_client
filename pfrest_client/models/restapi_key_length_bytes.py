from enum import IntEnum


class RESTAPIKeyLengthBytes(IntEnum):
    VALUE_16 = 16
    VALUE_24 = 24
    VALUE_32 = 32
    VALUE_64 = 64

    def __str__(self) -> str:
        return str(self.value)
