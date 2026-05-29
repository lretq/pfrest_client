from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HAProxyFrontendHaCertificatesItem")


@_attrs_define
class HAProxyFrontendHaCertificatesItem:
    """
    Attributes:
        ssl_certificate (None | str | Unset): The SSL/TLS certificate refid to add to this frontend.<br>
    """

    ssl_certificate: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssl_certificate: None | str | Unset
        if isinstance(self.ssl_certificate, Unset):
            ssl_certificate = UNSET
        else:
            ssl_certificate = self.ssl_certificate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssl_certificate is not UNSET:
            field_dict["ssl_certificate"] = ssl_certificate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ssl_certificate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssl_certificate = _parse_ssl_certificate(d.pop("ssl_certificate", UNSET))

        ha_proxy_frontend_ha_certificates_item = cls(
            ssl_certificate=ssl_certificate,
        )

        ha_proxy_frontend_ha_certificates_item.additional_properties = d
        return ha_proxy_frontend_ha_certificates_item

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
