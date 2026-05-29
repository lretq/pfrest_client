from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dhcp_server_denyunknown import DHCPServerDenyunknown
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_server_numberoptions_item import DHCPServerNumberoptionsItem
    from ..models.dhcp_server_pool_item import DHCPServerPoolItem
    from ..models.dhcp_server_staticmap_item import DHCPServerStaticmapItem


T = TypeVar("T", bound="PutServicesDHCPServersEndpointJsonBodyItem")


@_attrs_define
class PutServicesDHCPServersEndpointJsonBodyItem:
    """
    Attributes:
        interface (str): The interface to configure the DHCP server for. This field is only necessary when you wantto
            change the interface (ID) of an existing DHCP server, or you are replacing all DHCP server objects with a new
            configuration. Note that specifying an interface in this field will update the ID of the DHCP server to match
            the interface specified here. Leaving this field empty will retain the existing interface.<br>
        enable (bool | Unset): Enable the DHCP server for this interface.<br>
        range_from (str | Unset): The starting IP address for the primary DHCP pool. This address must be less than or
            equal to the `range_to` field.<br>
        range_to (str | Unset): The ending IP address for the primary DHCP pool. This address must be greater than or
            equal to the `range_to` field.<br>
        domain (str | Unset): The domain to be assigned via DHCP.<br>
        failover_peerip (str | Unset): The interface IP address of the other firewall (failover peer) in this subnet.
            Leave empty to disable failover peering.<br>
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
        staticarp (bool | Unset): Assign static ARP entries for DHCP leases provided by this server.<br>
        ignorebootp (bool | Unset): Force this DHCP server to ignore BOOTP queries.<br>
        ignoreclientuids (bool | Unset): Prevent recording a unique identifier (UID) in client lease data if present in
            the client DHCP request. This option may be useful when a client can dual boot using different client
            identifiers but the same hardware (MAC) address. Note that the resulting server behavior violates the official
            DHCP specification.<br>
        nonak (bool | Unset): Ignore denied clients rather than reject. This option is not compatible with failover and
            cannot be enabled when a Failover Peer IP address is configured.<br>
        disablepingcheck (bool | Unset): Prevent the DHCP server from sending a ping to the address being assigned,
            where if no response has been heard, it assigns the address.<br>
        dhcpleaseinlocaltime (bool | Unset): Display the DHCP lease times in local time instead of UTC.<br>
        statsgraph (bool | Unset): Enable adding DHCP lease statistics to the pfSense Monitoring graphs.<br>
        denyunknown (DHCPServerDenyunknown | Unset): Define how to handle unknown clients requesting DHCP leases. When
            set to `null`, any DHCP client will get an IP address within this scope/range on this interface. If set to
            `enabled`, any DHCP client with a MAC address listed in a static mapping on any scope(s)/interface(s) will get
            an IP address. If set to `class`, only MAC addresses listed in static mappings on this interface will get an IP
            address within this scope/range.<br>
        pool (list[DHCPServerPoolItem] | Unset): Additional address pools applied to this DHCP server.<br>
        numberoptions (list[DHCPServerNumberoptionsItem] | Unset): The custom DHCP options to apply to this DHCP
            server.<br>
        staticmap (list[DHCPServerStaticmapItem] | Unset): Static mappings applied to this DHCP server.<br>
    """

    interface: str
    enable: bool | Unset = UNSET
    range_from: str | Unset = UNSET
    range_to: str | Unset = UNSET
    domain: str | Unset = UNSET
    failover_peerip: str | Unset = UNSET
    mac_allow: list[str] | Unset = UNSET
    mac_deny: list[str] | Unset = UNSET
    domainsearchlist: list[str] | Unset = UNSET
    defaultleasetime: int | None | Unset = 7200
    maxleasetime: int | None | Unset = 86400
    gateway: str | Unset = UNSET
    dnsserver: list[str] | Unset = UNSET
    winsserver: list[str] | Unset = UNSET
    ntpserver: list[str] | Unset = UNSET
    staticarp: bool | Unset = UNSET
    ignorebootp: bool | Unset = UNSET
    ignoreclientuids: bool | Unset = UNSET
    nonak: bool | Unset = UNSET
    disablepingcheck: bool | Unset = UNSET
    dhcpleaseinlocaltime: bool | Unset = UNSET
    statsgraph: bool | Unset = UNSET
    denyunknown: DHCPServerDenyunknown | Unset = UNSET
    pool: list[DHCPServerPoolItem] | Unset = UNSET
    numberoptions: list[DHCPServerNumberoptionsItem] | Unset = UNSET
    staticmap: list[DHCPServerStaticmapItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        enable = self.enable

        range_from = self.range_from

        range_to = self.range_to

        domain = self.domain

        failover_peerip = self.failover_peerip

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

        staticarp = self.staticarp

        ignorebootp = self.ignorebootp

        ignoreclientuids = self.ignoreclientuids

        nonak = self.nonak

        disablepingcheck = self.disablepingcheck

        dhcpleaseinlocaltime = self.dhcpleaseinlocaltime

        statsgraph = self.statsgraph

        denyunknown: str | Unset = UNSET
        if not isinstance(self.denyunknown, Unset):
            denyunknown = self.denyunknown.value

        pool: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pool, Unset):
            pool = []
            for pool_item_data in self.pool:
                pool_item = pool_item_data.to_dict()
                pool.append(pool_item)

        numberoptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.numberoptions, Unset):
            numberoptions = []
            for numberoptions_item_data in self.numberoptions:
                numberoptions_item = numberoptions_item_data.to_dict()
                numberoptions.append(numberoptions_item)

        staticmap: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.staticmap, Unset):
            staticmap = []
            for staticmap_item_data in self.staticmap:
                staticmap_item = staticmap_item_data.to_dict()
                staticmap.append(staticmap_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interface": interface,
            }
        )
        if enable is not UNSET:
            field_dict["enable"] = enable
        if range_from is not UNSET:
            field_dict["range_from"] = range_from
        if range_to is not UNSET:
            field_dict["range_to"] = range_to
        if domain is not UNSET:
            field_dict["domain"] = domain
        if failover_peerip is not UNSET:
            field_dict["failover_peerip"] = failover_peerip
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
        if staticarp is not UNSET:
            field_dict["staticarp"] = staticarp
        if ignorebootp is not UNSET:
            field_dict["ignorebootp"] = ignorebootp
        if ignoreclientuids is not UNSET:
            field_dict["ignoreclientuids"] = ignoreclientuids
        if nonak is not UNSET:
            field_dict["nonak"] = nonak
        if disablepingcheck is not UNSET:
            field_dict["disablepingcheck"] = disablepingcheck
        if dhcpleaseinlocaltime is not UNSET:
            field_dict["dhcpleaseinlocaltime"] = dhcpleaseinlocaltime
        if statsgraph is not UNSET:
            field_dict["statsgraph"] = statsgraph
        if denyunknown is not UNSET:
            field_dict["denyunknown"] = denyunknown
        if pool is not UNSET:
            field_dict["pool"] = pool
        if numberoptions is not UNSET:
            field_dict["numberoptions"] = numberoptions
        if staticmap is not UNSET:
            field_dict["staticmap"] = staticmap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dhcp_server_numberoptions_item import DHCPServerNumberoptionsItem
        from ..models.dhcp_server_pool_item import DHCPServerPoolItem
        from ..models.dhcp_server_staticmap_item import DHCPServerStaticmapItem

        d = dict(src_dict)
        interface = d.pop("interface")

        enable = d.pop("enable", UNSET)

        range_from = d.pop("range_from", UNSET)

        range_to = d.pop("range_to", UNSET)

        domain = d.pop("domain", UNSET)

        failover_peerip = d.pop("failover_peerip", UNSET)

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

        staticarp = d.pop("staticarp", UNSET)

        ignorebootp = d.pop("ignorebootp", UNSET)

        ignoreclientuids = d.pop("ignoreclientuids", UNSET)

        nonak = d.pop("nonak", UNSET)

        disablepingcheck = d.pop("disablepingcheck", UNSET)

        dhcpleaseinlocaltime = d.pop("dhcpleaseinlocaltime", UNSET)

        statsgraph = d.pop("statsgraph", UNSET)

        _denyunknown = d.pop("denyunknown", UNSET)
        denyunknown: DHCPServerDenyunknown | Unset
        if isinstance(_denyunknown, Unset):
            denyunknown = UNSET
        else:
            denyunknown = DHCPServerDenyunknown(_denyunknown)

        _pool = d.pop("pool", UNSET)
        pool: list[DHCPServerPoolItem] | Unset = UNSET
        if _pool is not UNSET:
            pool = []
            for pool_item_data in _pool:
                pool_item = DHCPServerPoolItem.from_dict(pool_item_data)

                pool.append(pool_item)

        _numberoptions = d.pop("numberoptions", UNSET)
        numberoptions: list[DHCPServerNumberoptionsItem] | Unset = UNSET
        if _numberoptions is not UNSET:
            numberoptions = []
            for numberoptions_item_data in _numberoptions:
                numberoptions_item = DHCPServerNumberoptionsItem.from_dict(numberoptions_item_data)

                numberoptions.append(numberoptions_item)

        _staticmap = d.pop("staticmap", UNSET)
        staticmap: list[DHCPServerStaticmapItem] | Unset = UNSET
        if _staticmap is not UNSET:
            staticmap = []
            for staticmap_item_data in _staticmap:
                staticmap_item = DHCPServerStaticmapItem.from_dict(staticmap_item_data)

                staticmap.append(staticmap_item)

        put_services_dhcp_servers_endpoint_json_body_item = cls(
            interface=interface,
            enable=enable,
            range_from=range_from,
            range_to=range_to,
            domain=domain,
            failover_peerip=failover_peerip,
            mac_allow=mac_allow,
            mac_deny=mac_deny,
            domainsearchlist=domainsearchlist,
            defaultleasetime=defaultleasetime,
            maxleasetime=maxleasetime,
            gateway=gateway,
            dnsserver=dnsserver,
            winsserver=winsserver,
            ntpserver=ntpserver,
            staticarp=staticarp,
            ignorebootp=ignorebootp,
            ignoreclientuids=ignoreclientuids,
            nonak=nonak,
            disablepingcheck=disablepingcheck,
            dhcpleaseinlocaltime=dhcpleaseinlocaltime,
            statsgraph=statsgraph,
            denyunknown=denyunknown,
            pool=pool,
            numberoptions=numberoptions,
            staticmap=staticmap,
        )

        put_services_dhcp_servers_endpoint_json_body_item.additional_properties = d
        return put_services_dhcp_servers_endpoint_json_body_item

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
