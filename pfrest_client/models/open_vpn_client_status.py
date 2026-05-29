from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNClientStatus")


@_attrs_define
class OpenVPNClientStatus:
    """
    Attributes:
        name (None | str | Unset): The name of the OpenVPN client.<br>
        port (None | str | Unset): The port number of the OpenVPN client. Valid options are: a TCP/UDP port number<br>
        vpnid (int | None | Unset): The VPN ID of the OpenVPN client this status corresponds to.<br>
        mgmt (None | str | Unset): The management interface of the OpenVPN client.<br>
        status (None | str | Unset): The current status of the OpenVPN client.<br>
        state (None | str | Unset): The current state of the OpenVPN client.<br>
        state_detail (None | str | Unset): The details for the current state of the OpenVPN client.<br>
        connect_time (None | str | Unset): The connection time of the OpenVPN client.<br>
        virtual_addr (None | str | Unset): The virtual address of the OpenVPN client.<br>
        virtual_addr6 (None | str | Unset): The virtual address 6 of the OpenVPN client.<br>
        remote_host (None | str | Unset): The remote host of the OpenVPN client.<br>
        remote_port (None | str | Unset): The remote port of the OpenVPN client. Valid options are: a TCP/UDP port
            number<br>
        local_host (None | str | Unset): The local host of the OpenVPN client.<br>
        local_port (None | str | Unset): The local port of the OpenVPN client. Valid options are: a TCP/UDP port
            number<br>
    """

    name: None | str | Unset = UNSET
    port: None | str | Unset = UNSET
    vpnid: int | None | Unset = UNSET
    mgmt: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    state_detail: None | str | Unset = UNSET
    connect_time: None | str | Unset = UNSET
    virtual_addr: None | str | Unset = UNSET
    virtual_addr6: None | str | Unset = UNSET
    remote_host: None | str | Unset = UNSET
    remote_port: None | str | Unset = UNSET
    local_host: None | str | Unset = UNSET
    local_port: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        port: None | str | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        vpnid: int | None | Unset
        if isinstance(self.vpnid, Unset):
            vpnid = UNSET
        else:
            vpnid = self.vpnid

        mgmt: None | str | Unset
        if isinstance(self.mgmt, Unset):
            mgmt = UNSET
        else:
            mgmt = self.mgmt

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        state_detail: None | str | Unset
        if isinstance(self.state_detail, Unset):
            state_detail = UNSET
        else:
            state_detail = self.state_detail

        connect_time: None | str | Unset
        if isinstance(self.connect_time, Unset):
            connect_time = UNSET
        else:
            connect_time = self.connect_time

        virtual_addr: None | str | Unset
        if isinstance(self.virtual_addr, Unset):
            virtual_addr = UNSET
        else:
            virtual_addr = self.virtual_addr

        virtual_addr6: None | str | Unset
        if isinstance(self.virtual_addr6, Unset):
            virtual_addr6 = UNSET
        else:
            virtual_addr6 = self.virtual_addr6

        remote_host: None | str | Unset
        if isinstance(self.remote_host, Unset):
            remote_host = UNSET
        else:
            remote_host = self.remote_host

        remote_port: None | str | Unset
        if isinstance(self.remote_port, Unset):
            remote_port = UNSET
        else:
            remote_port = self.remote_port

        local_host: None | str | Unset
        if isinstance(self.local_host, Unset):
            local_host = UNSET
        else:
            local_host = self.local_host

        local_port: None | str | Unset
        if isinstance(self.local_port, Unset):
            local_port = UNSET
        else:
            local_port = self.local_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if mgmt is not UNSET:
            field_dict["mgmt"] = mgmt
        if status is not UNSET:
            field_dict["status"] = status
        if state is not UNSET:
            field_dict["state"] = state
        if state_detail is not UNSET:
            field_dict["state_detail"] = state_detail
        if connect_time is not UNSET:
            field_dict["connect_time"] = connect_time
        if virtual_addr is not UNSET:
            field_dict["virtual_addr"] = virtual_addr
        if virtual_addr6 is not UNSET:
            field_dict["virtual_addr6"] = virtual_addr6
        if remote_host is not UNSET:
            field_dict["remote_host"] = remote_host
        if remote_port is not UNSET:
            field_dict["remote_port"] = remote_port
        if local_host is not UNSET:
            field_dict["local_host"] = local_host
        if local_port is not UNSET:
            field_dict["local_port"] = local_port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_vpnid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vpnid = _parse_vpnid(d.pop("vpnid", UNSET))

        def _parse_mgmt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mgmt = _parse_mgmt(d.pop("mgmt", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_state_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_detail = _parse_state_detail(d.pop("state_detail", UNSET))

        def _parse_connect_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connect_time = _parse_connect_time(d.pop("connect_time", UNSET))

        def _parse_virtual_addr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_addr = _parse_virtual_addr(d.pop("virtual_addr", UNSET))

        def _parse_virtual_addr6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_addr6 = _parse_virtual_addr6(d.pop("virtual_addr6", UNSET))

        def _parse_remote_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_host = _parse_remote_host(d.pop("remote_host", UNSET))

        def _parse_remote_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_port = _parse_remote_port(d.pop("remote_port", UNSET))

        def _parse_local_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_host = _parse_local_host(d.pop("local_host", UNSET))

        def _parse_local_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_port = _parse_local_port(d.pop("local_port", UNSET))

        open_vpn_client_status = cls(
            name=name,
            port=port,
            vpnid=vpnid,
            mgmt=mgmt,
            status=status,
            state=state,
            state_detail=state_detail,
            connect_time=connect_time,
            virtual_addr=virtual_addr,
            virtual_addr6=virtual_addr6,
            remote_host=remote_host,
            remote_port=remote_port,
            local_host=local_host,
            local_port=local_port,
        )

        open_vpn_client_status.additional_properties = d
        return open_vpn_client_status

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
