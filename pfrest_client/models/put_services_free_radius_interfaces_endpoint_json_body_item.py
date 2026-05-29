from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.free_radius_interface_ip_version import FreeRADIUSInterfaceIpVersion
from ..models.free_radius_interface_type import FreeRADIUSInterfaceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem")


@_attrs_define
class PutServicesFreeRADIUSInterfacesEndpointJsonBodyItem:
    """
    Attributes:
        addr (str): The IP address of the listening interface. If you choose * then it means all interfaces.<br>
        ip_version (FreeRADIUSInterfaceIpVersion): The IP version of the listening interface.<br>
        port (str | Unset): The port number of the listening interface. Different interface types need different ports.
            Valid options are: a TCP/UDP port number<br> Default: '1812'.
        type_ (FreeRADIUSInterfaceType | Unset): The type of the listening interface: Authentication/Accounting.<br>
            Default: FreeRADIUSInterfaceType.AUTH.
        description (str | Unset): The description for this interface.<br>
    """

    addr: str
    ip_version: FreeRADIUSInterfaceIpVersion
    port: str | Unset = "1812"
    type_: FreeRADIUSInterfaceType | Unset = FreeRADIUSInterfaceType.AUTH
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr = self.addr

        ip_version = self.ip_version.value

        port = self.port

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addr": addr,
                "ip_version": ip_version,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        addr = d.pop("addr")

        ip_version = FreeRADIUSInterfaceIpVersion(d.pop("ip_version"))

        port = d.pop("port", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FreeRADIUSInterfaceType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FreeRADIUSInterfaceType(_type_)

        description = d.pop("description", UNSET)

        put_services_free_radius_interfaces_endpoint_json_body_item = cls(
            addr=addr,
            ip_version=ip_version,
            port=port,
            type_=type_,
            description=description,
        )

        put_services_free_radius_interfaces_endpoint_json_body_item.additional_properties = d
        return put_services_free_radius_interfaces_endpoint_json_body_item

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
