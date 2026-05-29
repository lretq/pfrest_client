from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_file_type import HAProxyFileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesHAProxyFileEndpointDataBody")


@_attrs_define
class PatchServicesHAProxyFileEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        name (str | Unset): The unique name for this file.<br>
        type_ (HAProxyFileType | Unset): The type of file. Use `null` to assume an Errorfile.<br>
        content (str | Unset): The content of this file.<br>
    """

    id: int
    name: str | Unset = UNSET
    type_: HAProxyFileType | Unset = UNSET
    content: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: HAProxyFileType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = HAProxyFileType(_type_)

        content = d.pop("content", UNSET)

        patch_services_ha_proxy_file_endpoint_data_body = cls(
            id=id,
            name=name,
            type_=type_,
            content=content,
        )

        patch_services_ha_proxy_file_endpoint_data_body.additional_properties = d
        return patch_services_ha_proxy_file_endpoint_data_body

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
