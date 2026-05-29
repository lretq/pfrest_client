from enum import Enum


class ACMECertificateDomainNwApiEndpoint(str, Enum):
    HTTPSCORE_THERMO_IO = "https:\/\/core.thermo.io"
    HTTPSMY_FUTUREHOSTING_COM = "https:\/\/my.futurehosting.com"
    HTTPSPORTAL_NEXCESS_NET = "https:\/\/portal.nexcess.net"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
