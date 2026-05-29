from enum import Enum


class HAProxyBackendBalance(str, Enum):
    LEASTCONN = "leastconn"
    ROUNDROBIN = "roundrobin"
    SOURCE = "source"
    STATIC_RR = "static-rr"
    URI = "uri"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
