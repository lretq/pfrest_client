from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_file_type import HAProxyFileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutServicesHAProxyFilesJsonBodyItem")


@_attrs_define
class PutServicesHAProxyFilesJsonBodyItem:
    """
    Attributes:
        name (str): The unique name for this file.<br>
        content (str): The content of this file.<br>
        type_ (HAProxyFileType | Unset): The type of file. Use `null` to assume an Errorfile.<br>
    """

    name: str
    content: str
    type_: HAProxyFileType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        content = self.content

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "content": content,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        content = d.pop("content")

        _type_ = d.pop("type", UNSET)
        type_: HAProxyFileType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = HAProxyFileType(_type_)

        put_services_ha_proxy_files_json_body_item = cls(
            name=name,
            content=content,
            type_=type_,
        )

        put_services_ha_proxy_files_json_body_item.additional_properties = d
        return put_services_ha_proxy_files_json_body_item

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
