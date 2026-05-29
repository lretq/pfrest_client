from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dhcp_server_custom_option_type import DHCPServerCustomOptionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DHCPServerCustomOption")


@_attrs_define
class DHCPServerCustomOption:
    """
    Attributes:
        number (int | Unset): The DHCP option number to configure.<br>
        type_ (DHCPServerCustomOptionType | Unset): The type of value to configure for the option.<br>
        value (str | Unset): The value to configure for the option.<br>
    """

    number: int | Unset = UNSET
    type_: DHCPServerCustomOptionType | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DHCPServerCustomOptionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DHCPServerCustomOptionType(_type_)

        value = d.pop("value", UNSET)

        dhcp_server_custom_option = cls(
            number=number,
            type_=type_,
            value=value,
        )

        dhcp_server_custom_option.additional_properties = d
        return dhcp_server_custom_option

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
