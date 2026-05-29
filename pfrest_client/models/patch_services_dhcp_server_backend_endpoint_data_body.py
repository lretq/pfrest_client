from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dhcp_server_backend_dhcpbackend import DHCPServerBackendDhcpbackend
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesDHCPServerBackendEndpointDataBody")


@_attrs_define
class PatchServicesDHCPServerBackendEndpointDataBody:
    """
    Attributes:
        dhcpbackend (DHCPServerBackendDhcpbackend | Unset): The backend DHCP server service to use. ISC DHCP is
            deprecate and will be removed in a future version of pfSense.<br> Default: DHCPServerBackendDhcpbackend.ISC.
    """

    dhcpbackend: DHCPServerBackendDhcpbackend | Unset = DHCPServerBackendDhcpbackend.ISC
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dhcpbackend: str | Unset = UNSET
        if not isinstance(self.dhcpbackend, Unset):
            dhcpbackend = self.dhcpbackend.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dhcpbackend is not UNSET:
            field_dict["dhcpbackend"] = dhcpbackend

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _dhcpbackend = d.pop("dhcpbackend", UNSET)
        dhcpbackend: DHCPServerBackendDhcpbackend | Unset
        if isinstance(_dhcpbackend, Unset):
            dhcpbackend = UNSET
        else:
            dhcpbackend = DHCPServerBackendDhcpbackend(_dhcpbackend)

        patch_services_dhcp_server_backend_endpoint_data_body = cls(
            dhcpbackend=dhcpbackend,
        )

        patch_services_dhcp_server_backend_endpoint_data_body.additional_properties = d
        return patch_services_dhcp_server_backend_endpoint_data_body

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
