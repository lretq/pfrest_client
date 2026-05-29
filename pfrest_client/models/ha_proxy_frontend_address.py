from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_frontend_address_extaddr import HAProxyFrontendAddressExtaddr
from ..types import UNSET, Unset

T = TypeVar("T", bound="HAProxyFrontendAddress")


@_attrs_define
class HAProxyFrontendAddress:
    """
    Attributes:
        extaddr (HAProxyFrontendAddressExtaddr | Unset): The external address to use.<br>
        extaddr_custom (str | Unset): The custom IPv4 or IPv6 address to use as the external address.<br><br>This field
            is only available when the following conditions are met:<br>- `extaddr` must be equal to `'custom'`<br>
        extaddr_port (None | str | Unset): The port to bind to for this address. Valid options are: a TCP/UDP port
            number<br>
        extaddr_ssl (bool | Unset): Enables or disables using SSL/TLS for this address.<br>
        exaddr_advanced (str | Unset): The advanced configuration to apply to this address.<br>
    """

    extaddr: HAProxyFrontendAddressExtaddr | Unset = UNSET
    extaddr_custom: str | Unset = UNSET
    extaddr_port: None | str | Unset = UNSET
    extaddr_ssl: bool | Unset = UNSET
    exaddr_advanced: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extaddr: str | Unset = UNSET
        if not isinstance(self.extaddr, Unset):
            extaddr = self.extaddr.value

        extaddr_custom = self.extaddr_custom

        extaddr_port: None | str | Unset
        if isinstance(self.extaddr_port, Unset):
            extaddr_port = UNSET
        else:
            extaddr_port = self.extaddr_port

        extaddr_ssl = self.extaddr_ssl

        exaddr_advanced = self.exaddr_advanced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extaddr is not UNSET:
            field_dict["extaddr"] = extaddr
        if extaddr_custom is not UNSET:
            field_dict["extaddr_custom"] = extaddr_custom
        if extaddr_port is not UNSET:
            field_dict["extaddr_port"] = extaddr_port
        if extaddr_ssl is not UNSET:
            field_dict["extaddr_ssl"] = extaddr_ssl
        if exaddr_advanced is not UNSET:
            field_dict["exaddr_advanced"] = exaddr_advanced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _extaddr = d.pop("extaddr", UNSET)
        extaddr: HAProxyFrontendAddressExtaddr | Unset
        if isinstance(_extaddr, Unset):
            extaddr = UNSET
        else:
            extaddr = HAProxyFrontendAddressExtaddr(_extaddr)

        extaddr_custom = d.pop("extaddr_custom", UNSET)

        def _parse_extaddr_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extaddr_port = _parse_extaddr_port(d.pop("extaddr_port", UNSET))

        extaddr_ssl = d.pop("extaddr_ssl", UNSET)

        exaddr_advanced = d.pop("exaddr_advanced", UNSET)

        ha_proxy_frontend_address = cls(
            extaddr=extaddr,
            extaddr_custom=extaddr_custom,
            extaddr_port=extaddr_port,
            extaddr_ssl=extaddr_ssl,
            exaddr_advanced=exaddr_advanced,
        )

        ha_proxy_frontend_address.additional_properties = d
        return ha_proxy_frontend_address

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
