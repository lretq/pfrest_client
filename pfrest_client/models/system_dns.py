from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_dns_dnslocalhost import SystemDNSDnslocalhost
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemDNS")


@_attrs_define
class SystemDNS:
    """
    Attributes:
        dnsallowoverride (bool | Unset): Allow DNS servers to be overwritten by DHCP on WAN interfaces.<br>
        dnslocalhost (SystemDNSDnslocalhost | Unset): Use local DNS server (DNS Resover or DNS Forwarder) as the primary
            DNS, or use only remote DNS servers specified in `dnsserver`. Set to `null` to use local DNS server as the
            primary and remote DNS servers as backup.<br>
        dnsserver (list[str] | Unset): The remote DNS server IPv4 or IPv6 addresses.<br>
    """

    dnsallowoverride: bool | Unset = UNSET
    dnslocalhost: SystemDNSDnslocalhost | Unset = UNSET
    dnsserver: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dnsallowoverride = self.dnsallowoverride

        dnslocalhost: str | Unset = UNSET
        if not isinstance(self.dnslocalhost, Unset):
            dnslocalhost = self.dnslocalhost.value

        dnsserver: list[str] | Unset = UNSET
        if not isinstance(self.dnsserver, Unset):
            dnsserver = self.dnsserver

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dnsallowoverride is not UNSET:
            field_dict["dnsallowoverride"] = dnsallowoverride
        if dnslocalhost is not UNSET:
            field_dict["dnslocalhost"] = dnslocalhost
        if dnsserver is not UNSET:
            field_dict["dnsserver"] = dnsserver

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dnsallowoverride = d.pop("dnsallowoverride", UNSET)

        _dnslocalhost = d.pop("dnslocalhost", UNSET)
        dnslocalhost: SystemDNSDnslocalhost | Unset
        if isinstance(_dnslocalhost, Unset):
            dnslocalhost = UNSET
        else:
            dnslocalhost = SystemDNSDnslocalhost(_dnslocalhost)

        dnsserver = cast(list[str], d.pop("dnsserver", UNSET))

        system_dns = cls(
            dnsallowoverride=dnsallowoverride,
            dnslocalhost=dnslocalhost,
            dnsserver=dnsserver,
        )

        system_dns.additional_properties = d
        return system_dns

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
