from enum import Enum


class OutboundNATMappingPoolopts(str, Enum):
    BITMASK = "bitmask"
    RANDOM = "random"
    RANDOM_STICKY_ADDRESS = "random sticky-address"
    ROUND_ROBIN = "round-robin"
    ROUND_ROBIN_STICKY_ADDRESS = "round-robin sticky-address"
    SOURCE_HASH = "source-hash"

    def __str__(self) -> str:
        return str(self.value)
