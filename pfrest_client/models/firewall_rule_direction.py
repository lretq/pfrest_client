from enum import Enum


class FirewallRuleDirection(str, Enum):
    ANY = "any"
    IN = "in"
    OUT = "out"

    def __str__(self) -> str:
        return str(self.value)
