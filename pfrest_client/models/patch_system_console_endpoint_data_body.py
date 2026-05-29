from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchSystemConsoleEndpointDataBody")


@_attrs_define
class PatchSystemConsoleEndpointDataBody:
    """
    Attributes:
        passwd_protect_console (bool | Unset): Enables or disables password protecting the console.<br>
    """

    passwd_protect_console: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        passwd_protect_console = self.passwd_protect_console

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if passwd_protect_console is not UNSET:
            field_dict["passwd_protect_console"] = passwd_protect_console

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        passwd_protect_console = d.pop("passwd_protect_console", UNSET)

        patch_system_console_endpoint_data_body = cls(
            passwd_protect_console=passwd_protect_console,
        )

        patch_system_console_endpoint_data_body.additional_properties = d
        return patch_system_console_endpoint_data_body

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
