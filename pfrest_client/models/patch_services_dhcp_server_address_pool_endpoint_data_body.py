from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dhcp_server_address_pool_denyunknown import DHCPServerAddressPoolDenyunknown
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesDHCPServerAddressPoolEndpointDataBody")


@_attrs_define
class PatchServicesDHCPServerAddressPoolEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        range_from (str | Unset): The starting IP address for this address pool. This address must be less than or equal
            to the `range_to` field.<br>
        range_to (str | Unset): The ending IP address for the this address pool. This address must be greater than or
            equal to the `range_to` field.<br>
        domain (str | Unset): The domain to be assigned via DHCP.<br>
        mac_allow (list[str] | Unset): MAC addresses this DHCP server is allowed to provide leases for.<br>
        mac_deny (list[str] | Unset): MAC addresses this DHCP server is not allowed to provide leases for.<br>
        domainsearchlist (list[str] | Unset): The domain search list to provide via DHCP.<br>
        defaultleasetime (int | None | Unset): The default DHCP lease validity period (in seconds). This is used for
            clients that do not ask for a specific expiration time.<br> Default: 7200.
        maxleasetime (int | None | Unset): The maximum DHCP lease validity period (in seconds) a client can request.<br>
            Default: 86400.
        gateway (str | Unset): The gateway IPv4 address to provide via DHCP. This is only necessary if you are not using
            the interface's IP as the gateway. Specify `none` for no gateway assignment.<br>
        dnsserver (list[str] | Unset): The DNS servers to provide via DHCP. Leave empty to default to system
            nameservers.<br>
        winsserver (list[str] | Unset): The WINS servers to provide via DHCP.<br>
        ntpserver (list[str] | Unset): The NTP servers to provide via DHCP.<br>
        ignorebootp (bool | Unset): Force this DHCP server to ignore BOOTP queries.<br>
        ignoreclientuids (bool | Unset): Prevent recording a unique identifier (UID) in client lease data if present in
            the client DHCP request. This option may be useful when a client can dual boot using different client
            identifiers but the same hardware (MAC) address. Note that the resulting server behavior violates the official
            DHCP specification.<br>
        denyunknown (DHCPServerAddressPoolDenyunknown | Unset): Define how to handle unknown clients requesting DHCP
            leases. When set to `null`, any DHCP client will get an IP address within this scope/range on this interface. If
            set to `enabled`, any DHCP client with a MAC address listed in a static mapping on any scope(s)/interface(s)
            will get an IP address. If set to `class`, only MAC addresses listed in static mappings on this interface will
            get an IP address within this scope/range.<br>
    """

    parent_id: int
    id: int
    range_from: str | Unset = UNSET
    range_to: str | Unset = UNSET
    domain: str | Unset = UNSET
    mac_allow: list[str] | Unset = UNSET
    mac_deny: list[str] | Unset = UNSET
    domainsearchlist: list[str] | Unset = UNSET
    defaultleasetime: int | None | Unset = 7200
    maxleasetime: int | None | Unset = 86400
    gateway: str | Unset = UNSET
    dnsserver: list[str] | Unset = UNSET
    winsserver: list[str] | Unset = UNSET
    ntpserver: list[str] | Unset = UNSET
    ignorebootp: bool | Unset = UNSET
    ignoreclientuids: bool | Unset = UNSET
    denyunknown: DHCPServerAddressPoolDenyunknown | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        range_from = self.range_from

        range_to = self.range_to

        domain = self.domain

        mac_allow: list[str] | Unset = UNSET
        if not isinstance(self.mac_allow, Unset):
            mac_allow = self.mac_allow

        mac_deny: list[str] | Unset = UNSET
        if not isinstance(self.mac_deny, Unset):
            mac_deny = self.mac_deny

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

        ignorebootp = self.ignorebootp

        ignoreclientuids = self.ignoreclientuids

        denyunknown: str | Unset = UNSET
        if not isinstance(self.denyunknown, Unset):
            denyunknown = self.denyunknown.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if range_from is not UNSET:
            field_dict["range_from"] = range_from
        if range_to is not UNSET:
            field_dict["range_to"] = range_to
        if domain is not UNSET:
            field_dict["domain"] = domain
        if mac_allow is not UNSET:
            field_dict["mac_allow"] = mac_allow
        if mac_deny is not UNSET:
            field_dict["mac_deny"] = mac_deny
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
        if ignorebootp is not UNSET:
            field_dict["ignorebootp"] = ignorebootp
        if ignoreclientuids is not UNSET:
            field_dict["ignoreclientuids"] = ignoreclientuids
        if denyunknown is not UNSET:
            field_dict["denyunknown"] = denyunknown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        range_from = d.pop("range_from", UNSET)

        range_to = d.pop("range_to", UNSET)

        domain = d.pop("domain", UNSET)

        mac_allow = cast(list[str], d.pop("mac_allow", UNSET))

        mac_deny = cast(list[str], d.pop("mac_deny", UNSET))

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

        ignorebootp = d.pop("ignorebootp", UNSET)

        ignoreclientuids = d.pop("ignoreclientuids", UNSET)

        _denyunknown = d.pop("denyunknown", UNSET)
        denyunknown: DHCPServerAddressPoolDenyunknown | Unset
        if isinstance(_denyunknown, Unset):
            denyunknown = UNSET
        else:
            denyunknown = DHCPServerAddressPoolDenyunknown(_denyunknown)

        patch_services_dhcp_server_address_pool_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            range_from=range_from,
            range_to=range_to,
            domain=domain,
            mac_allow=mac_allow,
            mac_deny=mac_deny,
            domainsearchlist=domainsearchlist,
            defaultleasetime=defaultleasetime,
            maxleasetime=maxleasetime,
            gateway=gateway,
            dnsserver=dnsserver,
            winsserver=winsserver,
            ntpserver=ntpserver,
            ignorebootp=ignorebootp,
            ignoreclientuids=ignoreclientuids,
            denyunknown=denyunknown,
        )

        patch_services_dhcp_server_address_pool_endpoint_data_body.additional_properties = d
        return patch_services_dhcp_server_address_pool_endpoint_data_body

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
