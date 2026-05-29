from enum import Enum


class RoutingGatewayGroupTrigger(str, Enum):
    DOWN = "down"
    DOWNLATENCY = "downlatency"
    DOWNLOSS = "downloss"
    DOWNLOSSLATENCY = "downlosslatency"

    def __str__(self) -> str:
        return str(self.value)
