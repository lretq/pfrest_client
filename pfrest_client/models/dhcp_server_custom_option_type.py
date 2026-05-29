from enum import Enum


class DHCPServerCustomOptionType(str, Enum):
    BOOLEAN = "boolean"
    IP_ADDRESS = "ip-address"
    SIGNED_INTEGER_16 = "signed integer 16"
    SIGNED_INTEGER_32 = "signed integer 32"
    SIGNED_INTEGER_8 = "signed integer 8"
    STRING = "string"
    TEXT = "text"
    UNSIGNED_INTEGER_16 = "unsigned integer 16"
    UNSIGNED_INTEGER_32 = "unsigned integer 32"
    UNSIGNED_INTEGER_8 = "unsigned integer 8"

    def __str__(self) -> str:
        return str(self.value)
