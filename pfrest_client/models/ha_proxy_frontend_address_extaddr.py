from enum import Enum


class HAProxyFrontendAddressExtaddr(str, Enum):
    ANY_IPV4 = "any_ipv4"
    ANY_IPV6 = "any_ipv6"
    CUSTOM = "custom"
    LOCALHOST_IPV4 = "localhost_ipv4"
    LOCALHOST_IPV6 = "localhost_ipv6"

    def __str__(self) -> str:
        return str(self.value)
