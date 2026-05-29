from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesHAProxySettingsDNSResolverEndpointDataBody")


@_attrs_define
class PatchServicesHAProxySettingsDNSResolverEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        name (str | Unset): The descriptive name for this DNS server.<br>
        server (str | Unset): The IP or hostname of the DNS server.<br>
        port (str | Unset): The port used by this DNS server. Valid options are: a TCP/UDP port number<br> Default:
            '53'.
    """

    id: int
    name: str | Unset = UNSET
    server: str | Unset = UNSET
    port: str | Unset = "53"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        server = self.server

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if server is not UNSET:
            field_dict["server"] = server
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        server = d.pop("server", UNSET)

        port = d.pop("port", UNSET)

        patch_services_ha_proxy_settings_dns_resolver_endpoint_data_body = cls(
            id=id,
            name=name,
            server=server,
            port=port,
        )

        patch_services_ha_proxy_settings_dns_resolver_endpoint_data_body.additional_properties = d
        return patch_services_ha_proxy_settings_dns_resolver_endpoint_data_body

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
