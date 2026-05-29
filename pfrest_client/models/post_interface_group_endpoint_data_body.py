from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostInterfaceGroupEndpointDataBody")


@_attrs_define
class PostInterfaceGroupEndpointDataBody:
    """
    Attributes:
        ifname (str): The name of this interface group.<br>
        members (list[str] | Unset): The member interfaces to assign to this interface group.<br>
        descr (str | Unset): The description for this interface group.<br>
    """

    ifname: str
    members: list[str] | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ifname = self.ifname

        members: list[str] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ifname": ifname,
            }
        )
        if members is not UNSET:
            field_dict["members"] = members
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ifname = d.pop("ifname")

        members = cast(list[str], d.pop("members", UNSET))

        descr = d.pop("descr", UNSET)

        post_interface_group_endpoint_data_body = cls(
            ifname=ifname,
            members=members,
            descr=descr,
        )

        post_interface_group_endpoint_data_body.additional_properties = d
        return post_interface_group_endpoint_data_body

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
