from enum import Enum


class BINDSettingsLogOptionsItem(str, Enum):
    CLIENT = "client"
    CONFIG = "config"
    DATABASE = "database"
    DEFAULT = "default"
    DISPATCH = "dispatch"
    DNSSEC = "dnssec"
    GENERAL = "general"
    LAME_SERVERS = "lame-servers"
    NETWORK = "network"
    NOTIFY = "notify"
    QUERIES = "queries"
    RESOLVER = "resolver"
    SECURITY = "security"
    UNMATCHED = "unmatched"
    UPDATE = "update"
    XFER_IN = "xfer-in"
    XFER_OUT = "xfer-out"

    def __str__(self) -> str:
        return str(self.value)
