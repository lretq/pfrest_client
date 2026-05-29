from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_forwarder_host_override_aliases_item import DNSForwarderHostOverrideAliasesItem


T = TypeVar("T", bound="PutServicesDNSForwarderHostOverridesEndpointDataBodyItem")


@_attrs_define
class PutServicesDNSForwarderHostOverridesEndpointDataBodyItem:
    """
    Attributes:
        host (str): The hostname of this override.<br>
        domain (str): The domain of this override.<br>
        ip (str): The IP address of this override.<br>
        descr (str | Unset): The description for this override.<br>
        aliases (list[DNSForwarderHostOverrideAliasesItem] | Unset): The aliases for this override.<br>
    """

    host: str
    domain: str
    ip: str
    descr: str | Unset = UNSET
    aliases: list[DNSForwarderHostOverrideAliasesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        domain = self.domain

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
                "host": host,
                "domain": domain,
                "ip": ip,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if aliases is not UNSET:
            field_dict["aliases"] = aliases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_forwarder_host_override_aliases_item import DNSForwarderHostOverrideAliasesItem

        d = dict(src_dict)
        host = d.pop("host")

        domain = d.pop("domain")

        ip = d.pop("ip")

        descr = d.pop("descr", UNSET)

        _aliases = d.pop("aliases", UNSET)
        aliases: list[DNSForwarderHostOverrideAliasesItem] | Unset = UNSET
        if _aliases is not UNSET:
            aliases = []
            for aliases_item_data in _aliases:
                aliases_item = DNSForwarderHostOverrideAliasesItem.from_dict(aliases_item_data)

                aliases.append(aliases_item)

        put_services_dns_forwarder_host_overrides_endpoint_data_body_item = cls(
            host=host,
            domain=domain,
            ip=ip,
            descr=descr,
            aliases=aliases,
        )

        put_services_dns_forwarder_host_overrides_endpoint_data_body_item.additional_properties = d
        return put_services_dns_forwarder_host_overrides_endpoint_data_body_item

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
