from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.port_forward_ipprotocol import PortForwardIpprotocol
from ..models.port_forward_natreflection import PortForwardNatreflection
from ..models.port_forward_protocol import PortForwardProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutFirewallNATPortForwardsEndpointJsonBodyItem")


@_attrs_define
class PutFirewallNATPortForwardsEndpointJsonBodyItem:
    """
    Attributes:
        interface (str): The interface this port forward rule applies to.<br>
        protocol (PortForwardProtocol): The IP/transport protocol this port forward rule should match.<br>
        source (str): The source address this port forward rule applies to. Valid value options are: an existing
            interface, an IP address, a subnet CIDR, an existing alias, `any`, `(self)`, `l2tp`, `pppoe`. The context of
            this address can be inverted by prefixing the value with `!`. For interface values, the `:ip`  modifier can be
            appended to the value to use the interface's IP address instead of its entire subnet.<br>
        destination (str): The destination address this rule applies to. Valid value options are: an existing interface,
            an IP address, a subnet CIDR, an existing alias, `any`, `(self)`, `l2tp`, `pppoe`. The context of this address
            can be inverted by prefixing the value with `!`. For interface values, the `:ip`  modifier can be appended to
            the value to use the interface's IP address instead of its entire subnet.<br>
        target (str): The IP address or alias of the internal host to forward matching traffic to. Valid value options
            are: an IP address, an existing alias. For interface values, the `:ip`  modifier can be appended to the value to
            use the interface's IP address instead of its entire subnet.<br>
        local_port (str): The port on the internal host to forward matching traffic to. In most cases, this must match
            the `destination_port` value. In the event that the `desintation_port` is a range, this value should be the
            first value in that range. Valid options are: a TCP/UDP port number, an existing port type firewall
            alias<br><br>This field is only available when the following conditions are met:<br>- `protocol` must be one of
            [ tcp, udp, tcp/udp ]<br>
        ipprotocol (PortForwardIpprotocol | Unset): The IP protocol this port forward rule should match.<br> Default:
            PortForwardIpprotocol.INET.
        source_port (None | str | Unset): The source port this port forward rule applies to. Set to `null` to allow any
            source port. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by `:`, an existing port
            type firewall alias<br><br>This field is only available when the following conditions are met:<br>- `protocol`
            must be one of [ tcp, udp, tcp/udp ]<br>
        destination_port (None | str | Unset): The destination port this port forward rule applies to. Set to `null` to
            allow any destination port. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by `:`, an
            existing port type firewall alias<br><br>This field is only available when the following conditions are
            met:<br>- `protocol` must be one of [ tcp, udp, tcp/udp ]<br>
        disabled (bool | Unset): Disables this port forward rule.<br>
        nordr (bool | Unset): Disables redirection for traffic matching this rule.<br>
        nosync (bool | Unset): Prevents this port forward rule from being synced to non-primary CARP members.<br>
        descr (str | Unset): A description for this port forward rule.<br>
        natreflection (PortForwardNatreflection | Unset): The NAT reflection mode to use for traffic matching this port
            forward rule. Set to `null` to use the system default.<br>
        associated_rule_id (str | Unset): The associated firewall rule mode. Use an empty string to require a separate
            firewall rule to be created to pass traffic matching this port forward rule. Use `new` to create a new
            associated firewall rule to pass traffic matching this port forward rule. Use `pass` to automatically pass
            traffic matching this port forward rule without the need for a firewall rule.   Otherwise, you can specify the
            `associated_rule_id` of an existing firewall rule to associate with this port forward rule.<br>
        created_time (int | None | Unset): The unix timestamp of when this port forward rule was original created.<br>
        created_by (None | str | Unset): The username and IP of the user who originally created this port forward
            rule.<br> Default: '@unknown IP (API)'.
        updated_time (int | None | Unset): The unix timestamp of when this port forward rule was original created.<br>
        updated_by (None | str | Unset): The username and IP of the user who last updated this port forward rule.<br>
            Default: '@unknown IP (API)'.
    """

    interface: str
    protocol: PortForwardProtocol
    source: str
    destination: str
    target: str
    local_port: str
    ipprotocol: PortForwardIpprotocol | Unset = PortForwardIpprotocol.INET
    source_port: None | str | Unset = UNSET
    destination_port: None | str | Unset = UNSET
    disabled: bool | Unset = UNSET
    nordr: bool | Unset = UNSET
    nosync: bool | Unset = UNSET
    descr: str | Unset = UNSET
    natreflection: PortForwardNatreflection | Unset = UNSET
    associated_rule_id: str | Unset = UNSET
    created_time: int | None | Unset = UNSET
    created_by: None | str | Unset = "@unknown IP (API)"
    updated_time: int | None | Unset = UNSET
    updated_by: None | str | Unset = "@unknown IP (API)"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        protocol = self.protocol.value

        source = self.source

        destination = self.destination

        target = self.target

        local_port = self.local_port

        ipprotocol: str | Unset = UNSET
        if not isinstance(self.ipprotocol, Unset):
            ipprotocol = self.ipprotocol.value

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

        disabled = self.disabled

        nordr = self.nordr

        nosync = self.nosync

        descr = self.descr

        natreflection: str | Unset = UNSET
        if not isinstance(self.natreflection, Unset):
            natreflection = self.natreflection.value

        associated_rule_id = self.associated_rule_id

        created_time: int | None | Unset
        if isinstance(self.created_time, Unset):
            created_time = UNSET
        else:
            created_time = self.created_time

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_time: int | None | Unset
        if isinstance(self.updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = self.updated_time

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interface": interface,
                "protocol": protocol,
                "source": source,
                "destination": destination,
                "target": target,
                "local_port": local_port,
            }
        )
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if source_port is not UNSET:
            field_dict["source_port"] = source_port
        if destination_port is not UNSET:
            field_dict["destination_port"] = destination_port
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if nordr is not UNSET:
            field_dict["nordr"] = nordr
        if nosync is not UNSET:
            field_dict["nosync"] = nosync
        if descr is not UNSET:
            field_dict["descr"] = descr
        if natreflection is not UNSET:
            field_dict["natreflection"] = natreflection
        if associated_rule_id is not UNSET:
            field_dict["associated_rule_id"] = associated_rule_id
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_time is not UNSET:
            field_dict["updated_time"] = updated_time
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interface = d.pop("interface")

        protocol = PortForwardProtocol(d.pop("protocol"))

        source = d.pop("source")

        destination = d.pop("destination")

        target = d.pop("target")

        local_port = d.pop("local_port")

        _ipprotocol = d.pop("ipprotocol", UNSET)
        ipprotocol: PortForwardIpprotocol | Unset
        if isinstance(_ipprotocol, Unset):
            ipprotocol = UNSET
        else:
            ipprotocol = PortForwardIpprotocol(_ipprotocol)

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

        disabled = d.pop("disabled", UNSET)

        nordr = d.pop("nordr", UNSET)

        nosync = d.pop("nosync", UNSET)

        descr = d.pop("descr", UNSET)

        _natreflection = d.pop("natreflection", UNSET)
        natreflection: PortForwardNatreflection | Unset
        if isinstance(_natreflection, Unset):
            natreflection = UNSET
        else:
            natreflection = PortForwardNatreflection(_natreflection)

        associated_rule_id = d.pop("associated_rule_id", UNSET)

        def _parse_created_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created_time = _parse_created_time(d.pop("created_time", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        updated_time = _parse_updated_time(d.pop("updated_time", UNSET))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        put_firewall_nat_port_forwards_endpoint_json_body_item = cls(
            interface=interface,
            protocol=protocol,
            source=source,
            destination=destination,
            target=target,
            local_port=local_port,
            ipprotocol=ipprotocol,
            source_port=source_port,
            destination_port=destination_port,
            disabled=disabled,
            nordr=nordr,
            nosync=nosync,
            descr=descr,
            natreflection=natreflection,
            associated_rule_id=associated_rule_id,
            created_time=created_time,
            created_by=created_by,
            updated_time=updated_time,
            updated_by=updated_by,
        )

        put_firewall_nat_port_forwards_endpoint_json_body_item.additional_properties = d
        return put_firewall_nat_port_forwards_endpoint_json_body_item

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
