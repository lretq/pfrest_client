from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.free_radiusmac_max_total_octets_time_range import FreeRADIUSMACMaxTotalOctetsTimeRange
from ..models.free_radiusmac_point_of_time import FreeRADIUSMACPointOfTime
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesFreeRADIUSMACEndpointJsonBody")


@_attrs_define
class PostServicesFreeRADIUSMACEndpointJsonBody:
    """
    Attributes:
        mac (str): The MAC address of the entry. May be delimited with '-' or ':' (e.g. 'aa:bb:cc:dd:ee:ff').<br>
        description (str | Unset): A description for this entry.<br>
        framed_ip_address (str | Unset): Framed-IP-Address MUST be supported by NAS. If the OpenVPN server uses a subnet
            style Topology the RADIUS server MUST also send back an appropriate Framed-IP-Netmask value matching the VPN
            Tunnel Network.<br>
        framed_ip_netmask (str | Unset): Framed-IP-Netmask MUST be supported by NAS.<br>
        framed_route (str | Unset): Framed-Route must be supported by NAS. Required format: Subnet Gateway Metric(s)
            (e.g. 192.168.10.0/24 192.168.10.1 1).<br>
        framed_ipv6_address (str | Unset): When the IPv6 prefix part is empty it uses Framed-IPv6-Address. When the
            prefix part is filled in, it uses Framed-IPv6-Prefix. Example: 2001:db8:abab::5 or 2001:db8:abab::/64<br>
        framed_ipv6_route (str | Unset): Framed-IPv6-Route must be supported by NAS. Required format: Prefix Gateway
            Metric(s) (e.g. 2001:db8:0:16::/64 2001:db8::16:a0:20ff:fe99:a998 1).<br>
        vlan_id (str | Unset): The VLAN ID (integer from 1-4095) or the VLAN name that this entry should be assigned to.
            Must be supported by the NAS.<br>
        wispr_redirection_url (str | Unset): The URL the user should be redirected to after successful login. Example:
            http://www.google.com<br>
        simultaneous_connect (int | None | Unset): The maximum number of simultaneous connections with this entry. Leave
            null for no limit. If using FreeRADIUS with Captive Portal you should leave this null.<br>
        expiration (str | Unset): The date when this account should expire. Required format: Mmm dd yyyy (e.g. Jan 01
            2030).<br>
        session_timeout (int | None | Unset): The time this entry has until relogin (in seconds).<br>
        login_time (str | Unset): The time when this entry should have access. Empty for no time restriction. Example:
            Wk0855-2305,Sa|Su2230-0230 (weekdays after 8:55 AM and before 11:05 PM | any time on Saturday | Sunday after
            10:30 PM and before 02:30 AM).<br>
        amount_of_time (int | None | Unset): The amount of time this entry is allowed (in minutes) within the configured
            time period.<br>
        point_of_time (FreeRADIUSMACPointOfTime | Unset): The time period after which the 'Amount of Time' is reset.<br>
            Default: FreeRADIUSMACPointOfTime.DAILY.
        max_total_octets (int | None | Unset): The amount of download and upload traffic (summarized) in megabytes (MB)
            for this entry. If using captive portal without periodic reauthentication enabled, this value must not exceed
            4095 due to protocol limitations.<br>
        max_total_octets_time_range (FreeRADIUSMACMaxTotalOctetsTimeRange | Unset): The time period for the amount of
            download and upload traffic. This does not automatically reset the counter; you must configure a cronjob to
            reset it.<br> Default: FreeRADIUSMACMaxTotalOctetsTimeRange.DAILY.
        max_bandwidth_down (int | None | Unset): The maximum bandwidth for download in kilobits (1000 bits) per second
            (Kbit/s).<br>
        max_bandwidth_up (int | None | Unset): The maximum bandwidth for upload in kilobits (1000 bits) per second
            (Kbit/s).<br>
        acct_interim_interval (int | None | Unset): The interval in seconds which should elapse between interim-updates.
            Must be more than 60s and should not be less than 600s.<br>
        top_additional_options (list[str] | Unset): Additional RADIUS attributes placed at the TOP of this entry. Each
            list entry becomes a separate line. For experts only.<br>
        check_items_additional_options (list[str] | Unset): Additional RADIUS check-item attributes for this entry. Each
            list entry becomes a separate attribute. For experts only.<br>
        reply_items_additional_options (list[str] | Unset): Additional RADIUS reply-item attributes for this entry. Each
            list entry becomes a separate attribute. For experts only.<br>
    """

    mac: str
    description: str | Unset = UNSET
    framed_ip_address: str | Unset = UNSET
    framed_ip_netmask: str | Unset = UNSET
    framed_route: str | Unset = UNSET
    framed_ipv6_address: str | Unset = UNSET
    framed_ipv6_route: str | Unset = UNSET
    vlan_id: str | Unset = UNSET
    wispr_redirection_url: str | Unset = UNSET
    simultaneous_connect: int | None | Unset = UNSET
    expiration: str | Unset = UNSET
    session_timeout: int | None | Unset = UNSET
    login_time: str | Unset = UNSET
    amount_of_time: int | None | Unset = UNSET
    point_of_time: FreeRADIUSMACPointOfTime | Unset = FreeRADIUSMACPointOfTime.DAILY
    max_total_octets: int | None | Unset = UNSET
    max_total_octets_time_range: FreeRADIUSMACMaxTotalOctetsTimeRange | Unset = (
        FreeRADIUSMACMaxTotalOctetsTimeRange.DAILY
    )
    max_bandwidth_down: int | None | Unset = UNSET
    max_bandwidth_up: int | None | Unset = UNSET
    acct_interim_interval: int | None | Unset = UNSET
    top_additional_options: list[str] | Unset = UNSET
    check_items_additional_options: list[str] | Unset = UNSET
    reply_items_additional_options: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        description = self.description

        framed_ip_address = self.framed_ip_address

        framed_ip_netmask = self.framed_ip_netmask

        framed_route = self.framed_route

        framed_ipv6_address = self.framed_ipv6_address

        framed_ipv6_route = self.framed_ipv6_route

        vlan_id = self.vlan_id

        wispr_redirection_url = self.wispr_redirection_url

        simultaneous_connect: int | None | Unset
        if isinstance(self.simultaneous_connect, Unset):
            simultaneous_connect = UNSET
        else:
            simultaneous_connect = self.simultaneous_connect

        expiration = self.expiration

        session_timeout: int | None | Unset
        if isinstance(self.session_timeout, Unset):
            session_timeout = UNSET
        else:
            session_timeout = self.session_timeout

        login_time = self.login_time

        amount_of_time: int | None | Unset
        if isinstance(self.amount_of_time, Unset):
            amount_of_time = UNSET
        else:
            amount_of_time = self.amount_of_time

        point_of_time: str | Unset = UNSET
        if not isinstance(self.point_of_time, Unset):
            point_of_time = self.point_of_time.value

        max_total_octets: int | None | Unset
        if isinstance(self.max_total_octets, Unset):
            max_total_octets = UNSET
        else:
            max_total_octets = self.max_total_octets

        max_total_octets_time_range: str | Unset = UNSET
        if not isinstance(self.max_total_octets_time_range, Unset):
            max_total_octets_time_range = self.max_total_octets_time_range.value

        max_bandwidth_down: int | None | Unset
        if isinstance(self.max_bandwidth_down, Unset):
            max_bandwidth_down = UNSET
        else:
            max_bandwidth_down = self.max_bandwidth_down

        max_bandwidth_up: int | None | Unset
        if isinstance(self.max_bandwidth_up, Unset):
            max_bandwidth_up = UNSET
        else:
            max_bandwidth_up = self.max_bandwidth_up

        acct_interim_interval: int | None | Unset
        if isinstance(self.acct_interim_interval, Unset):
            acct_interim_interval = UNSET
        else:
            acct_interim_interval = self.acct_interim_interval

        top_additional_options: list[str] | Unset = UNSET
        if not isinstance(self.top_additional_options, Unset):
            top_additional_options = self.top_additional_options

        check_items_additional_options: list[str] | Unset = UNSET
        if not isinstance(self.check_items_additional_options, Unset):
            check_items_additional_options = self.check_items_additional_options

        reply_items_additional_options: list[str] | Unset = UNSET
        if not isinstance(self.reply_items_additional_options, Unset):
            reply_items_additional_options = self.reply_items_additional_options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if framed_ip_address is not UNSET:
            field_dict["framed_ip_address"] = framed_ip_address
        if framed_ip_netmask is not UNSET:
            field_dict["framed_ip_netmask"] = framed_ip_netmask
        if framed_route is not UNSET:
            field_dict["framed_route"] = framed_route
        if framed_ipv6_address is not UNSET:
            field_dict["framed_ipv6_address"] = framed_ipv6_address
        if framed_ipv6_route is not UNSET:
            field_dict["framed_ipv6_route"] = framed_ipv6_route
        if vlan_id is not UNSET:
            field_dict["vlan_id"] = vlan_id
        if wispr_redirection_url is not UNSET:
            field_dict["wispr_redirection_url"] = wispr_redirection_url
        if simultaneous_connect is not UNSET:
            field_dict["simultaneous_connect"] = simultaneous_connect
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if session_timeout is not UNSET:
            field_dict["session_timeout"] = session_timeout
        if login_time is not UNSET:
            field_dict["login_time"] = login_time
        if amount_of_time is not UNSET:
            field_dict["amount_of_time"] = amount_of_time
        if point_of_time is not UNSET:
            field_dict["point_of_time"] = point_of_time
        if max_total_octets is not UNSET:
            field_dict["max_total_octets"] = max_total_octets
        if max_total_octets_time_range is not UNSET:
            field_dict["max_total_octets_time_range"] = max_total_octets_time_range
        if max_bandwidth_down is not UNSET:
            field_dict["max_bandwidth_down"] = max_bandwidth_down
        if max_bandwidth_up is not UNSET:
            field_dict["max_bandwidth_up"] = max_bandwidth_up
        if acct_interim_interval is not UNSET:
            field_dict["acct_interim_interval"] = acct_interim_interval
        if top_additional_options is not UNSET:
            field_dict["top_additional_options"] = top_additional_options
        if check_items_additional_options is not UNSET:
            field_dict["check_items_additional_options"] = check_items_additional_options
        if reply_items_additional_options is not UNSET:
            field_dict["reply_items_additional_options"] = reply_items_additional_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mac = d.pop("mac")

        description = d.pop("description", UNSET)

        framed_ip_address = d.pop("framed_ip_address", UNSET)

        framed_ip_netmask = d.pop("framed_ip_netmask", UNSET)

        framed_route = d.pop("framed_route", UNSET)

        framed_ipv6_address = d.pop("framed_ipv6_address", UNSET)

        framed_ipv6_route = d.pop("framed_ipv6_route", UNSET)

        vlan_id = d.pop("vlan_id", UNSET)

        wispr_redirection_url = d.pop("wispr_redirection_url", UNSET)

        def _parse_simultaneous_connect(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        simultaneous_connect = _parse_simultaneous_connect(d.pop("simultaneous_connect", UNSET))

        expiration = d.pop("expiration", UNSET)

        def _parse_session_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        session_timeout = _parse_session_timeout(d.pop("session_timeout", UNSET))

        login_time = d.pop("login_time", UNSET)

        def _parse_amount_of_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        amount_of_time = _parse_amount_of_time(d.pop("amount_of_time", UNSET))

        _point_of_time = d.pop("point_of_time", UNSET)
        point_of_time: FreeRADIUSMACPointOfTime | Unset
        if isinstance(_point_of_time, Unset):
            point_of_time = UNSET
        else:
            point_of_time = FreeRADIUSMACPointOfTime(_point_of_time)

        def _parse_max_total_octets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_total_octets = _parse_max_total_octets(d.pop("max_total_octets", UNSET))

        _max_total_octets_time_range = d.pop("max_total_octets_time_range", UNSET)
        max_total_octets_time_range: FreeRADIUSMACMaxTotalOctetsTimeRange | Unset
        if isinstance(_max_total_octets_time_range, Unset):
            max_total_octets_time_range = UNSET
        else:
            max_total_octets_time_range = FreeRADIUSMACMaxTotalOctetsTimeRange(_max_total_octets_time_range)

        def _parse_max_bandwidth_down(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_bandwidth_down = _parse_max_bandwidth_down(d.pop("max_bandwidth_down", UNSET))

        def _parse_max_bandwidth_up(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_bandwidth_up = _parse_max_bandwidth_up(d.pop("max_bandwidth_up", UNSET))

        def _parse_acct_interim_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        acct_interim_interval = _parse_acct_interim_interval(d.pop("acct_interim_interval", UNSET))

        top_additional_options = cast(list[str], d.pop("top_additional_options", UNSET))

        check_items_additional_options = cast(list[str], d.pop("check_items_additional_options", UNSET))

        reply_items_additional_options = cast(list[str], d.pop("reply_items_additional_options", UNSET))

        post_services_free_radiusmac_endpoint_json_body = cls(
            mac=mac,
            description=description,
            framed_ip_address=framed_ip_address,
            framed_ip_netmask=framed_ip_netmask,
            framed_route=framed_route,
            framed_ipv6_address=framed_ipv6_address,
            framed_ipv6_route=framed_ipv6_route,
            vlan_id=vlan_id,
            wispr_redirection_url=wispr_redirection_url,
            simultaneous_connect=simultaneous_connect,
            expiration=expiration,
            session_timeout=session_timeout,
            login_time=login_time,
            amount_of_time=amount_of_time,
            point_of_time=point_of_time,
            max_total_octets=max_total_octets,
            max_total_octets_time_range=max_total_octets_time_range,
            max_bandwidth_down=max_bandwidth_down,
            max_bandwidth_up=max_bandwidth_up,
            acct_interim_interval=acct_interim_interval,
            top_additional_options=top_additional_options,
            check_items_additional_options=check_items_additional_options,
            reply_items_additional_options=reply_items_additional_options,
        )

        post_services_free_radiusmac_endpoint_json_body.additional_properties = d
        return post_services_free_radiusmac_endpoint_json_body

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
