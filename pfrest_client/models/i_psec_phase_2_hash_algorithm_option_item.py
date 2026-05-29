from enum import Enum


class IPsecPhase2HashAlgorithmOptionItem(str, Enum):
    AESXCBC = "aesxcbc"
    HMAC_SHA1 = "hmac_sha1"
    HMAC_SHA256 = "hmac_sha256"
    HMAC_SHA384 = "hmac_sha384"
    HMAC_SHA512 = "hmac_sha512"

    def __str__(self) -> str:
        return str(self.value)
