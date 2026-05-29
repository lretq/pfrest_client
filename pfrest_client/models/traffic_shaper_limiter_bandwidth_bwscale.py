from enum import Enum


class TrafficShaperLimiterBandwidthBwscale(str, Enum):
    B = "b"
    KB = "Kb"
    MB = "Mb"

    def __str__(self) -> str:
        return str(self.value)
