from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DHCPServerLease")


@_attrs_define
class DHCPServerLease:
    """
    Attributes:
        ip (None | str | Unset): The IP address of the lease.<br>
        mac (None | str | Unset): The MAC address of the lease.<br>
        hostname (None | str | Unset): The hostname of the lease.<br>
        if_ (None | str | Unset): The interface the lease was registered on.<br>
        starts (None | str | Unset): The start time of the lease.<br>
        ends (None | str | Unset): The end time of the lease.<br>
        active_status (None | str | Unset): The active status of the lease.<br>
        online_status (None | str | Unset): The online status of the lease.<br>
        descr (None | str | Unset): The description of the lease.<br>
    """

    ip: None | str | Unset = UNSET
    mac: None | str | Unset = UNSET
    hostname: None | str | Unset = UNSET
    if_: None | str | Unset = UNSET
    starts: None | str | Unset = UNSET
    ends: None | str | Unset = UNSET
    active_status: None | str | Unset = UNSET
    online_status: None | str | Unset = UNSET
    descr: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        mac: None | str | Unset
        if isinstance(self.mac, Unset):
            mac = UNSET
        else:
            mac = self.mac

        hostname: None | str | Unset
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        if_: None | str | Unset
        if isinstance(self.if_, Unset):
            if_ = UNSET
        else:
            if_ = self.if_

        starts: None | str | Unset
        if isinstance(self.starts, Unset):
            starts = UNSET
        else:
            starts = self.starts

        ends: None | str | Unset
        if isinstance(self.ends, Unset):
            ends = UNSET
        else:
            ends = self.ends

        active_status: None | str | Unset
        if isinstance(self.active_status, Unset):
            active_status = UNSET
        else:
            active_status = self.active_status

        online_status: None | str | Unset
        if isinstance(self.online_status, Unset):
            online_status = UNSET
        else:
            online_status = self.online_status

        descr: None | str | Unset
        if isinstance(self.descr, Unset):
            descr = UNSET
        else:
            descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip is not UNSET:
            field_dict["ip"] = ip
        if mac is not UNSET:
            field_dict["mac"] = mac
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if if_ is not UNSET:
            field_dict["if"] = if_
        if starts is not UNSET:
            field_dict["starts"] = starts
        if ends is not UNSET:
            field_dict["ends"] = ends
        if active_status is not UNSET:
            field_dict["active_status"] = active_status
        if online_status is not UNSET:
            field_dict["online_status"] = online_status
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        def _parse_mac(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mac = _parse_mac(d.pop("mac", UNSET))

        def _parse_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        def _parse_if_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        if_ = _parse_if_(d.pop("if", UNSET))

        def _parse_starts(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        starts = _parse_starts(d.pop("starts", UNSET))

        def _parse_ends(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ends = _parse_ends(d.pop("ends", UNSET))

        def _parse_active_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        active_status = _parse_active_status(d.pop("active_status", UNSET))

        def _parse_online_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        online_status = _parse_online_status(d.pop("online_status", UNSET))

        def _parse_descr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        descr = _parse_descr(d.pop("descr", UNSET))

        dhcp_server_lease = cls(
            ip=ip,
            mac=mac,
            hostname=hostname,
            if_=if_,
            starts=starts,
            ends=ends,
            active_status=active_status,
            online_status=online_status,
            descr=descr,
        )

        dhcp_server_lease.additional_properties = d
        return dhcp_server_lease

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
