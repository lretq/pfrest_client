from enum import Enum


class FirewallRuleIcmptypeItem(str, Enum):
    ALTHOST = "althost"
    ANY = "any"
    DATACONV = "dataconv"
    ECHOREP = "echorep"
    ECHOREQ = "echoreq"
    INFOREP = "inforep"
    INFOREQ = "inforeq"
    IPV6_HERE = "ipv6-here"
    IPV6_WHERE = "ipv6-where"
    MASKREP = "maskrep"
    MASKREQ = "maskreq"
    MOBREDIR = "mobredir"
    MOBREGREP = "mobregrep"
    MOBREGREQ = "mobregreq"
    PARAMPROB = "paramprob"
    PHOTURIS = "photuris"
    REDIR = "redir"
    ROUTERADV = "routeradv"
    ROUTERSOL = "routersol"
    SKIP = "skip"
    SQUENCH = "squench"
    TIMEREP = "timerep"
    TIMEREQ = "timereq"
    TIMEX = "timex"
    TRACE = "trace"
    UNREACH = "unreach"

    def __str__(self) -> str:
        return str(self.value)
