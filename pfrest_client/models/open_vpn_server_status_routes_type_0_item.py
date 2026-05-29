from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNServerStatusRoutesType0Item")


@_attrs_define
class OpenVPNServerStatusRoutesType0Item:
    """
    Attributes:
        common_name (None | str | Unset): The common name of the OpenVPN server connection.<br>
        remote_host (None | str | Unset): The remote host of the OpenVPN server connection.<br>
        virtual_addr (None | str | Unset): The virtual address of the OpenVPN server connection.<br>
        last_time (None | str | Unset): The last time of the route was used.<br>
    """

    common_name: None | str | Unset = UNSET
    remote_host: None | str | Unset = UNSET
    virtual_addr: None | str | Unset = UNSET
    last_time: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        common_name: None | str | Unset
        if isinstance(self.common_name, Unset):
            common_name = UNSET
        else:
            common_name = self.common_name

        remote_host: None | str | Unset
        if isinstance(self.remote_host, Unset):
            remote_host = UNSET
        else:
            remote_host = self.remote_host

        virtual_addr: None | str | Unset
        if isinstance(self.virtual_addr, Unset):
            virtual_addr = UNSET
        else:
            virtual_addr = self.virtual_addr

        last_time: None | str | Unset
        if isinstance(self.last_time, Unset):
            last_time = UNSET
        else:
            last_time = self.last_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if common_name is not UNSET:
            field_dict["common_name"] = common_name
        if remote_host is not UNSET:
            field_dict["remote_host"] = remote_host
        if virtual_addr is not UNSET:
            field_dict["virtual_addr"] = virtual_addr
        if last_time is not UNSET:
            field_dict["last_time"] = last_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_common_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        common_name = _parse_common_name(d.pop("common_name", UNSET))

        def _parse_remote_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_host = _parse_remote_host(d.pop("remote_host", UNSET))

        def _parse_virtual_addr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_addr = _parse_virtual_addr(d.pop("virtual_addr", UNSET))

        def _parse_last_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_time = _parse_last_time(d.pop("last_time", UNSET))

        open_vpn_server_status_routes_type_0_item = cls(
            common_name=common_name,
            remote_host=remote_host,
            virtual_addr=virtual_addr,
            last_time=last_time,
        )

        open_vpn_server_status_routes_type_0_item.additional_properties = d
        return open_vpn_server_status_routes_type_0_item

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
