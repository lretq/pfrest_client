from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesDNSResolverAccessListNetworkEndpointDataBody")


@_attrs_define
class PatchServicesDNSResolverAccessListNetworkEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        network (str | Unset): The network address of this access list entry.<br>
        mask (int | Unset): The subnet mask of this access list entry's network.<br>
        description (str | Unset): A description for this access list entry.<br>
    """

    parent_id: int
    id: int
    network: str | Unset = UNSET
    mask: int | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        network = self.network

        mask = self.mask

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if network is not UNSET:
            field_dict["network"] = network
        if mask is not UNSET:
            field_dict["mask"] = mask
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        network = d.pop("network", UNSET)

        mask = d.pop("mask", UNSET)

        description = d.pop("description", UNSET)

        patch_services_dns_resolver_access_list_network_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            network=network,
            mask=mask,
            description=description,
        )

        patch_services_dns_resolver_access_list_network_endpoint_data_body.additional_properties = d
        return patch_services_dns_resolver_access_list_network_endpoint_data_body

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
