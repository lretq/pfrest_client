from enum import Enum


class IPsecPhase1PeeridType(str, Enum):
    ADDRESS = "address"
    ANY = "any"
    ASN1DN = "asn1dn"
    AUTO = "auto"
    DYN_DNS = "dyn_dns"
    FQDN = "fqdn"
    KEYID_TAG = "keyid tag"
    PEERADDRESS = "peeraddress"
    USER_FQDN = "user_fqdn"

    def __str__(self) -> str:
        return str(self.value)
