from enum import Enum


class InterfaceLAGGLagghash(str, Enum):
    L2 = "l2"
    L2L3 = "l2,l3"
    L2L3L4 = "l2,l3,l4"
    L2L4 = "l2,l4"
    L3 = "l3"
    L3L4 = "l3,l4"
    L4 = "l4"

    def __str__(self) -> str:
        return str(self.value)
