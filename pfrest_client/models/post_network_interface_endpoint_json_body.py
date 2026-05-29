from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.network_interface_adv_dhcp_pt_values import NetworkInterfaceAdvDhcpPtValues
from ..models.network_interface_typev_4 import NetworkInterfaceTypev4
from ..models.network_interface_typev_6 import NetworkInterfaceTypev6
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostNetworkInterfaceEndpointJsonBody")


@_attrs_define
class PostNetworkInterfaceEndpointJsonBody:
    """
    Attributes:
        if_ (str): The real interface this configuration will be applied to.<br>
        descr (str): The descriptive name for this interface.<br>
        typev4 (NetworkInterfaceTypev4): Selects the IPv4 address type to assign this interface.<br>
        ipaddr (str): Sets the IPv4 address to assign to this interface.<br><br>This field is only available when the
            following conditions are met:<br>- `typev4` must be one of [ static, dhcp ]<br>
        subnet (int): Sets the subnet bit count to assign this interface.<br><br>This field is only available when the
            following conditions are met:<br>- `typev4` must be equal to `'static'`<br>
        ipaddrv6 (str): Sets the IPv6 address to assign to this interface.<br><br>This field is only available when the
            following conditions are met:<br>- `typev6` must be one of [ staticv6, dhcp6, slaac, 6rd, track6, 6to4 ]<br>
        subnetv6 (int): Sets the subnet bit count to assign this interface.<br><br>This field is only available when the
            following conditions are met:<br>- `typev6` must be equal to `'staticv6'`<br>
        prefix_6rd (str): Sets the 6RD IPv6 prefix assigned by the ISP for this interface.<br><br>This field is only
            available when the following conditions are met:<br>- `typev6` must be equal to `'6rd'`<br>
        gateway_6rd (str): Sets the 6RD IPv4 gateway address assigned by the ISP for this interface.<br><br>This field
            is only available when the following conditions are met:<br>- `typev6` must be equal to `'6rd'`<br>
        prefix_6rd_v4plen (int): Sets the 6RD IPv4 prefix length. Normally specified by the ISP. A value of 0 means
            embed theentire IPv4 address in the 6RD prefix.<br><br>This field is only available when the following
            conditions are met:<br>- `typev6` must be equal to `'6rd'`<br>
        track6_interface (str): Sets the dynamic IPv6 WAN interface to track for configuration.<br><br>This field is
            only available when the following conditions are met:<br>- `typev6` must be equal to `'track6'`<br>
        enable (bool | Unset): Enable or disable this interface.<br>
        spoofmac (str | Unset): Assigns (spoofs) the MAC address for this interface instead of using the interface's
            real MAC.<br>
        mtu (int | None | Unset): Sets the MTU for this interface. Assumes default MTU if value is `null`.<br>
        mss (int | None | Unset): Sets the MSS for this interface. Assumes default MSS if value is `null`.<br>
        media (str | Unset): Sets the link speed for this interface. In most situations this can be left as the
            default.<br>
        mediaopt (str | Unset): Sets the link duplex for this interface. In most situations this can be left as the
            default.<br>
        blockpriv (bool | Unset): Enable or disable automatically blocking RFC 1918 private networks on this
            interface.<br>
        blockbogons (bool | Unset): Enable or disable automatically blocking bogon networks on this interface.<br>
        gateway (None | str | Unset): Sets the upstream gateway this interface will use. This is only applicable for
            WAN-type interfaces.<br><br>This field is only available when the following conditions are met:<br>- `typev4`
            must be equal to `'static'`<br>
        dhcphostname (str | Unset): Sets the DHCP hostname this interface will advertise via DHCP.<br><br>This field is
            only available when the following conditions are met:<br>- `typev4` must be equal to `'dhcp'`<br>
        alias_address (str | Unset): Sets the value used as a fixed alias IPv4 address by the DHCP client.<br><br>This
            field is only available when the following conditions are met:<br>- `typev4` must be equal to `'dhcp'`<br>
        alias_subnet (int | None | Unset): Sets the value used as the fixed alias IPv4 address's subnet bit count by the
            DHCP client.<br><br>This field is only available when the following conditions are met:<br>- `typev4` must be
            equal to `'dhcp'`<br> Default: 32.
        dhcprejectfrom (list[str] | Unset): Sets a list of IPv4 DHCP server addresses to reject DHCP offers for on this
            interface.<br><br>This field is only available when the following conditions are met:<br>- `typev4` must be
            equal to `'dhcp'`<br>
        adv_dhcp_config_advanced (bool | Unset): Enables or disables the advanced DHCP settings on this
            interface.<br><br>This field is only available when the following conditions are met:<br>- `typev4` must be
            equal to `'dhcp'`<br>
        adv_dhcp_pt_values (NetworkInterfaceAdvDhcpPtValues | Unset): Selects the advanced DHCP timing
            preset.<br><br>This field is only available when the following conditions are met:<br>- `typev4` must be equal
            to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br> Default:
            NetworkInterfaceAdvDhcpPtValues.SAVEDCFG.
        adv_dhcp_pt_timeout (int | None | Unset): Manually sets the timeout timing value used when requested DHCP leases
            on this interface.<br><br>This field is only available when the following conditions are met:<br>- `typev4` must
            be equal to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_pt_retry (int | None | Unset): Manually sets the retry timing value used when requested DHCP leases on
            this interface.<br><br>This field is only available when the following conditions are met:<br>- `typev4` must be
            equal to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_pt_select_timeout (int | None | Unset): Manually sets the select timing value used when requested DHCP
            leases on this interface.<br><br>This field is only available when the following conditions are met:<br>-
            `typev4` must be equal to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_pt_reboot (int | None | Unset): Manually sets the reboot timing value used when requested DHCP leases
            on this interface.<br><br>This field is only available when the following conditions are met:<br>- `typev4` must
            be equal to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_pt_backoff_cutoff (int | None | Unset): Manually sets the backoff cutoff timing value used when
            requested DHCP leases on this interface.<br><br>This field is only available when the following conditions are
            met:<br>- `typev4` must be equal to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_pt_initial_interval (int | None | Unset): Manually sets the initial interval timing value used when
            requested DHCP leases on this interface.<br><br>This field is only available when the following conditions are
            met:<br>- `typev4` must be equal to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_send_options (None | str | Unset): Sets DHCP options to be sent when requesting a DHCP lease for this
            interface.<br><br>This field is only available when the following conditions are met:<br>- `typev4` must be
            equal to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_request_options (None | str | Unset): Sets DHCP option 55 values to be sent when requesting a DHCP
            lease for this interface.<br><br>This field is only available when the following conditions are met:<br>-
            `typev4` must be equal to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_required_options (None | str | Unset): Sets DHCP options required by the client when requesting a DHCP
            lease for this interface.<br><br>This field is only available when the following conditions are met:<br>-
            `typev4` must be equal to `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_option_modifiers (None | str | Unset): Sets DHCP option modifiers applied to the obtained DHCP
            lease.<br><br>This field is only available when the following conditions are met:<br>- `typev4` must be equal to
            `'dhcp'`<br>- `adv_dhcp_config_advanced` must be equal to `true`<br>
        adv_dhcp_config_file_override (bool | Unset): Enables or disables overriding the entire DHCP configuration file
            for this interface.<br><br>This field is only available when the following conditions are met:<br>- `typev4`
            must be equal to `'dhcp'`<br>
        adv_dhcp_config_file_override_path (None | str | Unset): Sets the local file path of the custom DHCP
            configuration file.<br><br>This field is only available when the following conditions are met:<br>- `typev4`
            must be equal to `'dhcp'`<br>- `adv_dhcp_config_file_override` must be equal to `true`<br>
        typev6 (NetworkInterfaceTypev6 | Unset): Selects the IPv6 address type to assign this interface.<br>
        gatewayv6 (None | str | Unset): Sets the upstream IPv6 gateway this interface will use. This is only applicable
            for WAN-type interfaces.<br><br>This field is only available when the following conditions are met:<br>-
            `typev6` must be equal to `'staticv6'`<br>
        ipv6usev4iface (bool | Unset): Enable or disable IPv6 using the IPv4 connectivity link (PPPoE).<br><br>This
            field is only available when the following conditions are met:<br>- `typev6` must be equal to `'staticv6'`<br>
        slaacusev4iface (bool | Unset): Enable or disable IPv6 using the IPv4 connectivity link (PPPoE).<br><br>This
            field is only available when the following conditions are met:<br>- `typev6` must be equal to `'slaac'`<br>
        track6_prefix_id_hex (str | Unset): Sets the hexadecimal IPv6 prefix ID. This determines the configurable
            network ID based on the dynamic IPv6 connection.<br><br>This field is only available when the following
            conditions are met:<br>- `typev6` must be equal to `'track6'`<br>
    """

    if_: str
    descr: str
    typev4: NetworkInterfaceTypev4
    ipaddr: str
    subnet: int
    ipaddrv6: str
    subnetv6: int
    prefix_6rd: str
    gateway_6rd: str
    prefix_6rd_v4plen: int
    track6_interface: str
    enable: bool | Unset = UNSET
    spoofmac: str | Unset = UNSET
    mtu: int | None | Unset = UNSET
    mss: int | None | Unset = UNSET
    media: str | Unset = UNSET
    mediaopt: str | Unset = UNSET
    blockpriv: bool | Unset = UNSET
    blockbogons: bool | Unset = UNSET
    gateway: None | str | Unset = UNSET
    dhcphostname: str | Unset = UNSET
    alias_address: str | Unset = UNSET
    alias_subnet: int | None | Unset = 32
    dhcprejectfrom: list[str] | Unset = UNSET
    adv_dhcp_config_advanced: bool | Unset = UNSET
    adv_dhcp_pt_values: NetworkInterfaceAdvDhcpPtValues | Unset = NetworkInterfaceAdvDhcpPtValues.SAVEDCFG
    adv_dhcp_pt_timeout: int | None | Unset = UNSET
    adv_dhcp_pt_retry: int | None | Unset = UNSET
    adv_dhcp_pt_select_timeout: int | None | Unset = UNSET
    adv_dhcp_pt_reboot: int | None | Unset = UNSET
    adv_dhcp_pt_backoff_cutoff: int | None | Unset = UNSET
    adv_dhcp_pt_initial_interval: int | None | Unset = UNSET
    adv_dhcp_send_options: None | str | Unset = UNSET
    adv_dhcp_request_options: None | str | Unset = UNSET
    adv_dhcp_required_options: None | str | Unset = UNSET
    adv_dhcp_option_modifiers: None | str | Unset = UNSET
    adv_dhcp_config_file_override: bool | Unset = UNSET
    adv_dhcp_config_file_override_path: None | str | Unset = UNSET
    typev6: NetworkInterfaceTypev6 | Unset = UNSET
    gatewayv6: None | str | Unset = UNSET
    ipv6usev4iface: bool | Unset = UNSET
    slaacusev4iface: bool | Unset = UNSET
    track6_prefix_id_hex: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if_ = self.if_

        descr = self.descr

        typev4 = self.typev4.value

        ipaddr = self.ipaddr

        subnet = self.subnet

        ipaddrv6 = self.ipaddrv6

        subnetv6 = self.subnetv6

        prefix_6rd = self.prefix_6rd

        gateway_6rd = self.gateway_6rd

        prefix_6rd_v4plen = self.prefix_6rd_v4plen

        track6_interface = self.track6_interface

        enable = self.enable

        spoofmac = self.spoofmac

        mtu: int | None | Unset
        if isinstance(self.mtu, Unset):
            mtu = UNSET
        else:
            mtu = self.mtu

        mss: int | None | Unset
        if isinstance(self.mss, Unset):
            mss = UNSET
        else:
            mss = self.mss

        media = self.media

        mediaopt = self.mediaopt

        blockpriv = self.blockpriv

        blockbogons = self.blockbogons

        gateway: None | str | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        else:
            gateway = self.gateway

        dhcphostname = self.dhcphostname

        alias_address = self.alias_address

        alias_subnet: int | None | Unset
        if isinstance(self.alias_subnet, Unset):
            alias_subnet = UNSET
        else:
            alias_subnet = self.alias_subnet

        dhcprejectfrom: list[str] | Unset = UNSET
        if not isinstance(self.dhcprejectfrom, Unset):
            dhcprejectfrom = self.dhcprejectfrom

        adv_dhcp_config_advanced = self.adv_dhcp_config_advanced

        adv_dhcp_pt_values: str | Unset = UNSET
        if not isinstance(self.adv_dhcp_pt_values, Unset):
            adv_dhcp_pt_values = self.adv_dhcp_pt_values.value

        adv_dhcp_pt_timeout: int | None | Unset
        if isinstance(self.adv_dhcp_pt_timeout, Unset):
            adv_dhcp_pt_timeout = UNSET
        else:
            adv_dhcp_pt_timeout = self.adv_dhcp_pt_timeout

        adv_dhcp_pt_retry: int | None | Unset
        if isinstance(self.adv_dhcp_pt_retry, Unset):
            adv_dhcp_pt_retry = UNSET
        else:
            adv_dhcp_pt_retry = self.adv_dhcp_pt_retry

        adv_dhcp_pt_select_timeout: int | None | Unset
        if isinstance(self.adv_dhcp_pt_select_timeout, Unset):
            adv_dhcp_pt_select_timeout = UNSET
        else:
            adv_dhcp_pt_select_timeout = self.adv_dhcp_pt_select_timeout

        adv_dhcp_pt_reboot: int | None | Unset
        if isinstance(self.adv_dhcp_pt_reboot, Unset):
            adv_dhcp_pt_reboot = UNSET
        else:
            adv_dhcp_pt_reboot = self.adv_dhcp_pt_reboot

        adv_dhcp_pt_backoff_cutoff: int | None | Unset
        if isinstance(self.adv_dhcp_pt_backoff_cutoff, Unset):
            adv_dhcp_pt_backoff_cutoff = UNSET
        else:
            adv_dhcp_pt_backoff_cutoff = self.adv_dhcp_pt_backoff_cutoff

        adv_dhcp_pt_initial_interval: int | None | Unset
        if isinstance(self.adv_dhcp_pt_initial_interval, Unset):
            adv_dhcp_pt_initial_interval = UNSET
        else:
            adv_dhcp_pt_initial_interval = self.adv_dhcp_pt_initial_interval

        adv_dhcp_send_options: None | str | Unset
        if isinstance(self.adv_dhcp_send_options, Unset):
            adv_dhcp_send_options = UNSET
        else:
            adv_dhcp_send_options = self.adv_dhcp_send_options

        adv_dhcp_request_options: None | str | Unset
        if isinstance(self.adv_dhcp_request_options, Unset):
            adv_dhcp_request_options = UNSET
        else:
            adv_dhcp_request_options = self.adv_dhcp_request_options

        adv_dhcp_required_options: None | str | Unset
        if isinstance(self.adv_dhcp_required_options, Unset):
            adv_dhcp_required_options = UNSET
        else:
            adv_dhcp_required_options = self.adv_dhcp_required_options

        adv_dhcp_option_modifiers: None | str | Unset
        if isinstance(self.adv_dhcp_option_modifiers, Unset):
            adv_dhcp_option_modifiers = UNSET
        else:
            adv_dhcp_option_modifiers = self.adv_dhcp_option_modifiers

        adv_dhcp_config_file_override = self.adv_dhcp_config_file_override

        adv_dhcp_config_file_override_path: None | str | Unset
        if isinstance(self.adv_dhcp_config_file_override_path, Unset):
            adv_dhcp_config_file_override_path = UNSET
        else:
            adv_dhcp_config_file_override_path = self.adv_dhcp_config_file_override_path

        typev6: str | Unset = UNSET
        if not isinstance(self.typev6, Unset):
            typev6 = self.typev6.value

        gatewayv6: None | str | Unset
        if isinstance(self.gatewayv6, Unset):
            gatewayv6 = UNSET
        else:
            gatewayv6 = self.gatewayv6

        ipv6usev4iface = self.ipv6usev4iface

        slaacusev4iface = self.slaacusev4iface

        track6_prefix_id_hex = self.track6_prefix_id_hex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if": if_,
                "descr": descr,
                "typev4": typev4,
                "ipaddr": ipaddr,
                "subnet": subnet,
                "ipaddrv6": ipaddrv6,
                "subnetv6": subnetv6,
                "prefix_6rd": prefix_6rd,
                "gateway_6rd": gateway_6rd,
                "prefix_6rd_v4plen": prefix_6rd_v4plen,
                "track6_interface": track6_interface,
            }
        )
        if enable is not UNSET:
            field_dict["enable"] = enable
        if spoofmac is not UNSET:
            field_dict["spoofmac"] = spoofmac
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if mss is not UNSET:
            field_dict["mss"] = mss
        if media is not UNSET:
            field_dict["media"] = media
        if mediaopt is not UNSET:
            field_dict["mediaopt"] = mediaopt
        if blockpriv is not UNSET:
            field_dict["blockpriv"] = blockpriv
        if blockbogons is not UNSET:
            field_dict["blockbogons"] = blockbogons
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if dhcphostname is not UNSET:
            field_dict["dhcphostname"] = dhcphostname
        if alias_address is not UNSET:
            field_dict["alias_address"] = alias_address
        if alias_subnet is not UNSET:
            field_dict["alias_subnet"] = alias_subnet
        if dhcprejectfrom is not UNSET:
            field_dict["dhcprejectfrom"] = dhcprejectfrom
        if adv_dhcp_config_advanced is not UNSET:
            field_dict["adv_dhcp_config_advanced"] = adv_dhcp_config_advanced
        if adv_dhcp_pt_values is not UNSET:
            field_dict["adv_dhcp_pt_values"] = adv_dhcp_pt_values
        if adv_dhcp_pt_timeout is not UNSET:
            field_dict["adv_dhcp_pt_timeout"] = adv_dhcp_pt_timeout
        if adv_dhcp_pt_retry is not UNSET:
            field_dict["adv_dhcp_pt_retry"] = adv_dhcp_pt_retry
        if adv_dhcp_pt_select_timeout is not UNSET:
            field_dict["adv_dhcp_pt_select_timeout"] = adv_dhcp_pt_select_timeout
        if adv_dhcp_pt_reboot is not UNSET:
            field_dict["adv_dhcp_pt_reboot"] = adv_dhcp_pt_reboot
        if adv_dhcp_pt_backoff_cutoff is not UNSET:
            field_dict["adv_dhcp_pt_backoff_cutoff"] = adv_dhcp_pt_backoff_cutoff
        if adv_dhcp_pt_initial_interval is not UNSET:
            field_dict["adv_dhcp_pt_initial_interval"] = adv_dhcp_pt_initial_interval
        if adv_dhcp_send_options is not UNSET:
            field_dict["adv_dhcp_send_options"] = adv_dhcp_send_options
        if adv_dhcp_request_options is not UNSET:
            field_dict["adv_dhcp_request_options"] = adv_dhcp_request_options
        if adv_dhcp_required_options is not UNSET:
            field_dict["adv_dhcp_required_options"] = adv_dhcp_required_options
        if adv_dhcp_option_modifiers is not UNSET:
            field_dict["adv_dhcp_option_modifiers"] = adv_dhcp_option_modifiers
        if adv_dhcp_config_file_override is not UNSET:
            field_dict["adv_dhcp_config_file_override"] = adv_dhcp_config_file_override
        if adv_dhcp_config_file_override_path is not UNSET:
            field_dict["adv_dhcp_config_file_override_path"] = adv_dhcp_config_file_override_path
        if typev6 is not UNSET:
            field_dict["typev6"] = typev6
        if gatewayv6 is not UNSET:
            field_dict["gatewayv6"] = gatewayv6
        if ipv6usev4iface is not UNSET:
            field_dict["ipv6usev4iface"] = ipv6usev4iface
        if slaacusev4iface is not UNSET:
            field_dict["slaacusev4iface"] = slaacusev4iface
        if track6_prefix_id_hex is not UNSET:
            field_dict["track6_prefix_id_hex"] = track6_prefix_id_hex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        if_ = d.pop("if")

        descr = d.pop("descr")

        typev4 = NetworkInterfaceTypev4(d.pop("typev4"))

        ipaddr = d.pop("ipaddr")

        subnet = d.pop("subnet")

        ipaddrv6 = d.pop("ipaddrv6")

        subnetv6 = d.pop("subnetv6")

        prefix_6rd = d.pop("prefix_6rd")

        gateway_6rd = d.pop("gateway_6rd")

        prefix_6rd_v4plen = d.pop("prefix_6rd_v4plen")

        track6_interface = d.pop("track6_interface")

        enable = d.pop("enable", UNSET)

        spoofmac = d.pop("spoofmac", UNSET)

        def _parse_mtu(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mtu = _parse_mtu(d.pop("mtu", UNSET))

        def _parse_mss(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mss = _parse_mss(d.pop("mss", UNSET))

        media = d.pop("media", UNSET)

        mediaopt = d.pop("mediaopt", UNSET)

        blockpriv = d.pop("blockpriv", UNSET)

        blockbogons = d.pop("blockbogons", UNSET)

        def _parse_gateway(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))

        dhcphostname = d.pop("dhcphostname", UNSET)

        alias_address = d.pop("alias_address", UNSET)

        def _parse_alias_subnet(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        alias_subnet = _parse_alias_subnet(d.pop("alias_subnet", UNSET))

        dhcprejectfrom = cast(list[str], d.pop("dhcprejectfrom", UNSET))

        adv_dhcp_config_advanced = d.pop("adv_dhcp_config_advanced", UNSET)

        _adv_dhcp_pt_values = d.pop("adv_dhcp_pt_values", UNSET)
        adv_dhcp_pt_values: NetworkInterfaceAdvDhcpPtValues | Unset
        if isinstance(_adv_dhcp_pt_values, Unset):
            adv_dhcp_pt_values = UNSET
        else:
            adv_dhcp_pt_values = NetworkInterfaceAdvDhcpPtValues(_adv_dhcp_pt_values)

        def _parse_adv_dhcp_pt_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adv_dhcp_pt_timeout = _parse_adv_dhcp_pt_timeout(d.pop("adv_dhcp_pt_timeout", UNSET))

        def _parse_adv_dhcp_pt_retry(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adv_dhcp_pt_retry = _parse_adv_dhcp_pt_retry(d.pop("adv_dhcp_pt_retry", UNSET))

        def _parse_adv_dhcp_pt_select_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adv_dhcp_pt_select_timeout = _parse_adv_dhcp_pt_select_timeout(d.pop("adv_dhcp_pt_select_timeout", UNSET))

        def _parse_adv_dhcp_pt_reboot(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adv_dhcp_pt_reboot = _parse_adv_dhcp_pt_reboot(d.pop("adv_dhcp_pt_reboot", UNSET))

        def _parse_adv_dhcp_pt_backoff_cutoff(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adv_dhcp_pt_backoff_cutoff = _parse_adv_dhcp_pt_backoff_cutoff(d.pop("adv_dhcp_pt_backoff_cutoff", UNSET))

        def _parse_adv_dhcp_pt_initial_interval(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adv_dhcp_pt_initial_interval = _parse_adv_dhcp_pt_initial_interval(d.pop("adv_dhcp_pt_initial_interval", UNSET))

        def _parse_adv_dhcp_send_options(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adv_dhcp_send_options = _parse_adv_dhcp_send_options(d.pop("adv_dhcp_send_options", UNSET))

        def _parse_adv_dhcp_request_options(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adv_dhcp_request_options = _parse_adv_dhcp_request_options(d.pop("adv_dhcp_request_options", UNSET))

        def _parse_adv_dhcp_required_options(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adv_dhcp_required_options = _parse_adv_dhcp_required_options(d.pop("adv_dhcp_required_options", UNSET))

        def _parse_adv_dhcp_option_modifiers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adv_dhcp_option_modifiers = _parse_adv_dhcp_option_modifiers(d.pop("adv_dhcp_option_modifiers", UNSET))

        adv_dhcp_config_file_override = d.pop("adv_dhcp_config_file_override", UNSET)

        def _parse_adv_dhcp_config_file_override_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adv_dhcp_config_file_override_path = _parse_adv_dhcp_config_file_override_path(
            d.pop("adv_dhcp_config_file_override_path", UNSET)
        )

        _typev6 = d.pop("typev6", UNSET)
        typev6: NetworkInterfaceTypev6 | Unset
        if isinstance(_typev6, Unset):
            typev6 = UNSET
        else:
            typev6 = NetworkInterfaceTypev6(_typev6)

        def _parse_gatewayv6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gatewayv6 = _parse_gatewayv6(d.pop("gatewayv6", UNSET))

        ipv6usev4iface = d.pop("ipv6usev4iface", UNSET)

        slaacusev4iface = d.pop("slaacusev4iface", UNSET)

        track6_prefix_id_hex = d.pop("track6_prefix_id_hex", UNSET)

        post_network_interface_endpoint_json_body = cls(
            if_=if_,
            descr=descr,
            typev4=typev4,
            ipaddr=ipaddr,
            subnet=subnet,
            ipaddrv6=ipaddrv6,
            subnetv6=subnetv6,
            prefix_6rd=prefix_6rd,
            gateway_6rd=gateway_6rd,
            prefix_6rd_v4plen=prefix_6rd_v4plen,
            track6_interface=track6_interface,
            enable=enable,
            spoofmac=spoofmac,
            mtu=mtu,
            mss=mss,
            media=media,
            mediaopt=mediaopt,
            blockpriv=blockpriv,
            blockbogons=blockbogons,
            gateway=gateway,
            dhcphostname=dhcphostname,
            alias_address=alias_address,
            alias_subnet=alias_subnet,
            dhcprejectfrom=dhcprejectfrom,
            adv_dhcp_config_advanced=adv_dhcp_config_advanced,
            adv_dhcp_pt_values=adv_dhcp_pt_values,
            adv_dhcp_pt_timeout=adv_dhcp_pt_timeout,
            adv_dhcp_pt_retry=adv_dhcp_pt_retry,
            adv_dhcp_pt_select_timeout=adv_dhcp_pt_select_timeout,
            adv_dhcp_pt_reboot=adv_dhcp_pt_reboot,
            adv_dhcp_pt_backoff_cutoff=adv_dhcp_pt_backoff_cutoff,
            adv_dhcp_pt_initial_interval=adv_dhcp_pt_initial_interval,
            adv_dhcp_send_options=adv_dhcp_send_options,
            adv_dhcp_request_options=adv_dhcp_request_options,
            adv_dhcp_required_options=adv_dhcp_required_options,
            adv_dhcp_option_modifiers=adv_dhcp_option_modifiers,
            adv_dhcp_config_file_override=adv_dhcp_config_file_override,
            adv_dhcp_config_file_override_path=adv_dhcp_config_file_override_path,
            typev6=typev6,
            gatewayv6=gatewayv6,
            ipv6usev4iface=ipv6usev4iface,
            slaacusev4iface=slaacusev4iface,
            track6_prefix_id_hex=track6_prefix_id_hex,
        )

        post_network_interface_endpoint_json_body.additional_properties = d
        return post_network_interface_endpoint_json_body

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
