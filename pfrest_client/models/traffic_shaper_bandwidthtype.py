from enum import Enum


class TrafficShaperBandwidthtype(str, Enum):
    B = "b"
    GB = "Gb"
    KB = "Kb"
    MB = "Mb"
    VALUE_0 = "%"

    def __str__(self) -> str:
        return str(self.value)
