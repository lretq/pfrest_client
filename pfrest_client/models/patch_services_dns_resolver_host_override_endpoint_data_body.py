from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_resolver_host_override_aliases_item import DNSResolverHostOverrideAliasesItem


T = TypeVar("T", bound="PatchServicesDNSResolverHostOverrideEndpointDataBody")


@_attrs_define
class PatchServicesDNSResolverHostOverrideEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        host (str | Unset): The hostname portion of the host override.<br>
        domain (str | Unset): The hostname portion of the host override.<br>
        ip (list[str] | Unset): The IP addresses this host override will resolve.<br>
        descr (str | Unset): A detailed description for this host override.<br>
        aliases (list[DNSResolverHostOverrideAliasesItem] | Unset): Additional alias hostnames that should resolve the
            same IP(s).<br>
    """

    id: int
    host: str | Unset = UNSET
    domain: str | Unset = UNSET
    ip: list[str] | Unset = UNSET
    descr: str | Unset = UNSET
    aliases: list[DNSResolverHostOverrideAliasesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        host = self.host

        domain = self.domain

        ip: list[str] | Unset = UNSET
        if not isinstance(self.ip, Unset):
            ip = self.ip

        descr = self.descr

        aliases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()
                aliases.append(aliases_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if host is not UNSET:
            field_dict["host"] = host
        if domain is not UNSET:
            field_dict["domain"] = domain
        if ip is not UNSET:
            field_dict["ip"] = ip
        if descr is not UNSET:
            field_dict["descr"] = descr
        if aliases is not UNSET:
            field_dict["aliases"] = aliases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_resolver_host_override_aliases_item import DNSResolverHostOverrideAliasesItem

        d = dict(src_dict)
        id = d.pop("id")

        host = d.pop("host", UNSET)

        domain = d.pop("domain", UNSET)

        ip = cast(list[str], d.pop("ip", UNSET))

        descr = d.pop("descr", UNSET)

        _aliases = d.pop("aliases", UNSET)
        aliases: list[DNSResolverHostOverrideAliasesItem] | Unset = UNSET
        if _aliases is not UNSET:
            aliases = []
            for aliases_item_data in _aliases:
                aliases_item = DNSResolverHostOverrideAliasesItem.from_dict(aliases_item_data)

                aliases.append(aliases_item)

        patch_services_dns_resolver_host_override_endpoint_data_body = cls(
            id=id,
            host=host,
            domain=domain,
            ip=ip,
            descr=descr,
            aliases=aliases,
        )

        patch_services_dns_resolver_host_override_endpoint_data_body.additional_properties = d
        return patch_services_dns_resolver_host_override_endpoint_data_body

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
