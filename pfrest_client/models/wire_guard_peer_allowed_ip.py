from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WireGuardPeerAllowedIP")


@_attrs_define
class WireGuardPeerAllowedIP:
    """
    Attributes:
        address (str | Unset): The IPv4 or IPv6 address for this peer IP.<br>
        mask (int | Unset): The subnet mask for this peer IP.<br>
        descr (str | Unset): A description for this allowed peer IP.<br>
    """

    address: str | Unset = UNSET
    mask: int | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        mask = self.mask

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        address = d.pop("address", UNSET)

        mask = d.pop("mask", UNSET)

        descr = d.pop("descr", UNSET)

        wire_guard_peer_allowed_ip = cls(
            address=address,
            mask=mask,
            descr=descr,
        )

        wire_guard_peer_allowed_ip.additional_properties = d
        return wire_guard_peer_allowed_ip

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
