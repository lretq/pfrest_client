from enum import Enum


class GetServicesHAProxyBackendActionsEndpointSortOrder(str, Enum):
    SORT_ASC = "SORT_ASC"
    SORT_DESC = "SORT_DESC"

    def __str__(self) -> str:
        return str(self.value)
