from enum import Enum


class HAProxyBackendCheckType(str, Enum):
    BASIC = "Basic"
    ESMTP = "ESMTP"
    HTTP = "HTTP"
    LDAP = "LDAP"
    MYSQL = "MySQL"
    NONE = "none"
    POSTGRESQL = "PostgreSQL"
    REDIS = "Redis"
    SMTP = "SMTP"
    SSL = "SSL"

    def __str__(self) -> str:
        return str(self.value)
