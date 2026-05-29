from enum import Enum


class IPsecPhase1AuthenticationMethod(str, Enum):
    CERT = "cert"
    PRE_SHARED_KEY = "pre_shared_key"

    def __str__(self) -> str:
        return str(self.value)
