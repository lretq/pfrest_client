from enum import IntEnum


class OpenVPNServerSndrcvbuf(IntEnum):
    VALUE_65536 = 65536
    VALUE_131072 = 131072
    VALUE_262144 = 262144
    VALUE_524288 = 524288
    VALUE_1048576 = 1048576
    VALUE_2097152 = 2097152

    def __str__(self) -> str:
        return str(self.value)
