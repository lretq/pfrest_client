from enum import Enum


class HAProxyBackendHttpcheckMethod(str, Enum):
    DELETE = "DELETE"
    GET = "GET"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    POST = "POST"
    PUT = "PUT"
    TRACE = "TRACE"

    def __str__(self) -> str:
        return str(self.value)
