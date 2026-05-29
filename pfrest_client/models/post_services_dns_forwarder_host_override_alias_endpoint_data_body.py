from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesDNSForwarderHostOverrideAliasEndpointDataBody")


@_attrs_define
class PostServicesDNSForwarderHostOverrideAliasEndpointDataBody:
    """
    Attributes:
        host (str): The hostname of this override alias.<br>
        domain (str): The domain of this override alias.<br>
        parent_id (int): The ID of the parent this object is nested under.
        description (str | Unset): The description of this override alias.<br>
    """

    host: str
    domain: str
    parent_id: int
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        domain = self.domain

        parent_id = self.parent_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
                "domain": domain,
                "parent_id": parent_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        domain = d.pop("domain")

        parent_id = d.pop("parent_id")

        description = d.pop("description", UNSET)

        post_services_dns_forwarder_host_override_alias_endpoint_data_body = cls(
            host=host,
            domain=domain,
            parent_id=parent_id,
            description=description,
        )

        post_services_dns_forwarder_host_override_alias_endpoint_data_body.additional_properties = d
        return post_services_dns_forwarder_host_override_alias_endpoint_data_body

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
