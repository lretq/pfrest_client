from enum import Enum


class DNSResolverSettingsPythonOrder(str, Enum):
    POST_VALIDATOR = "post_validator"
    PRE_VALIDATOR = "pre_validator"

    def __str__(self) -> str:
        return str(self.value)
