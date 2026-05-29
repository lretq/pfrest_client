from enum import Enum


class TrafficShaperLimiterAqm(str, Enum):
    CODEL = "codel"
    DROPTAIL = "droptail"
    GRED = "gred"
    PIE = "pie"
    RED = "red"

    def __str__(self) -> str:
        return str(self.value)
