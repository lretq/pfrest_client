from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dhcp_server_custom_option_type import DHCPServerCustomOptionType

T = TypeVar("T", bound="DHCPServerNumberoptionsItem")


@_attrs_define
class DHCPServerNumberoptionsItem:
    """
    Attributes:
        number (int): The DHCP option number to configure.<br>
        type_ (DHCPServerCustomOptionType): The type of value to configure for the option.<br>
        value (str): The value to configure for the option.<br>
    """

    number: int
    type_: DHCPServerCustomOptionType
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")

        type_ = DHCPServerCustomOptionType(d.pop("type"))

        value = d.pop("value")

        dhcp_server_numberoptions_item = cls(
            number=number,
            type_=type_,
            value=value,
        )

        dhcp_server_numberoptions_item.additional_properties = d
        return dhcp_server_numberoptions_item

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
