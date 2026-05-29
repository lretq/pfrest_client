from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody")


@_attrs_define
class PatchServicesDNSForwarderHostOverrideAliasEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        host (str | Unset): The hostname of this override alias.<br>
        domain (str | Unset): The domain of this override alias.<br>
        description (str | Unset): The description of this override alias.<br>
    """

    parent_id: int
    id: int
    host: str | Unset = UNSET
    domain: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        host = self.host

        domain = self.domain

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if host is not UNSET:
            field_dict["host"] = host
        if domain is not UNSET:
            field_dict["domain"] = domain
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        host = d.pop("host", UNSET)

        domain = d.pop("domain", UNSET)

        description = d.pop("description", UNSET)

        patch_services_dns_forwarder_host_override_alias_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            host=host,
            domain=domain,
            description=description,
        )

        patch_services_dns_forwarder_host_override_alias_endpoint_data_body.additional_properties = d
        return patch_services_dns_forwarder_host_override_alias_endpoint_data_body

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
