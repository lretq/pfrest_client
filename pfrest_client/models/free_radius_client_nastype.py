from enum import Enum


class FreeRADIUSClientNastype(str, Enum):
    CISCO = "cisco"
    COMPUTONE = "computone"
    CVX = "cvx"
    DIGITRO = "digitro"
    DOT1X = "dot1x"
    JUNIPER = "juniper"
    LIVINGSTON = "livingston"
    MAX40XX = "max40xx"
    MIKROTIK = "mikrotik"
    MIKROTIK_SNMP = "mikrotik_snmp"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
