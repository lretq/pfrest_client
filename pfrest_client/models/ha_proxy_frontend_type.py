from enum import Enum


class HAProxyFrontendType(str, Enum):
    HTTP = "http"
    HTTPS = "https"
    TCP = "tcp"

    def __str__(self) -> str:
        return str(self.value)
