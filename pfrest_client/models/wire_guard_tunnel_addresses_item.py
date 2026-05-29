from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireGuardTunnelAddressesItem")


@_attrs_define
class WireGuardTunnelAddressesItem:
    """
    Attributes:
        address (str): The IPv4 or IPv6 address for this WireGuard tunnel.<br>
        mask (int): The subnet mask for this WireGuard tunnel.<br>
        descr (str | Unset): A description for this WireGuard tunnel address entry.<br>
    """

    address: str
    mask: int
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        mask = self.mask

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "mask": mask,
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

        descr = d.pop("descr", UNSET)

        wire_guard_tunnel_addresses_item = cls(
            address=address,
            mask=mask,
            descr=descr,
        )

        wire_guard_tunnel_addresses_item.additional_properties = d
        return wire_guard_tunnel_addresses_item

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
