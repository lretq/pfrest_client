from enum import Enum


class AuthServerRadiusProtocol(str, Enum):
    CHAP_MD5 = "CHAP_MD5"
    MSCHAPV1 = "MSCHAPv1"
    MSCHAPV2 = "MSCHAPv2"
    PAP = "PAP"

    def __str__(self) -> str:
        return str(self.value)
