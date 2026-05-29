from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesDHCPRelayEndpointDataBody")


@_attrs_define
class PatchServicesDHCPRelayEndpointDataBody:
    """
    Attributes:
        server (list[str]): The IPv4 addresses of the DHCP server to relay requests to.<br>
        enable (bool | Unset): Enables or disables the DHCP relay.<br>
        interface (list[str] | Unset): The downstream interfaces to listen on for DHCP requests.<br>
        agentoption (bool | Unset): Enables or disables appending the circuit ID (interface number) and the agent ID to
            the DHCP request.<br>
        carpstatusvip (str | Unset): DHCP Relay will be stopped when the chosen VIP is in BACKUP status, and started in
            MASTER status.<br> Default: 'none'.
    """

    server: list[str]
    enable: bool | Unset = UNSET
    interface: list[str] | Unset = UNSET
    agentoption: bool | Unset = UNSET
    carpstatusvip: str | Unset = "none"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server = self.server

        enable = self.enable

        interface: list[str] | Unset = UNSET
        if not isinstance(self.interface, Unset):
            interface = self.interface

        agentoption = self.agentoption

        carpstatusvip = self.carpstatusvip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server": server,
            }
        )
        if enable is not UNSET:
            field_dict["enable"] = enable
        if interface is not UNSET:
            field_dict["interface"] = interface
        if agentoption is not UNSET:
            field_dict["agentoption"] = agentoption
        if carpstatusvip is not UNSET:
            field_dict["carpstatusvip"] = carpstatusvip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = cast(list[str], d.pop("server"))

        enable = d.pop("enable", UNSET)

        interface = cast(list[str], d.pop("interface", UNSET))

        agentoption = d.pop("agentoption", UNSET)

        carpstatusvip = d.pop("carpstatusvip", UNSET)

        patch_services_dhcp_relay_endpoint_data_body = cls(
            server=server,
            enable=enable,
            interface=interface,
            agentoption=agentoption,
            carpstatusvip=carpstatusvip,
        )

        patch_services_dhcp_relay_endpoint_data_body.additional_properties = d
        return patch_services_dhcp_relay_endpoint_data_body

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
