from enum import Enum


class FreeRADIUSEAPDefaultEapType(str, Enum):
    GTC = "gtc"
    LEAP = "leap"
    MD5 = "md5"
    MSCHAPV2 = "mschapv2"
    PEAP = "peap"
    TLS = "tls"
    TTLS = "ttls"

    def __str__(self) -> str:
        return str(self.value)
