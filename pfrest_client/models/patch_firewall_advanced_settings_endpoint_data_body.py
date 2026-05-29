from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchFirewallAdvancedSettingsEndpointDataBody")


@_attrs_define
class PatchFirewallAdvancedSettingsEndpointDataBody:
    """
    Attributes:
        aliasesresolveinterval (int | Unset): The interval (in seconds) at which to resolve hostnames in aliases.<br>
            Default: 9223372036854775807.
        checkaliasesurlcert (bool | Unset): Check the certificate of URLs used in aliases.<br> Default: True.
    """

    aliasesresolveinterval: int | Unset = 9223372036854775807
    checkaliasesurlcert: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aliasesresolveinterval = self.aliasesresolveinterval

        checkaliasesurlcert = self.checkaliasesurlcert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aliasesresolveinterval is not UNSET:
            field_dict["aliasesresolveinterval"] = aliasesresolveinterval
        if checkaliasesurlcert is not UNSET:
            field_dict["checkaliasesurlcert"] = checkaliasesurlcert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aliasesresolveinterval = d.pop("aliasesresolveinterval", UNSET)

        checkaliasesurlcert = d.pop("checkaliasesurlcert", UNSET)

        patch_firewall_advanced_settings_endpoint_data_body = cls(
            aliasesresolveinterval=aliasesresolveinterval,
            checkaliasesurlcert=checkaliasesurlcert,
        )

        patch_firewall_advanced_settings_endpoint_data_body.additional_properties = d
        return patch_firewall_advanced_settings_endpoint_data_body

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
