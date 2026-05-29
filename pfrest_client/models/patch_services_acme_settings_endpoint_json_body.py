from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesACMESettingsEndpointJsonBody")


@_attrs_define
class PatchServicesACMESettingsEndpointJsonBody:
    """
    Attributes:
        enable (bool | Unset): Enables or disables the ACME renewal job.<br>
        writecerts (bool | Unset): Enables or disables the writing of certificates to /conf/acme/ in various formats for
            use by other scripts or daemons which do not integrate with the pfSense certificate manager.<br>
    """

    enable: bool | Unset = UNSET
    writecerts: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        writecerts = self.writecerts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if writecerts is not UNSET:
            field_dict["writecerts"] = writecerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        writecerts = d.pop("writecerts", UNSET)

        patch_services_acme_settings_endpoint_json_body = cls(
            enable=enable,
            writecerts=writecerts,
        )

        patch_services_acme_settings_endpoint_json_body.additional_properties = d
        return patch_services_acme_settings_endpoint_json_body

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
