from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dhcp_server_custom_option_type import DHCPServerCustomOptionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesDHCPServerCustomOptionEndpointDataBody")


@_attrs_define
class PatchServicesDHCPServerCustomOptionEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        number (int | Unset): The DHCP option number to configure.<br>
        type_ (DHCPServerCustomOptionType | Unset): The type of value to configure for the option.<br>
        value (str | Unset): The value to configure for the option.<br>
    """

    parent_id: int
    id: int
    number: int | Unset = UNSET
    type_: DHCPServerCustomOptionType | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        number = self.number

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
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
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        number = d.pop("number", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DHCPServerCustomOptionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DHCPServerCustomOptionType(_type_)

        value = d.pop("value", UNSET)

        patch_services_dhcp_server_custom_option_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            number=number,
            type_=type_,
            value=value,
        )

        patch_services_dhcp_server_custom_option_endpoint_data_body.additional_properties = d
        return patch_services_dhcp_server_custom_option_endpoint_data_body

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
