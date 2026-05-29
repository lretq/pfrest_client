from enum import Enum


class RoutingGatewayGwDownKillStates(str, Enum):
    DOWN = "down"
    NONE = "none"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
