from enum import Enum


class HAProxyFrontendHttpclose(str, Enum):
    FORCECLOSE = "forceclose"
    HTTPCLOSE = "httpclose"
    HTTP_KEEP_ALIVE = "http-keep-alive"
    HTTP_SERVER_CLOSE = "http-server-close"
    HTTP_TUNNEL = "http-tunnel"

    def __str__(self) -> str:
        return str(self.value)
