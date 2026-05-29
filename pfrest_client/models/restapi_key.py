from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.restapi_key_hash_algo import RESTAPIKeyHashAlgo
from ..models.restapi_key_length_bytes import RESTAPIKeyLengthBytes
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTAPIKey")


@_attrs_define
class RESTAPIKey:
    """
    Attributes:
        descr (str | Unset): Sets a description for this API key. This is used to identify the key's purpose and cannot
            be changed once created.<br>
        username (None | str | Unset): The username this API key is issued to.<br>
        hash_algo (RESTAPIKeyHashAlgo | Unset): The hash algorithm used for this API key. It is recommended to increase
            the strength of the algorithm for keys assigned to privileged users.<br> Default: RESTAPIKeyHashAlgo.SHA256.
        length_bytes (RESTAPIKeyLengthBytes | Unset): The length of the API key (in bytes). Greater key lengths provide
            greater security, but also increase the number of characters used in the key string.<br> Default:
            RESTAPIKeyLengthBytes.VALUE_24.
        hash_ (None | str | Unset): The hash of the generated API key<br>
        key (None | str | Unset): The real API key. This value is not stored internally and cannot be recovered if
            lost.<br>
    """

    descr: str | Unset = UNSET
    username: None | str | Unset = UNSET
    hash_algo: RESTAPIKeyHashAlgo | Unset = RESTAPIKeyHashAlgo.SHA256
    length_bytes: RESTAPIKeyLengthBytes | Unset = RESTAPIKeyLengthBytes.VALUE_24
    hash_: None | str | Unset = UNSET
    key: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        descr = self.descr

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        hash_algo: str | Unset = UNSET
        if not isinstance(self.hash_algo, Unset):
            hash_algo = self.hash_algo.value

        length_bytes: int | Unset = UNSET
        if not isinstance(self.length_bytes, Unset):
            length_bytes = self.length_bytes.value

        hash_: None | str | Unset
        if isinstance(self.hash_, Unset):
            hash_ = UNSET
        else:
            hash_ = self.hash_

        key: None | str | Unset
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descr is not UNSET:
            field_dict["descr"] = descr
        if username is not UNSET:
            field_dict["username"] = username
        if hash_algo is not UNSET:
            field_dict["hash_algo"] = hash_algo
        if length_bytes is not UNSET:
            field_dict["length_bytes"] = length_bytes
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        descr = d.pop("descr", UNSET)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        _hash_algo = d.pop("hash_algo", UNSET)
        hash_algo: RESTAPIKeyHashAlgo | Unset
        if isinstance(_hash_algo, Unset):
            hash_algo = UNSET
        else:
            hash_algo = RESTAPIKeyHashAlgo(_hash_algo)

        _length_bytes = d.pop("length_bytes", UNSET)
        length_bytes: RESTAPIKeyLengthBytes | Unset
        if isinstance(_length_bytes, Unset):
            length_bytes = UNSET
        else:
            length_bytes = RESTAPIKeyLengthBytes(_length_bytes)

        def _parse_hash_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hash_ = _parse_hash_(d.pop("hash", UNSET))

        def _parse_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key = _parse_key(d.pop("key", UNSET))

        restapi_key = cls(
            descr=descr,
            username=username,
            hash_algo=hash_algo,
            length_bytes=length_bytes,
            hash_=hash_,
            key=key,
        )

        restapi_key.additional_properties = d
        return restapi_key

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
