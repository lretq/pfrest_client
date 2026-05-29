from enum import Enum


class GetServicesCronJobsEndpointSortFlags(str, Enum):
    SORT_FLAG_CASE = "SORT_FLAG_CASE"
    SORT_LOCALE_STRING = "SORT_LOCALE_STRING"
    SORT_NATURAL = "SORT_NATURAL"
    SORT_NUMERIC = "SORT_NUMERIC"
    SORT_REGULAR = "SORT_REGULAR"
    SORT_STRING = "SORT_STRING"

    def __str__(self) -> str:
        return str(self.value)
