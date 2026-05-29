from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ARPTable")


@_attrs_define
class ARPTable:
    """
    Attributes:
        hostname (None | str | Unset): The hostname associated with the ARP entry.<br>
        ip_address (None | str | Unset): The IP address associated with the ARP entry.<br>
        mac_address (None | str | Unset): The MAC address associated with the ARP entry.<br>
        interface (None | str | Unset): The interface where the ARP entry was registered.<br>
        type_ (None | str | Unset): The type of connection this host utilizes.<br>
        permanent (bool | None | Unset): Indicates whether the ARP entry is permanent in the ARP table.<br>
        dnsresolve (None | str | Unset): The full DNS name associated with this ARP entry.<br>
        expires (None | str | Unset): The expiration time for this ARP entry.<br>
    """

    hostname: None | str | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    mac_address: None | str | Unset = UNSET
    interface: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    permanent: bool | None | Unset = UNSET
    dnsresolve: None | str | Unset = UNSET
    expires: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostname: None | str | Unset
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        mac_address: None | str | Unset
        if isinstance(self.mac_address, Unset):
            mac_address = UNSET
        else:
            mac_address = self.mac_address

        interface: None | str | Unset
        if isinstance(self.interface, Unset):
            interface = UNSET
        else:
            interface = self.interface

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        permanent: bool | None | Unset
        if isinstance(self.permanent, Unset):
            permanent = UNSET
        else:
            permanent = self.permanent

        dnsresolve: None | str | Unset
        if isinstance(self.dnsresolve, Unset):
            dnsresolve = UNSET
        else:
            dnsresolve = self.dnsresolve

        expires: None | str | Unset
        if isinstance(self.expires, Unset):
            expires = UNSET
        else:
            expires = self.expires

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address
        if mac_address is not UNSET:
            field_dict["mac_address"] = mac_address
        if interface is not UNSET:
            field_dict["interface"] = interface
        if type_ is not UNSET:
            field_dict["type"] = type_
        if permanent is not UNSET:
            field_dict["permanent"] = permanent
        if dnsresolve is not UNSET:
            field_dict["dnsresolve"] = dnsresolve
        if expires is not UNSET:
            field_dict["expires"] = expires

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ip_address", UNSET))

        def _parse_mac_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mac_address = _parse_mac_address(d.pop("mac_address", UNSET))

        def _parse_interface(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interface = _parse_interface(d.pop("interface", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_permanent(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        permanent = _parse_permanent(d.pop("permanent", UNSET))

        def _parse_dnsresolve(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dnsresolve = _parse_dnsresolve(d.pop("dnsresolve", UNSET))

        def _parse_expires(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires = _parse_expires(d.pop("expires", UNSET))

        arp_table = cls(
            hostname=hostname,
            ip_address=ip_address,
            mac_address=mac_address,
            interface=interface,
            type_=type_,
            permanent=permanent,
            dnsresolve=dnsresolve,
            expires=expires,
        )

        arp_table.additional_properties = d
        return arp_table

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
