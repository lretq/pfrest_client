from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesACMEAccountKeyRegisterEndpointDataBody")


@_attrs_define
class PostServicesACMEAccountKeyRegisterEndpointDataBody:
    """
    Attributes:
        name (str): The name of the ACME account key to register.<br>
        status (None | str | Unset): The registration status of the ACME account key. This will show 'pending' if the
            registration process is still running, 'registered' if the registration was successful, 'failed' if the
            registration failed, and 'unknown' if the registration status is not known. Note: This status can only be
            determined for registrations initiated through the REST API.<br> Default: 'unknown'.
    """

    name: str
    status: None | str | Unset = "unknown"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        post_services_acme_account_key_register_endpoint_data_body = cls(
            name=name,
            status=status,
        )

        post_services_acme_account_key_register_endpoint_data_body.additional_properties = d
        return post_services_acme_account_key_register_endpoint_data_body

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
