from enum import Enum


class DNSResolverSettingsSystemDomainLocalZoneType(str, Enum):
    DENY = "deny"
    INFORM = "inform"
    INFORM_DENY = "inform_deny"
    NODEFAULT = "nodefault"
    REDIRECT = "redirect"
    REFUSE = "refuse"
    STATIC = "static"
    TRANSPARENT = "transparent"
    TYPETRANSPARENT = "typetransparent"

    def __str__(self) -> str:
        return str(self.value)
