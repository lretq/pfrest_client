from enum import Enum


class FreeRADIUSUserPasswordEncryption(str, Enum):
    CLEARTEXT_PASSWORD = "Cleartext-Password"
    MD5_PASSWORD = "MD5-Password"
    MD5_PASSWORD_HASHED = "MD5-Password-hashed"
    NT_PASSWORD_HASHED = "NT-Password-hashed"

    def __str__(self) -> str:
        return str(self.value)
