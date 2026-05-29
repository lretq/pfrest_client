from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CARP")


@_attrs_define
class CARP:
    """
    Attributes:
        enable (bool | Unset): Enables or disables CARP on this system.<br>
        maintenance_mode (bool | Unset): Enables or disables CARP maintenance mode on this system.<br>
    """

    enable: bool | Unset = UNSET
    maintenance_mode: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        maintenance_mode = self.maintenance_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if maintenance_mode is not UNSET:
            field_dict["maintenance_mode"] = maintenance_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        maintenance_mode = d.pop("maintenance_mode", UNSET)

        carp = cls(
            enable=enable,
            maintenance_mode=maintenance_mode,
        )

        carp.additional_properties = d
        return carp

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
