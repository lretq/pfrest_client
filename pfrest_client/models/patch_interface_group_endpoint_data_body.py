from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchInterfaceGroupEndpointDataBody")


@_attrs_define
class PatchInterfaceGroupEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        ifname (str | Unset): The name of this interface group.<br>
        members (list[str] | Unset): The member interfaces to assign to this interface group.<br>
        descr (str | Unset): The description for this interface group.<br>
    """

    id: int
    ifname: str | Unset = UNSET
    members: list[str] | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ifname = self.ifname

        members: list[str] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if ifname is not UNSET:
            field_dict["ifname"] = ifname
        if members is not UNSET:
            field_dict["members"] = members
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ifname = d.pop("ifname", UNSET)

        members = cast(list[str], d.pop("members", UNSET))

        descr = d.pop("descr", UNSET)

        patch_interface_group_endpoint_data_body = cls(
            id=id,
            ifname=ifname,
            members=members,
            descr=descr,
        )

        patch_interface_group_endpoint_data_body.additional_properties = d
        return patch_interface_group_endpoint_data_body

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
