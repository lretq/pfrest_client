from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesHAProxySettingsDNSResolverEndpointJsonBody")


@_attrs_define
class PostServicesHAProxySettingsDNSResolverEndpointJsonBody:
    """
    Attributes:
        name (str): The descriptive name for this DNS server.<br>
        server (str): The IP or hostname of the DNS server.<br>
        port (str | Unset): The port used by this DNS server. Valid options are: a TCP/UDP port number<br> Default:
            '53'.
    """

    name: str
    server: str
    port: str | Unset = "53"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        server = self.server

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "server": server,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        server = d.pop("server")

        port = d.pop("port", UNSET)

        post_services_ha_proxy_settings_dns_resolver_endpoint_json_body = cls(
            name=name,
            server=server,
            port=port,
        )

        post_services_ha_proxy_settings_dns_resolver_endpoint_json_body.additional_properties = d
        return post_services_ha_proxy_settings_dns_resolver_endpoint_json_body

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
