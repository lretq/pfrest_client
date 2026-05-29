from enum import Enum


class IPsecPhase1MyidType(str, Enum):
    ADDRESS = "address"
    ASN1DN = "asn1dn"
    AUTO = "auto"
    DYN_DNS = "dyn_dns"
    FQDN = "fqdn"
    KEYID_TAG = "keyid tag"
    MYADDRESS = "myaddress"
    USER_FQDN = "user_fqdn"

    def __str__(self) -> str:
        return str(self.value)
