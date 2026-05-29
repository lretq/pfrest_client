from enum import Enum


class HAProxyBackendPersistStickyType(str, Enum):
    NONE = "none"
    STICK_COOKIE_VALUE = "stick_cookie_value"
    STICK_RDP_COOKIE = "stick_rdp_cookie"
    STICK_SOURCEIPV4 = "stick_sourceipv4"
    STICK_SOURCEIPV6 = "stick_sourceipv6"
    STICK_SSLSESSIONID = "stick_sslsessionid"

    def __str__(self) -> str:
        return str(self.value)
