from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outbound_nat_mapping_poolopts import OutboundNATMappingPoolopts
from ..models.outbound_nat_mapping_protocol import OutboundNATMappingProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFirewallNATOutboundMappingEndpointJsonBody")


@_attrs_define
class PostFirewallNATOutboundMappingEndpointJsonBody:
    """
    Attributes:
        interface (str): The interface on which traffic is matched as it exits the firewall. In most cases this is a
            WAN-type or another externally-connected interface.<br>
        source (str): The source network this rule should match. Valid value options are: an existing interface, a
            subnet CIDR, an existing alias, `any`, `(self)`, `pppoe`. The context of this address can be inverted by
            prefixing the value with `!`. For interface values, the `:ip`  modifier can be appended to the value to use the
            interface's IP address instead of its entire subnet.<br>
        destination (str): The destination network this rule should match. Valid value options are: an existing
            interface, a subnet CIDR, an existing alias, `any`, `pppoe`. The context of this address can be inverted by
            prefixing the value with `!`. For interface values, the `:ip`  modifier can be appended to the value to use the
            interface's IP address instead of its entire subnet.<br>
        target (str): The target network traffic matching this rule should be translated to. Valid value options are: an
            IP address, an existing alias. For interface values, the `:ip`  modifier can be appended to the value to use the
            interface's IP address instead of its entire subnet.<br><br>This field is only available when the following
            conditions are met:<br>- `nonat` must be equal to `false`<br>
        protocol (OutboundNATMappingProtocol | Unset): The protocol this rule should match. Use `null` for any
            protocol.<br>
        disabled (bool | Unset): Disable this outbound NAT rule.<br>
        nonat (bool | Unset): Do not NAT traffic matching this rule.<br>
        nosync (bool | Unset): Do not sync this rule to HA peers.<br>
        source_port (None | str | Unset): The source port this rule should match. Valid options are: a TCP/UDP port
            number, a TCP/UDP port range separated by `:`, an existing port type firewall alias<br>
        destination_port (None | str | Unset): The destination port this rule should match. Valid options are: a TCP/UDP
            port number, a TCP/UDP port range separated by `:`, an existing port type firewall alias<br>
        target_subnet (int | Unset): The subnet bits for the assigned `target`. This field is only applicable if
            `target` is set to an IP address. This has no affect for alias or interface `targets`.<br><br>This field is only
            available when the following conditions are met:<br>- `nonat` must be equal to `false`<br> Default: 128.
        nat_port (str | Unset): The external source port or port range used for rewriting the original source port on
            connections matching the rule. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by
            `:`<br><br>This field is only available when the following conditions are met:<br>- `static_nat_port` must be
            equal to `false`<br>- `nonat` must be equal to `false`<br>
        static_nat_port (bool | Unset): Do not rewrite source port for traffic matching this rule.<br><br>This field is
            only available when the following conditions are met:<br>- `nonat` must be equal to `false`<br>
        poolopts (OutboundNATMappingPoolopts | Unset): The pool option used to load balance external IP mapping when
            `target` is set to a subnet or alias of many addresses. Set to `null` to revert to the system
            default.<br><br>This field is only available when the following conditions are met:<br>- `nonat` must be equal
            to `false`<br>
        source_hash_key (str | Unset): The key that is fed to the hashing algorithm in hex format. This must be a 16
            byte (32 character) hex string prefixed with `0x`. If a value is not provided, one will automatically be
            generated<br><br>This field is only available when the following conditions are met:<br>- `poolopts` must be
            equal to `'source-hash'`<br>- `nonat` must be equal to `false`<br> Default:
            '0x322ba3a1033b2d2e3a5c03cb2156414f'.
        descr (str | Unset): A description for the outbound NAT mapping.<br>
    """

    interface: str
    source: str
    destination: str
    target: str
    protocol: OutboundNATMappingProtocol | Unset = UNSET
    disabled: bool | Unset = UNSET
    nonat: bool | Unset = UNSET
    nosync: bool | Unset = UNSET
    source_port: None | str | Unset = UNSET
    destination_port: None | str | Unset = UNSET
    target_subnet: int | Unset = 128
    nat_port: str | Unset = UNSET
    static_nat_port: bool | Unset = UNSET
    poolopts: OutboundNATMappingPoolopts | Unset = UNSET
    source_hash_key: str | Unset = "0x322ba3a1033b2d2e3a5c03cb2156414f"
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        source = self.source

        destination = self.destination

        target = self.target

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        disabled = self.disabled

        nonat = self.nonat

        nosync = self.nosync

        source_port: None | str | Unset
        if isinstance(self.source_port, Unset):
            source_port = UNSET
        else:
            source_port = self.source_port

        destination_port: None | str | Unset
        if isinstance(self.destination_port, Unset):
            destination_port = UNSET
        else:
            destination_port = self.destination_port

        target_subnet = self.target_subnet

        nat_port = self.nat_port

        static_nat_port = self.static_nat_port

        poolopts: str | Unset = UNSET
        if not isinstance(self.poolopts, Unset):
            poolopts = self.poolopts.value

        source_hash_key = self.source_hash_key

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interface": interface,
                "source": source,
                "destination": destination,
                "target": target,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if nonat is not UNSET:
            field_dict["nonat"] = nonat
        if nosync is not UNSET:
            field_dict["nosync"] = nosync
        if source_port is not UNSET:
            field_dict["source_port"] = source_port
        if destination_port is not UNSET:
            field_dict["destination_port"] = destination_port
        if target_subnet is not UNSET:
            field_dict["target_subnet"] = target_subnet
        if nat_port is not UNSET:
            field_dict["nat_port"] = nat_port
        if static_nat_port is not UNSET:
            field_dict["static_nat_port"] = static_nat_port
        if poolopts is not UNSET:
            field_dict["poolopts"] = poolopts
        if source_hash_key is not UNSET:
            field_dict["source_hash_key"] = source_hash_key
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interface = d.pop("interface")

        source = d.pop("source")

        destination = d.pop("destination")

        target = d.pop("target")

        _protocol = d.pop("protocol", UNSET)
        protocol: OutboundNATMappingProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = OutboundNATMappingProtocol(_protocol)

        disabled = d.pop("disabled", UNSET)

        nonat = d.pop("nonat", UNSET)

        nosync = d.pop("nosync", UNSET)

        def _parse_source_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_port = _parse_source_port(d.pop("source_port", UNSET))

        def _parse_destination_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_port = _parse_destination_port(d.pop("destination_port", UNSET))

        target_subnet = d.pop("target_subnet", UNSET)

        nat_port = d.pop("nat_port", UNSET)

        static_nat_port = d.pop("static_nat_port", UNSET)

        _poolopts = d.pop("poolopts", UNSET)
        poolopts: OutboundNATMappingPoolopts | Unset
        if isinstance(_poolopts, Unset):
            poolopts = UNSET
        else:
            poolopts = OutboundNATMappingPoolopts(_poolopts)

        source_hash_key = d.pop("source_hash_key", UNSET)

        descr = d.pop("descr", UNSET)

        post_firewall_nat_outbound_mapping_endpoint_json_body = cls(
            interface=interface,
            source=source,
            destination=destination,
            target=target,
            protocol=protocol,
            disabled=disabled,
            nonat=nonat,
            nosync=nosync,
            source_port=source_port,
            destination_port=destination_port,
            target_subnet=target_subnet,
            nat_port=nat_port,
            static_nat_port=static_nat_port,
            poolopts=poolopts,
            source_hash_key=source_hash_key,
            descr=descr,
        )

        post_firewall_nat_outbound_mapping_endpoint_json_body.additional_properties = d
        return post_firewall_nat_outbound_mapping_endpoint_json_body

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
