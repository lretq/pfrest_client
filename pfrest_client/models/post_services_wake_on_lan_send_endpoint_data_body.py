from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostServicesWakeOnLANSendEndpointDataBody")


@_attrs_define
class PostServicesWakeOnLANSendEndpointDataBody:
    """
    Attributes:
        interface (str): The interface the host to be woken up is connected to.<br>
        mac_addr (str): The MAC address of the host to be awoken.<br>
    """

    interface: str
    mac_addr: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        mac_addr = self.mac_addr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interface": interface,
                "mac_addr": mac_addr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interface = d.pop("interface")

        mac_addr = d.pop("mac_addr")

        post_services_wake_on_lan_send_endpoint_data_body = cls(
            interface=interface,
            mac_addr=mac_addr,
        )

        post_services_wake_on_lan_send_endpoint_data_body.additional_properties = d
        return post_services_wake_on_lan_send_endpoint_data_body

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
