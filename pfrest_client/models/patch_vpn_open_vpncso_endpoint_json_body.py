from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.open_vpn_client_specific_override_netbios_ntype import OpenVPNClientSpecificOverrideNetbiosNtype
from ..models.open_vpn_client_specific_override_remove_options_item import (
    OpenVPNClientSpecificOverrideRemoveOptionsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchVPNOpenVPNCSOEndpointJsonBody")


@_attrs_define
class PatchVPNOpenVPNCSOEndpointJsonBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        common_name (str | Unset): The X.509 common name for the client certificate, or the username for VPNs utilizing
            password authentication.<br>
        disable (bool | Unset): Disables this client specific override.<br>
        block (bool | Unset): Enables or disables the client from connecting to this server. Do not use this option to
            permanently disable a client due to a compromised key or password. Use a CRL instead.<br>
        description (str | Unset): The description for this client specific override.<br>
        server_list (list[str] | Unset): The OpenVPN servers that will utilize this override. When no servers are
            specified, the override will apply to all servers.<br>
        tunnel_network (str | Unset): The IPv4 virtual network used for private communications between the server and
            client hosts.<br>
        tunnel_networkv6 (str | Unset): The IPv6 virtual network used for private communications between the server and
            client hosts.<br>
        local_network (list[str] | Unset): The IPv4 server-side networks that will be accessible from this particular
            client.<br>
        local_networkv6 (list[str] | Unset): the IPv6 server-side networks that will be accessible from this particular
            client.<br>
        remote_network (list[str] | Unset): The IPv4 client-side networks that will be routed to this client
            specifically using iroute, so that a site-to-site VPN can be established.<br>
        remote_networkv6 (list[str] | Unset): The IPv6 client-side networks that will be routed to this client
            specifically using iroute, so that a site-to-site VPN can be established.<br>
        gwredir (bool | Unset): Enable forcing all client-generated traffic through the tunnel.<br>
        push_reset (bool | Unset): Enables or disables preventing this client from receiving any server-defined client
            settings.<br>
        remove_options (list[OpenVPNClientSpecificOverrideRemoveOptionsItem] | Unset): Specifies the push-remove options
            to apply to the client<br><br>This field is only available when the following conditions are met:<br>-
            `push_reset` must be equal to `false`<br>
        dns_domain (str | Unset): The default domain to provide to the client.<br>
        dns_server1 (str | Unset): The primary DNS server to provide to the client.<br>
        dns_server2 (str | Unset): The secondary DNS server to provide to the client.<br>
        dns_server3 (str | Unset): The tertiary DNS server to provide to the client.<br>
        dns_server4 (str | Unset): The quaternary DNS server to provide to the client.<br>
        ntp_server1 (str | Unset): The primary NTP server to provide to the client.<br>
        ntp_server2 (str | Unset): The secondary NTP server to provide to the client.<br>
        netbios_enable (bool | Unset): Enables or disables NetBIOS over TCP/IP.<br>
        netbios_ntype (OpenVPNClientSpecificOverrideNetbiosNtype | Unset): The NetBIOS node type.<br><br>This field is
            only available when the following conditions are met:<br>- `netbios_enable` must be equal to `true`<br>
        netbios_scope (str | Unset): The NetBIOS Scope ID. This provides an extended naming service for NetBIOS over
            TCP/IP. The NetBIOS scope ID isolates NetBIOS traffic on a single network to only those nodes with the same
            NetBIOS scope ID.<br><br>This field is only available when the following conditions are met:<br>-
            `netbios_enable` must be equal to `true`<br>
        wins_server1 (str | Unset): The primary WINS server to provide to the client.<br><br>This field is only
            available when the following conditions are met:<br>- `netbios_enable` must be equal to `true`<br>
        wins_server2 (str | Unset): The secondary WINS server to provide to the client.<br><br>This field is only
            available when the following conditions are met:<br>- `netbios_enable` must be equal to `true`<br>
        custom_options (list[str] | Unset): Additional OpenVPN options to add for this client.<br>
    """

    id: int
    common_name: str | Unset = UNSET
    disable: bool | Unset = UNSET
    block: bool | Unset = UNSET
    description: str | Unset = UNSET
    server_list: list[str] | Unset = UNSET
    tunnel_network: str | Unset = UNSET
    tunnel_networkv6: str | Unset = UNSET
    local_network: list[str] | Unset = UNSET
    local_networkv6: list[str] | Unset = UNSET
    remote_network: list[str] | Unset = UNSET
    remote_networkv6: list[str] | Unset = UNSET
    gwredir: bool | Unset = UNSET
    push_reset: bool | Unset = UNSET
    remove_options: list[OpenVPNClientSpecificOverrideRemoveOptionsItem] | Unset = UNSET
    dns_domain: str | Unset = UNSET
    dns_server1: str | Unset = UNSET
    dns_server2: str | Unset = UNSET
    dns_server3: str | Unset = UNSET
    dns_server4: str | Unset = UNSET
    ntp_server1: str | Unset = UNSET
    ntp_server2: str | Unset = UNSET
    netbios_enable: bool | Unset = UNSET
    netbios_ntype: OpenVPNClientSpecificOverrideNetbiosNtype | Unset = UNSET
    netbios_scope: str | Unset = UNSET
    wins_server1: str | Unset = UNSET
    wins_server2: str | Unset = UNSET
    custom_options: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        common_name = self.common_name

        disable = self.disable

        block = self.block

        description = self.description

        server_list: list[str] | Unset = UNSET
        if not isinstance(self.server_list, Unset):
            server_list = self.server_list

        tunnel_network = self.tunnel_network

        tunnel_networkv6 = self.tunnel_networkv6

        local_network: list[str] | Unset = UNSET
        if not isinstance(self.local_network, Unset):
            local_network = self.local_network

        local_networkv6: list[str] | Unset = UNSET
        if not isinstance(self.local_networkv6, Unset):
            local_networkv6 = self.local_networkv6

        remote_network: list[str] | Unset = UNSET
        if not isinstance(self.remote_network, Unset):
            remote_network = self.remote_network

        remote_networkv6: list[str] | Unset = UNSET
        if not isinstance(self.remote_networkv6, Unset):
            remote_networkv6 = self.remote_networkv6

        gwredir = self.gwredir

        push_reset = self.push_reset

        remove_options: list[str] | Unset = UNSET
        if not isinstance(self.remove_options, Unset):
            remove_options = []
            for remove_options_item_data in self.remove_options:
                remove_options_item = remove_options_item_data.value
                remove_options.append(remove_options_item)

        dns_domain = self.dns_domain

        dns_server1 = self.dns_server1

        dns_server2 = self.dns_server2

        dns_server3 = self.dns_server3

        dns_server4 = self.dns_server4

        ntp_server1 = self.ntp_server1

        ntp_server2 = self.ntp_server2

        netbios_enable = self.netbios_enable

        netbios_ntype: int | Unset = UNSET
        if not isinstance(self.netbios_ntype, Unset):
            netbios_ntype = self.netbios_ntype.value

        netbios_scope = self.netbios_scope

        wins_server1 = self.wins_server1

        wins_server2 = self.wins_server2

        custom_options: list[str] | Unset = UNSET
        if not isinstance(self.custom_options, Unset):
            custom_options = self.custom_options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if common_name is not UNSET:
            field_dict["common_name"] = common_name
        if disable is not UNSET:
            field_dict["disable"] = disable
        if block is not UNSET:
            field_dict["block"] = block
        if description is not UNSET:
            field_dict["description"] = description
        if server_list is not UNSET:
            field_dict["server_list"] = server_list
        if tunnel_network is not UNSET:
            field_dict["tunnel_network"] = tunnel_network
        if tunnel_networkv6 is not UNSET:
            field_dict["tunnel_networkv6"] = tunnel_networkv6
        if local_network is not UNSET:
            field_dict["local_network"] = local_network
        if local_networkv6 is not UNSET:
            field_dict["local_networkv6"] = local_networkv6
        if remote_network is not UNSET:
            field_dict["remote_network"] = remote_network
        if remote_networkv6 is not UNSET:
            field_dict["remote_networkv6"] = remote_networkv6
        if gwredir is not UNSET:
            field_dict["gwredir"] = gwredir
        if push_reset is not UNSET:
            field_dict["push_reset"] = push_reset
        if remove_options is not UNSET:
            field_dict["remove_options"] = remove_options
        if dns_domain is not UNSET:
            field_dict["dns_domain"] = dns_domain
        if dns_server1 is not UNSET:
            field_dict["dns_server1"] = dns_server1
        if dns_server2 is not UNSET:
            field_dict["dns_server2"] = dns_server2
        if dns_server3 is not UNSET:
            field_dict["dns_server3"] = dns_server3
        if dns_server4 is not UNSET:
            field_dict["dns_server4"] = dns_server4
        if ntp_server1 is not UNSET:
            field_dict["ntp_server1"] = ntp_server1
        if ntp_server2 is not UNSET:
            field_dict["ntp_server2"] = ntp_server2
        if netbios_enable is not UNSET:
            field_dict["netbios_enable"] = netbios_enable
        if netbios_ntype is not UNSET:
            field_dict["netbios_ntype"] = netbios_ntype
        if netbios_scope is not UNSET:
            field_dict["netbios_scope"] = netbios_scope
        if wins_server1 is not UNSET:
            field_dict["wins_server1"] = wins_server1
        if wins_server2 is not UNSET:
            field_dict["wins_server2"] = wins_server2
        if custom_options is not UNSET:
            field_dict["custom_options"] = custom_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        common_name = d.pop("common_name", UNSET)

        disable = d.pop("disable", UNSET)

        block = d.pop("block", UNSET)

        description = d.pop("description", UNSET)

        server_list = cast(list[str], d.pop("server_list", UNSET))

        tunnel_network = d.pop("tunnel_network", UNSET)

        tunnel_networkv6 = d.pop("tunnel_networkv6", UNSET)

        local_network = cast(list[str], d.pop("local_network", UNSET))

        local_networkv6 = cast(list[str], d.pop("local_networkv6", UNSET))

        remote_network = cast(list[str], d.pop("remote_network", UNSET))

        remote_networkv6 = cast(list[str], d.pop("remote_networkv6", UNSET))

        gwredir = d.pop("gwredir", UNSET)

        push_reset = d.pop("push_reset", UNSET)

        _remove_options = d.pop("remove_options", UNSET)
        remove_options: list[OpenVPNClientSpecificOverrideRemoveOptionsItem] | Unset = UNSET
        if _remove_options is not UNSET:
            remove_options = []
            for remove_options_item_data in _remove_options:
                remove_options_item = OpenVPNClientSpecificOverrideRemoveOptionsItem(remove_options_item_data)

                remove_options.append(remove_options_item)

        dns_domain = d.pop("dns_domain", UNSET)

        dns_server1 = d.pop("dns_server1", UNSET)

        dns_server2 = d.pop("dns_server2", UNSET)

        dns_server3 = d.pop("dns_server3", UNSET)

        dns_server4 = d.pop("dns_server4", UNSET)

        ntp_server1 = d.pop("ntp_server1", UNSET)

        ntp_server2 = d.pop("ntp_server2", UNSET)

        netbios_enable = d.pop("netbios_enable", UNSET)

        _netbios_ntype = d.pop("netbios_ntype", UNSET)
        netbios_ntype: OpenVPNClientSpecificOverrideNetbiosNtype | Unset
        if isinstance(_netbios_ntype, Unset):
            netbios_ntype = UNSET
        else:
            netbios_ntype = OpenVPNClientSpecificOverrideNetbiosNtype(_netbios_ntype)

        netbios_scope = d.pop("netbios_scope", UNSET)

        wins_server1 = d.pop("wins_server1", UNSET)

        wins_server2 = d.pop("wins_server2", UNSET)

        custom_options = cast(list[str], d.pop("custom_options", UNSET))

        patch_vpn_open_vpncso_endpoint_json_body = cls(
            id=id,
            common_name=common_name,
            disable=disable,
            block=block,
            description=description,
            server_list=server_list,
            tunnel_network=tunnel_network,
            tunnel_networkv6=tunnel_networkv6,
            local_network=local_network,
            local_networkv6=local_networkv6,
            remote_network=remote_network,
            remote_networkv6=remote_networkv6,
            gwredir=gwredir,
            push_reset=push_reset,
            remove_options=remove_options,
            dns_domain=dns_domain,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            ntp_server1=ntp_server1,
            ntp_server2=ntp_server2,
            netbios_enable=netbios_enable,
            netbios_ntype=netbios_ntype,
            netbios_scope=netbios_scope,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            custom_options=custom_options,
        )

        patch_vpn_open_vpncso_endpoint_json_body.additional_properties = d
        return patch_vpn_open_vpncso_endpoint_json_body

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
