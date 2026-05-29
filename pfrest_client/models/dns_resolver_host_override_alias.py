from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DNSResolverHostOverrideAlias")


@_attrs_define
class DNSResolverHostOverrideAlias:
    """
    Attributes:
        host (str | Unset): The hostname portion of the host override alias.<br>
        domain (str | Unset): The hostname portion of the host override alias.<br>
        descr (str | Unset): A detailed description for this host override alias.<br>
    """

    host: str | Unset = UNSET
    domain: str | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        domain = self.domain

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if domain is not UNSET:
            field_dict["domain"] = domain
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host", UNSET)

        domain = d.pop("domain", UNSET)

        descr = d.pop("descr", UNSET)

        dns_resolver_host_override_alias = cls(
            host=host,
            domain=domain,
            descr=descr,
        )

        dns_resolver_host_override_alias.additional_properties = d
        return dns_resolver_host_override_alias

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
