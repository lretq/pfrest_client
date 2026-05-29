from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesDHCPServerStaticMappingEndpointJsonBody")


@_attrs_define
class PostServicesDHCPServerStaticMappingEndpointJsonBody:
    """
    Attributes:
        mac (str): The MAC address of the client this mapping is for.<br>
        parent_id (int): The ID of the parent this object is nested under.
        ipaddr (None | str | Unset): The IP address to assign this client via DHCP.<br>
        cid (None | str | Unset): The client identifier of the client this mapping is for.<br>
        hostname (None | str | Unset): The hostname to assign this client via DHCP.<br>
        domain (str | Unset): The domain to be assigned via DHCP.<br>
        domainsearchlist (list[str] | Unset): The domain search list to provide via DHCP.<br>
        defaultleasetime (int | None | Unset): The default DHCP lease validity period (in seconds). This is used for
            clients that do not ask for a specific expiration time.<br> Default: 7200.
        maxleasetime (int | None | Unset): The maximum DHCP lease validity period (in seconds) this client can
            request.<br> Default: 86400.
        gateway (str | Unset): The gateway IPv4 address to provide via DHCP. This is only necessary if you are not using
            the interface's IP as the gateway. Specify `none` for no gateway assignment.<br>
        dnsserver (list[str] | Unset): The DNS servers to provide via DHCP. Leave empty to default to system
            nameservers.<br>
        winsserver (list[str] | Unset): The WINS servers to provide via DHCP.<br>
        ntpserver (list[str] | Unset): The NTP servers to provide via DHCP.<br>
        arp_table_static_entry (bool | Unset): Assign a static ARP entry for this static mapping.<br>
        descr (str | Unset): The description of this static mapping.<br>
    """

    mac: str
    parent_id: int
    ipaddr: None | str | Unset = UNSET
    cid: None | str | Unset = UNSET
    hostname: None | str | Unset = UNSET
    domain: str | Unset = UNSET
    domainsearchlist: list[str] | Unset = UNSET
    defaultleasetime: int | None | Unset = 7200
    maxleasetime: int | None | Unset = 86400
    gateway: str | Unset = UNSET
    dnsserver: list[str] | Unset = UNSET
    winsserver: list[str] | Unset = UNSET
    ntpserver: list[str] | Unset = UNSET
    arp_table_static_entry: bool | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        parent_id = self.parent_id

        ipaddr: None | str | Unset
        if isinstance(self.ipaddr, Unset):
            ipaddr = UNSET
        else:
            ipaddr = self.ipaddr

        cid: None | str | Unset
        if isinstance(self.cid, Unset):
            cid = UNSET
        else:
            cid = self.cid

        hostname: None | str | Unset
        if isinstance(self.hostname, Unset):
            hostname = UNSET
        else:
            hostname = self.hostname

        domain = self.domain

        domainsearchlist: list[str] | Unset = UNSET
        if not isinstance(self.domainsearchlist, Unset):
            domainsearchlist = self.domainsearchlist

        defaultleasetime: int | None | Unset
        if isinstance(self.defaultleasetime, Unset):
            defaultleasetime = UNSET
        else:
            defaultleasetime = self.defaultleasetime

        maxleasetime: int | None | Unset
        if isinstance(self.maxleasetime, Unset):
            maxleasetime = UNSET
        else:
            maxleasetime = self.maxleasetime

        gateway = self.gateway

        dnsserver: list[str] | Unset = UNSET
        if not isinstance(self.dnsserver, Unset):
            dnsserver = self.dnsserver

        winsserver: list[str] | Unset = UNSET
        if not isinstance(self.winsserver, Unset):
            winsserver = self.winsserver

        ntpserver: list[str] | Unset = UNSET
        if not isinstance(self.ntpserver, Unset):
            ntpserver = self.ntpserver

        arp_table_static_entry = self.arp_table_static_entry

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "parent_id": parent_id,
            }
        )
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if cid is not UNSET:
            field_dict["cid"] = cid
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if domain is not UNSET:
            field_dict["domain"] = domain
        if domainsearchlist is not UNSET:
            field_dict["domainsearchlist"] = domainsearchlist
        if defaultleasetime is not UNSET:
            field_dict["defaultleasetime"] = defaultleasetime
        if maxleasetime is not UNSET:
            field_dict["maxleasetime"] = maxleasetime
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if dnsserver is not UNSET:
            field_dict["dnsserver"] = dnsserver
        if winsserver is not UNSET:
            field_dict["winsserver"] = winsserver
        if ntpserver is not UNSET:
            field_dict["ntpserver"] = ntpserver
        if arp_table_static_entry is not UNSET:
            field_dict["arp_table_static_entry"] = arp_table_static_entry
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mac = d.pop("mac")

        parent_id = d.pop("parent_id")

        def _parse_ipaddr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ipaddr = _parse_ipaddr(d.pop("ipaddr", UNSET))

        def _parse_cid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cid = _parse_cid(d.pop("cid", UNSET))

        def _parse_hostname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostname = _parse_hostname(d.pop("hostname", UNSET))

        domain = d.pop("domain", UNSET)

        domainsearchlist = cast(list[str], d.pop("domainsearchlist", UNSET))

        def _parse_defaultleasetime(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        defaultleasetime = _parse_defaultleasetime(d.pop("defaultleasetime", UNSET))

        def _parse_maxleasetime(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        maxleasetime = _parse_maxleasetime(d.pop("maxleasetime", UNSET))

        gateway = d.pop("gateway", UNSET)

        dnsserver = cast(list[str], d.pop("dnsserver", UNSET))

        winsserver = cast(list[str], d.pop("winsserver", UNSET))

        ntpserver = cast(list[str], d.pop("ntpserver", UNSET))

        arp_table_static_entry = d.pop("arp_table_static_entry", UNSET)

        descr = d.pop("descr", UNSET)

        post_services_dhcp_server_static_mapping_endpoint_json_body = cls(
            mac=mac,
            parent_id=parent_id,
            ipaddr=ipaddr,
            cid=cid,
            hostname=hostname,
            domain=domain,
            domainsearchlist=domainsearchlist,
            defaultleasetime=defaultleasetime,
            maxleasetime=maxleasetime,
            gateway=gateway,
            dnsserver=dnsserver,
            winsserver=winsserver,
            ntpserver=ntpserver,
            arp_table_static_entry=arp_table_static_entry,
            descr=descr,
        )

        post_services_dhcp_server_static_mapping_endpoint_json_body.additional_properties = d
        return post_services_dhcp_server_static_mapping_endpoint_json_body

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
