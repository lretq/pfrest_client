from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableInterface")


@_attrs_define
class AvailableInterface:
    """
    Attributes:
        if_ (None | str | Unset): The name of the interface.<br>
        mac (None | str | Unset): The MAC address of the interface.<br>
        dmesg (None | str | Unset): The description of the interface.<br>
        in_use_by (None | str | Unset): The pfSense interface ID that is using this interface.<br>
    """

    if_: None | str | Unset = UNSET
    mac: None | str | Unset = UNSET
    dmesg: None | str | Unset = UNSET
    in_use_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if_: None | str | Unset
        if isinstance(self.if_, Unset):
            if_ = UNSET
        else:
            if_ = self.if_

        mac: None | str | Unset
        if isinstance(self.mac, Unset):
            mac = UNSET
        else:
            mac = self.mac

        dmesg: None | str | Unset
        if isinstance(self.dmesg, Unset):
            dmesg = UNSET
        else:
            dmesg = self.dmesg

        in_use_by: None | str | Unset
        if isinstance(self.in_use_by, Unset):
            in_use_by = UNSET
        else:
            in_use_by = self.in_use_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if if_ is not UNSET:
            field_dict["if"] = if_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if dmesg is not UNSET:
            field_dict["dmesg"] = dmesg
        if in_use_by is not UNSET:
            field_dict["in_use_by"] = in_use_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_if_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        if_ = _parse_if_(d.pop("if", UNSET))

        def _parse_mac(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mac = _parse_mac(d.pop("mac", UNSET))

        def _parse_dmesg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dmesg = _parse_dmesg(d.pop("dmesg", UNSET))

        def _parse_in_use_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        in_use_by = _parse_in_use_by(d.pop("in_use_by", UNSET))

        available_interface = cls(
            if_=if_,
            mac=mac,
            dmesg=dmesg,
            in_use_by=in_use_by,
        )

        available_interface.additional_properties = d
        return available_interface

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
