from enum import Enum


class OneToOneNATMappingNatreflection(str, Enum):
    DISABLE = "disable"
    ENABLE = "enable"

    def __str__(self) -> str:
        return str(self.value)
