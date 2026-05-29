from enum import Enum


class OpenVPNClientExportType(str, Enum):
    CONFINLINE = "confinline"
    CONFINLINECONNECT = "confinlineconnect"
    CONFINLINEDROID = "confinlinedroid"
    CONFINLINEVISC = "confinlinevisc"
    CONFZIP = "confzip"
    CONF_SNOM = "conf_snom"
    CONF_YEALINK_T28 = "conf_yealink_t28"
    CONF_YEALINK_T38G = "conf_yealink_t38g"
    CONF_YEALINK_T38G2 = "conf_yealink_t38g2"
    INST_WIN10 = "inst-Win10"
    INST_WIN7 = "inst-Win7"
    INST_X64_CURRENT = "inst-x64-current"
    INST_X64_PREVIOUS = "inst-x64-previous"
    INST_X86_CURRENT = "inst-x86-current"
    INST_X86_PREVIOUS = "inst-x86-previous"
    VISC = "visc"

    def __str__(self) -> str:
        return str(self.value)
