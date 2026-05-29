from enum import Enum


class LogSettingsLogcompressiontype(str, Enum):
    BZIP2 = "bzip2"
    GZIP = "gzip"
    NONE = "none"
    XZ = "xz"
    ZSTD = "zstd"

    def __str__(self) -> str:
        return str(self.value)
