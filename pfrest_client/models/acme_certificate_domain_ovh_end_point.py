from enum import Enum


class ACMECertificateDomainOvhEndPoint(str, Enum):
    KIMSUFI_CA = "kimsufi-ca"
    KIMSUFI_EU = "kimsufi-eu"
    OVH_CA = "ovh-ca"
    OVH_EU = "ovh-eu"
    RUNABOVE_CA = "runabove-ca"
    SOYOUSTART_CA = "soyoustart-ca"
    SOYOUSTART_EU = "soyoustart-eu"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
