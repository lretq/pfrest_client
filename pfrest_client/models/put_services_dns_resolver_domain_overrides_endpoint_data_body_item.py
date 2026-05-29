from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PutServicesDNSResolverDomainOverridesEndpointDataBodyItem")


@_attrs_define
class PutServicesDNSResolverDomainOverridesEndpointDataBodyItem:
    """
    Attributes:
        domain (str): The domain to override.<br>
        ip (str): The IP address to which the domain should resolve.<br>
        descr (str | Unset): The description for this domain override.<br>
        forward_tls_upstream (bool | Unset): Enables or disables forwarding DNS queries to the upstream DNS server using
            TLS.<br>
        tls_hostname (str | Unset): The hostname to use for the TLS connection to the upstream DNS server.<br><br>This
            field is only available when the following conditions are met:<br>- `forward_tls_upstream` must be equal to
            `true`<br>
    """

    domain: str
    ip: str
    descr: str | Unset = UNSET
    forward_tls_upstream: bool | Unset = UNSET
    tls_hostname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        ip = self.ip

        descr = self.descr

        forward_tls_upstream = self.forward_tls_upstream

        tls_hostname = self.tls_hostname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "ip": ip,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if forward_tls_upstream is not UNSET:
            field_dict["forward_tls_upstream"] = forward_tls_upstream
        if tls_hostname is not UNSET:
            field_dict["tls_hostname"] = tls_hostname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        ip = d.pop("ip")

        descr = d.pop("descr", UNSET)

        forward_tls_upstream = d.pop("forward_tls_upstream", UNSET)

        tls_hostname = d.pop("tls_hostname", UNSET)

        put_services_dns_resolver_domain_overrides_endpoint_data_body_item = cls(
            domain=domain,
            ip=ip,
            descr=descr,
            forward_tls_upstream=forward_tls_upstream,
            tls_hostname=tls_hostname,
        )

        put_services_dns_resolver_domain_overrides_endpoint_data_body_item.additional_properties = d
        return put_services_dns_resolver_domain_overrides_endpoint_data_body_item

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
