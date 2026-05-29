from enum import Enum


class ACMECertificateActionMethod(str, Enum):
    PHP_COMMAND = "php_command"
    SERVICERESTART = "servicerestart"
    SHELLCOMMAND = "shellcommand"
    XMLRPCSERVICERESTART = "xmlrpcservicerestart"

    def __str__(self) -> str:
        return str(self.value)
