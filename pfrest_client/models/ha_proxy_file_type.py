from enum import Enum


class HAProxyFileType(str, Enum):
    LUASCRIPT = "luascript"
    WRITETODISK = "writetodisk"

    def __str__(self) -> str:
        return str(self.value)
