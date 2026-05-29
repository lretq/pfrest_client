from enum import IntEnum


class OpenVPNServerNetbiosNtype(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_4 = 4
    VALUE_8 = 8

    def __str__(self) -> str:
        return str(self.value)
