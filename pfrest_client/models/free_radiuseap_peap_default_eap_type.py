from enum import Enum


class FreeRADIUSEAPPeapDefaultEapType(str, Enum):
    GTC = "gtc"
    MD5 = "md5"
    MSCHAPV2 = "mschapv2"
    OTP = "otp"
    TLS = "tls"

    def __str__(self) -> str:
        return str(self.value)
