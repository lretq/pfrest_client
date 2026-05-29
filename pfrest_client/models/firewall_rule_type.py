from enum import Enum


class FirewallRuleType(str, Enum):
    BLOCK = "block"
    PASS = "pass"
    REJECT = "reject"

    def __str__(self) -> str:
        return str(self.value)
