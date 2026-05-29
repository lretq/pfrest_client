from enum import Enum


class ACMECertificateDomainNsupdateKeyalgo(str, Enum):
    VALUE_0 = ""
    VALUE_1 = "157"
    VALUE_2 = "165"
    VALUE_3 = "164"
    VALUE_4 = "163"
    VALUE_5 = "162"
    VALUE_6 = "161"

    def __str__(self) -> str:
        return str(self.value)
