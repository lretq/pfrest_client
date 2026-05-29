from enum import Enum


class RESTAPISettingsRepresentInterfacesAs(str, Enum):
    DESCR = "descr"
    ID = "id"
    IF = "if"

    def __str__(self) -> str:
        return str(self.value)
