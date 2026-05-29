from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostVPNWireGuardTunnelAddressEndpointDataBody")


@_attrs_define
class PostVPNWireGuardTunnelAddressEndpointDataBody:
    """
    Attributes:
        address (str): The IPv4 or IPv6 address for this WireGuard tunnel.<br>
        mask (int): The subnet mask for this WireGuard tunnel.<br>
        parent_id (int): The ID of the parent this object is nested under.
        descr (str | Unset): A description for this WireGuard tunnel address entry.<br>
    """

    address: str
    mask: int
    parent_id: int
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        mask = self.mask

        parent_id = self.parent_id

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "mask": mask,
                "parent_id": parent_id,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address")

        mask = d.pop("mask")

        parent_id = d.pop("parent_id")

        descr = d.pop("descr", UNSET)

        post_vpn_wire_guard_tunnel_address_endpoint_data_body = cls(
            address=address,
            mask=mask,
            parent_id=parent_id,
            descr=descr,
        )

        post_vpn_wire_guard_tunnel_address_endpoint_data_body.additional_properties = d
        return post_vpn_wire_guard_tunnel_address_endpoint_data_body

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
