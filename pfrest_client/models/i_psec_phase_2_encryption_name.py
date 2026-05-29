from enum import Enum


class IPsecPhase2EncryptionName(str, Enum):
    AES = "aes"
    AES128GCM = "aes128gcm"
    AES192GCM = "aes192gcm"
    AES256GCM = "aes256gcm"
    CHACHA20POLY1305 = "chacha20poly1305"

    def __str__(self) -> str:
        return str(self.value)
