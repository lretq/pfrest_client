from enum import Enum


class PortForwardNatreflection(str, Enum):
    DISABLE = "disable"
    ENABLE = "enable"
    PURENAT = "purenat"

    def __str__(self) -> str:
        return str(self.value)
