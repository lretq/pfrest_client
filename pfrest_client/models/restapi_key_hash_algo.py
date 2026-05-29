from enum import Enum


class RESTAPIKeyHashAlgo(str, Enum):
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"

    def __str__(self) -> str:
        return str(self.value)
