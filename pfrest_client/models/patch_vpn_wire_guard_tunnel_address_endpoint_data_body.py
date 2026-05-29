from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchVPNWireGuardTunnelAddressEndpointDataBody")


@_attrs_define
class PatchVPNWireGuardTunnelAddressEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        address (str | Unset): The IPv4 or IPv6 address for this WireGuard tunnel.<br>
        mask (int | Unset): The subnet mask for this WireGuard tunnel.<br>
        descr (str | Unset): A description for this WireGuard tunnel address entry.<br>
    """

    parent_id: int
    id: int
    address: str | Unset = UNSET
    mask: int | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        address = self.address

        mask = self.mask

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if mask is not UNSET:
            field_dict["mask"] = mask
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        address = d.pop("address", UNSET)

        mask = d.pop("mask", UNSET)

        descr = d.pop("descr", UNSET)

        patch_vpn_wire_guard_tunnel_address_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            address=address,
            mask=mask,
            descr=descr,
        )

        patch_vpn_wire_guard_tunnel_address_endpoint_data_body.additional_properties = d
        return patch_vpn_wire_guard_tunnel_address_endpoint_data_body

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
