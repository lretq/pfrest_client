from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.free_radius_interface_ip_version import FreeRADIUSInterfaceIpVersion
from ..models.free_radius_interface_type import FreeRADIUSInterfaceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesFreeRADIUSInterfaceEndpointDataBody")


@_attrs_define
class PatchServicesFreeRADIUSInterfaceEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        addr (str | Unset): The IP address of the listening interface. If you choose * then it means all interfaces.<br>
        port (str | Unset): The port number of the listening interface. Different interface types need different ports.
            Valid options are: a TCP/UDP port number<br> Default: '1812'.
        type_ (FreeRADIUSInterfaceType | Unset): The type of the listening interface: Authentication/Accounting.<br>
            Default: FreeRADIUSInterfaceType.AUTH.
        ip_version (FreeRADIUSInterfaceIpVersion | Unset): The IP version of the listening interface.<br>
        description (str | Unset): The description for this interface.<br>
    """

    id: int
    addr: str | Unset = UNSET
    port: str | Unset = "1812"
    type_: FreeRADIUSInterfaceType | Unset = FreeRADIUSInterfaceType.AUTH
    ip_version: FreeRADIUSInterfaceIpVersion | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        addr = self.addr

        port = self.port

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        ip_version: str | Unset = UNSET
        if not isinstance(self.ip_version, Unset):
            ip_version = self.ip_version.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if addr is not UNSET:
            field_dict["addr"] = addr
        if port is not UNSET:
            field_dict["port"] = port
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ip_version is not UNSET:
            field_dict["ip_version"] = ip_version
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        addr = d.pop("addr", UNSET)

        port = d.pop("port", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FreeRADIUSInterfaceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FreeRADIUSInterfaceType(_type_)

        _ip_version = d.pop("ip_version", UNSET)
        ip_version: FreeRADIUSInterfaceIpVersion | Unset
        if isinstance(_ip_version, Unset):
            ip_version = UNSET
        else:
            ip_version = FreeRADIUSInterfaceIpVersion(_ip_version)

        description = d.pop("description", UNSET)

        patch_services_free_radius_interface_endpoint_data_body = cls(
            id=id,
            addr=addr,
            port=port,
            type_=type_,
            ip_version=ip_version,
            description=description,
        )

        patch_services_free_radius_interface_endpoint_data_body.additional_properties = d
        return patch_services_free_radius_interface_endpoint_data_body

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
