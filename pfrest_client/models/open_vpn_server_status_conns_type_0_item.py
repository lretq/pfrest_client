from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNServerStatusConnsType0Item")


@_attrs_define
class OpenVPNServerStatusConnsType0Item:
    """
    Attributes:
        common_name (None | str | Unset): The common name of the OpenVPN server connection.<br>
        remote_host (None | str | Unset): The remote host of the OpenVPN server connection.<br>
        virtual_addr (None | str | Unset): The virtual address of the OpenVPN server connection.<br>
        virtual_addr6 (None | str | Unset): The virtual IPv6 address of the OpenVPN server connection.<br>
        bytes_recv (int | None | Unset): The number of bytes received by the OpenVPN server connection.<br>
        bytes_sent (int | None | Unset): The number of bytes sent by the OpenVPN server connection.<br>
        connect_time (None | str | Unset): The connection time of the OpenVPN server connection.<br>
        connect_time_unix (int | None | Unset): The connection time of the OpenVPN server connection in Unix time.<br>
        user_name (None | str | Unset): The user name of the OpenVPN server connection.<br>
        client_id (int | None | Unset): The client ID of the OpenVPN server connection.<br>
        peer_id (int | None | Unset): The peer ID of the OpenVPN server connection.<br>
        cipher (None | str | Unset): The cipher of the OpenVPN server connection.<br>
    """

    common_name: None | str | Unset = UNSET
    remote_host: None | str | Unset = UNSET
    virtual_addr: None | str | Unset = UNSET
    virtual_addr6: None | str | Unset = UNSET
    bytes_recv: int | None | Unset = UNSET
    bytes_sent: int | None | Unset = UNSET
    connect_time: None | str | Unset = UNSET
    connect_time_unix: int | None | Unset = UNSET
    user_name: None | str | Unset = UNSET
    client_id: int | None | Unset = UNSET
    peer_id: int | None | Unset = UNSET
    cipher: None | str | Unset = UNSET
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

        virtual_addr6: None | str | Unset
        if isinstance(self.virtual_addr6, Unset):
            virtual_addr6 = UNSET
        else:
            virtual_addr6 = self.virtual_addr6

        bytes_recv: int | None | Unset
        if isinstance(self.bytes_recv, Unset):
            bytes_recv = UNSET
        else:
            bytes_recv = self.bytes_recv

        bytes_sent: int | None | Unset
        if isinstance(self.bytes_sent, Unset):
            bytes_sent = UNSET
        else:
            bytes_sent = self.bytes_sent

        connect_time: None | str | Unset
        if isinstance(self.connect_time, Unset):
            connect_time = UNSET
        else:
            connect_time = self.connect_time

        connect_time_unix: int | None | Unset
        if isinstance(self.connect_time_unix, Unset):
            connect_time_unix = UNSET
        else:
            connect_time_unix = self.connect_time_unix

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        client_id: int | None | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        peer_id: int | None | Unset
        if isinstance(self.peer_id, Unset):
            peer_id = UNSET
        else:
            peer_id = self.peer_id

        cipher: None | str | Unset
        if isinstance(self.cipher, Unset):
            cipher = UNSET
        else:
            cipher = self.cipher

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if common_name is not UNSET:
            field_dict["common_name"] = common_name
        if remote_host is not UNSET:
            field_dict["remote_host"] = remote_host
        if virtual_addr is not UNSET:
            field_dict["virtual_addr"] = virtual_addr
        if virtual_addr6 is not UNSET:
            field_dict["virtual_addr6"] = virtual_addr6
        if bytes_recv is not UNSET:
            field_dict["bytes_recv"] = bytes_recv
        if bytes_sent is not UNSET:
            field_dict["bytes_sent"] = bytes_sent
        if connect_time is not UNSET:
            field_dict["connect_time"] = connect_time
        if connect_time_unix is not UNSET:
            field_dict["connect_time_unix"] = connect_time_unix
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if peer_id is not UNSET:
            field_dict["peer_id"] = peer_id
        if cipher is not UNSET:
            field_dict["cipher"] = cipher

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

        def _parse_virtual_addr6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_addr6 = _parse_virtual_addr6(d.pop("virtual_addr6", UNSET))

        def _parse_bytes_recv(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bytes_recv = _parse_bytes_recv(d.pop("bytes_recv", UNSET))

        def _parse_bytes_sent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bytes_sent = _parse_bytes_sent(d.pop("bytes_sent", UNSET))

        def _parse_connect_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connect_time = _parse_connect_time(d.pop("connect_time", UNSET))

        def _parse_connect_time_unix(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        connect_time_unix = _parse_connect_time_unix(d.pop("connect_time_unix", UNSET))

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("user_name", UNSET))

        def _parse_client_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        client_id = _parse_client_id(d.pop("client_id", UNSET))

        def _parse_peer_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        peer_id = _parse_peer_id(d.pop("peer_id", UNSET))

        def _parse_cipher(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cipher = _parse_cipher(d.pop("cipher", UNSET))

        open_vpn_server_status_conns_type_0_item = cls(
            common_name=common_name,
            remote_host=remote_host,
            virtual_addr=virtual_addr,
            virtual_addr6=virtual_addr6,
            bytes_recv=bytes_recv,
            bytes_sent=bytes_sent,
            connect_time=connect_time,
            connect_time_unix=connect_time_unix,
            user_name=user_name,
            client_id=client_id,
            peer_id=peer_id,
            cipher=cipher,
        )

        open_vpn_server_status_conns_type_0_item.additional_properties = d
        return open_vpn_server_status_conns_type_0_item

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
