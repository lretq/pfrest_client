from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dhcp_server_custom_option_type import DHCPServerCustomOptionType

T = TypeVar("T", bound="PostServicesDHCPServerCustomOptionEndpointDataBody")


@_attrs_define
class PostServicesDHCPServerCustomOptionEndpointDataBody:
    """
    Attributes:
        number (int): The DHCP option number to configure.<br>
        type_ (DHCPServerCustomOptionType): The type of value to configure for the option.<br>
        value (str): The value to configure for the option.<br>
        parent_id (int): The ID of the parent this object is nested under.
    """

    number: int
    type_: DHCPServerCustomOptionType
    value: str
    parent_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        type_ = self.type_.value

        value = self.value

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "type": type_,
                "value": value,
                "parent_id": parent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number = d.pop("number")

        type_ = DHCPServerCustomOptionType(d.pop("type"))

        value = d.pop("value")

        parent_id = d.pop("parent_id")

        post_services_dhcp_server_custom_option_endpoint_data_body = cls(
            number=number,
            type_=type_,
            value=value,
            parent_id=parent_id,
        )

        post_services_dhcp_server_custom_option_endpoint_data_body.additional_properties = d
        return post_services_dhcp_server_custom_option_endpoint_data_body

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
