from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WakeOnLANSend")


@_attrs_define
class WakeOnLANSend:
    """
    Attributes:
        interface (str | Unset): The interface the host to be woken up is connected to.<br>
        mac_addr (str | Unset): The MAC address of the host to be awoken.<br>
    """

    interface: str | Unset = UNSET
    mac_addr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        mac_addr = self.mac_addr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface
        if mac_addr is not UNSET:
            field_dict["mac_addr"] = mac_addr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interface = d.pop("interface", UNSET)

        mac_addr = d.pop("mac_addr", UNSET)

        wake_on_lan_send = cls(
            interface=interface,
            mac_addr=mac_addr,
        )

        wake_on_lan_send.additional_properties = d
        return wake_on_lan_send

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
