from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.firewall_rule_direction import FirewallRuleDirection
from ..models.firewall_rule_icmptype_item import FirewallRuleIcmptypeItem
from ..models.firewall_rule_ipprotocol import FirewallRuleIpprotocol
from ..models.firewall_rule_protocol import FirewallRuleProtocol
from ..models.firewall_rule_statetype import FirewallRuleStatetype
from ..models.firewall_rule_tcp_flags_out_of_type_0_item import FirewallRuleTcpFlagsOutOfType0Item
from ..models.firewall_rule_tcp_flags_set_type_0_item import FirewallRuleTcpFlagsSetType0Item
from ..models.firewall_rule_type import FirewallRuleType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutFirewallRulesEndpointJsonBodyItem")


@_attrs_define
class PutFirewallRulesEndpointJsonBodyItem:
    """
    Attributes:
        type_ (FirewallRuleType): The action to take against traffic that matches this rule.<br>
        interface (list[str]): The interface where packets must originate to match this rule.<br>
        ipprotocol (FirewallRuleIpprotocol): The IP version(s) this rule applies to.<br>
        source (str): The source address this rule applies to. Valid value options are: an existing interface, an IP
            address, a subnet CIDR, an existing alias, `any`, `(self)`, `l2tp`, `pppoe`. The context of this address can be
            inverted by prefixing the value with `!`. For interface values, the `:ip`  modifier can be appended to the value
            to use the interface's IP address instead of its entire subnet.<br>
        destination (str): The destination address this rule applies to. Valid value options are: an existing interface,
            an IP address, a subnet CIDR, an existing alias, `any`, `(self)`, `l2tp`, `pppoe`. The context of this address
            can be inverted by prefixing the value with `!`. For interface values, the `:ip`  modifier can be appended to
            the value to use the interface's IP address instead of its entire subnet.<br>
        protocol (FirewallRuleProtocol | Unset): The IP/transport protocol this rule should match.<br>
        icmptype (list[FirewallRuleIcmptypeItem] | Unset): Th ICMP subtypes this rule applies to. This field is only
            applicable when `ipprotocol` is `inet` and `protocol` is `icmp`.<br><br>This field is only available when the
            following conditions are met:<br>- `protocol` must be equal to `'icmp'`<br>
        source_port (None | str | Unset): The source port this rule applies to. Set to `null` to allow any source port.
            Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by `:`, an existing port type firewall
            alias<br><br>This field is only available when the following conditions are met:<br>- `protocol` must be one of
            [ tcp, udp, tcp/udp ]<br>
        destination_port (None | str | Unset): The destination port this rule applies to. Set to `null` to allow any
            destination port. Valid options are: a TCP/UDP port number, a TCP/UDP port range separated by `:`, an existing
            port type firewall alias<br><br>This field is only available when the following conditions are met:<br>-
            `protocol` must be one of [ tcp, udp, tcp/udp ]<br>
        descr (str | Unset): A description detailing the purpose or justification of this firewall rule.<br>
        disabled (bool | Unset): Enable or disable this firewall rule.<br>
        log (bool | Unset): Enable or disable logging of traffic that matches this rule.<br>
        tag (str | Unset): A packet matching this rule can be marked and this mark used to match on other NAT/filter
            rules. It is called <br>
        statetype (FirewallRuleStatetype | Unset): The state mechanism to use for this firewall rule.<br> Default:
            FirewallRuleStatetype.KEEP_STATE.
        tcp_flags_any (bool | Unset): Allow any TCP flags.<br>
        tcp_flags_out_of (list[FirewallRuleTcpFlagsOutOfType0Item] | None | Unset): The TCP flags that can be set for
            this rule to match.<br><br>This field is only available when the following conditions are met:<br>-
            `tcp_flags_any` must be equal to `false`<br>
        tcp_flags_set (list[FirewallRuleTcpFlagsSetType0Item] | None | Unset): The TCP flags that must be set for this
            rule to match.<br><br>This field is only available when the following conditions are met:<br>- `tcp_flags_any`
            must be equal to `false`<br>
        gateway (None | str | Unset): The gateway traffic matching this rule will be routed to. Set to `null` to use
            default.<br>
        sched (None | str | Unset): The name of an existing firewall schedule to assign to this firewall rule.<br>
        dnpipe (None | str | Unset): The name of the traffic shaper limiter pipe or queue to use for incoming
            traffic.<br>
        pdnpipe (None | str | Unset): The name of the traffic shaper limiter pipe or queue to use for outgoing
            traffic.<br>
        defaultqueue (None | str | Unset): The name of the traffic shaper queue to assume as the default queue for
            traffic matching this rule.<br>
        ackqueue (None | str | Unset): The name of the traffic shaper queue to assume as the ACK queue for ACK traffic
            matching this rule.<br>
        floating (bool | Unset): Mark this rule as a floating firewall rule.<br>
        quick (bool | Unset): Apply this action to traffic that matches this rule immediately. This field only applies
            to floating firewall rules.<br><br>This field is only available when the following conditions are met:<br>-
            `floating` must be equal to `true`<br>
        direction (FirewallRuleDirection | Unset): The direction of traffic this firewall rule applies to. This field
            only applies to floating firewall rules.<br><br>This field is only available when the following conditions are
            met:<br>- `floating` must be equal to `true`<br> Default: FirewallRuleDirection.ANY.
        tracker (int | None | Unset): The internal tracking ID for this firewall rule.<br>
        associated_rule_id (None | str | Unset): The internal rule ID for the NAT rule associated with this rule.<br>
        created_time (int | None | Unset): The unix timestamp of when this firewall rule was original created.<br>
        created_by (None | str | Unset): The username and IP of the user who originally created this firewall rule.<br>
            Default: '@unknown IP (API)'.
        updated_time (int | None | Unset): The unix timestamp of when this firewall rule was original created.<br>
        updated_by (None | str | Unset): The username and IP of the user who last updated this firewall rule.<br>
            Default: '@unknown IP (API)'.
    """

    type_: FirewallRuleType
    interface: list[str]
    ipprotocol: FirewallRuleIpprotocol
    source: str
    destination: str
    protocol: FirewallRuleProtocol | Unset = UNSET
    icmptype: list[FirewallRuleIcmptypeItem] | Unset = UNSET
    source_port: None | str | Unset = UNSET
    destination_port: None | str | Unset = UNSET
    descr: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    log: bool | Unset = UNSET
    tag: str | Unset = UNSET
    statetype: FirewallRuleStatetype | Unset = FirewallRuleStatetype.KEEP_STATE
    tcp_flags_any: bool | Unset = UNSET
    tcp_flags_out_of: list[FirewallRuleTcpFlagsOutOfType0Item] | None | Unset = UNSET
    tcp_flags_set: list[FirewallRuleTcpFlagsSetType0Item] | None | Unset = UNSET
    gateway: None | str | Unset = UNSET
    sched: None | str | Unset = UNSET
    dnpipe: None | str | Unset = UNSET
    pdnpipe: None | str | Unset = UNSET
    defaultqueue: None | str | Unset = UNSET
    ackqueue: None | str | Unset = UNSET
    floating: bool | Unset = UNSET
    quick: bool | Unset = UNSET
    direction: FirewallRuleDirection | Unset = FirewallRuleDirection.ANY
    tracker: int | None | Unset = UNSET
    associated_rule_id: None | str | Unset = UNSET
    created_time: int | None | Unset = UNSET
    created_by: None | str | Unset = "@unknown IP (API)"
    updated_time: int | None | Unset = UNSET
    updated_by: None | str | Unset = "@unknown IP (API)"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        interface = self.interface

        ipprotocol = self.ipprotocol.value

        source = self.source

        destination = self.destination

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        icmptype: list[str] | Unset = UNSET
        if not isinstance(self.icmptype, Unset):
            icmptype = []
            for icmptype_item_data in self.icmptype:
                icmptype_item = icmptype_item_data.value
                icmptype.append(icmptype_item)

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

        descr = self.descr

        disabled = self.disabled

        log = self.log

        tag = self.tag

        statetype: str | Unset = UNSET
        if not isinstance(self.statetype, Unset):
            statetype = self.statetype.value

        tcp_flags_any = self.tcp_flags_any

        tcp_flags_out_of: list[str] | None | Unset
        if isinstance(self.tcp_flags_out_of, Unset):
            tcp_flags_out_of = UNSET
        elif isinstance(self.tcp_flags_out_of, list):
            tcp_flags_out_of = []
            for tcp_flags_out_of_type_0_item_data in self.tcp_flags_out_of:
                tcp_flags_out_of_type_0_item = tcp_flags_out_of_type_0_item_data.value
                tcp_flags_out_of.append(tcp_flags_out_of_type_0_item)

        else:
            tcp_flags_out_of = self.tcp_flags_out_of

        tcp_flags_set: list[str] | None | Unset
        if isinstance(self.tcp_flags_set, Unset):
            tcp_flags_set = UNSET
        elif isinstance(self.tcp_flags_set, list):
            tcp_flags_set = []
            for tcp_flags_set_type_0_item_data in self.tcp_flags_set:
                tcp_flags_set_type_0_item = tcp_flags_set_type_0_item_data.value
                tcp_flags_set.append(tcp_flags_set_type_0_item)

        else:
            tcp_flags_set = self.tcp_flags_set

        gateway: None | str | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        else:
            gateway = self.gateway

        sched: None | str | Unset
        if isinstance(self.sched, Unset):
            sched = UNSET
        else:
            sched = self.sched

        dnpipe: None | str | Unset
        if isinstance(self.dnpipe, Unset):
            dnpipe = UNSET
        else:
            dnpipe = self.dnpipe

        pdnpipe: None | str | Unset
        if isinstance(self.pdnpipe, Unset):
            pdnpipe = UNSET
        else:
            pdnpipe = self.pdnpipe

        defaultqueue: None | str | Unset
        if isinstance(self.defaultqueue, Unset):
            defaultqueue = UNSET
        else:
            defaultqueue = self.defaultqueue

        ackqueue: None | str | Unset
        if isinstance(self.ackqueue, Unset):
            ackqueue = UNSET
        else:
            ackqueue = self.ackqueue

        floating = self.floating

        quick = self.quick

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        tracker: int | None | Unset
        if isinstance(self.tracker, Unset):
            tracker = UNSET
        else:
            tracker = self.tracker

        associated_rule_id: None | str | Unset
        if isinstance(self.associated_rule_id, Unset):
            associated_rule_id = UNSET
        else:
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
                "type": type_,
                "interface": interface,
                "ipprotocol": ipprotocol,
                "source": source,
                "destination": destination,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if icmptype is not UNSET:
            field_dict["icmptype"] = icmptype
        if source_port is not UNSET:
            field_dict["source_port"] = source_port
        if destination_port is not UNSET:
            field_dict["destination_port"] = destination_port
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if log is not UNSET:
            field_dict["log"] = log
        if tag is not UNSET:
            field_dict["tag"] = tag
        if statetype is not UNSET:
            field_dict["statetype"] = statetype
        if tcp_flags_any is not UNSET:
            field_dict["tcp_flags_any"] = tcp_flags_any
        if tcp_flags_out_of is not UNSET:
            field_dict["tcp_flags_out_of"] = tcp_flags_out_of
        if tcp_flags_set is not UNSET:
            field_dict["tcp_flags_set"] = tcp_flags_set
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if sched is not UNSET:
            field_dict["sched"] = sched
        if dnpipe is not UNSET:
            field_dict["dnpipe"] = dnpipe
        if pdnpipe is not UNSET:
            field_dict["pdnpipe"] = pdnpipe
        if defaultqueue is not UNSET:
            field_dict["defaultqueue"] = defaultqueue
        if ackqueue is not UNSET:
            field_dict["ackqueue"] = ackqueue
        if floating is not UNSET:
            field_dict["floating"] = floating
        if quick is not UNSET:
            field_dict["quick"] = quick
        if direction is not UNSET:
            field_dict["direction"] = direction
        if tracker is not UNSET:
            field_dict["tracker"] = tracker
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
        type_ = FirewallRuleType(d.pop("type"))

        interface = cast(list[str], d.pop("interface"))

        ipprotocol = FirewallRuleIpprotocol(d.pop("ipprotocol"))

        source = d.pop("source")

        destination = d.pop("destination")

        _protocol = d.pop("protocol", UNSET)
        protocol: FirewallRuleProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = FirewallRuleProtocol(_protocol)

        _icmptype = d.pop("icmptype", UNSET)
        icmptype: list[FirewallRuleIcmptypeItem] | Unset = UNSET
        if _icmptype is not UNSET:
            icmptype = []
            for icmptype_item_data in _icmptype:
                icmptype_item = FirewallRuleIcmptypeItem(icmptype_item_data)

                icmptype.append(icmptype_item)

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

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        log = d.pop("log", UNSET)

        tag = d.pop("tag", UNSET)

        _statetype = d.pop("statetype", UNSET)
        statetype: FirewallRuleStatetype | Unset
        if isinstance(_statetype, Unset):
            statetype = UNSET
        else:
            statetype = FirewallRuleStatetype(_statetype)

        tcp_flags_any = d.pop("tcp_flags_any", UNSET)

        def _parse_tcp_flags_out_of(data: object) -> list[FirewallRuleTcpFlagsOutOfType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tcp_flags_out_of_type_0 = []
                _tcp_flags_out_of_type_0 = data
                for tcp_flags_out_of_type_0_item_data in _tcp_flags_out_of_type_0:
                    tcp_flags_out_of_type_0_item = FirewallRuleTcpFlagsOutOfType0Item(tcp_flags_out_of_type_0_item_data)

                    tcp_flags_out_of_type_0.append(tcp_flags_out_of_type_0_item)

                return tcp_flags_out_of_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[FirewallRuleTcpFlagsOutOfType0Item] | None | Unset, data)

        tcp_flags_out_of = _parse_tcp_flags_out_of(d.pop("tcp_flags_out_of", UNSET))

        def _parse_tcp_flags_set(data: object) -> list[FirewallRuleTcpFlagsSetType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tcp_flags_set_type_0 = []
                _tcp_flags_set_type_0 = data
                for tcp_flags_set_type_0_item_data in _tcp_flags_set_type_0:
                    tcp_flags_set_type_0_item = FirewallRuleTcpFlagsSetType0Item(tcp_flags_set_type_0_item_data)

                    tcp_flags_set_type_0.append(tcp_flags_set_type_0_item)

                return tcp_flags_set_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[FirewallRuleTcpFlagsSetType0Item] | None | Unset, data)

        tcp_flags_set = _parse_tcp_flags_set(d.pop("tcp_flags_set", UNSET))

        def _parse_gateway(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))

        def _parse_sched(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sched = _parse_sched(d.pop("sched", UNSET))

        def _parse_dnpipe(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dnpipe = _parse_dnpipe(d.pop("dnpipe", UNSET))

        def _parse_pdnpipe(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pdnpipe = _parse_pdnpipe(d.pop("pdnpipe", UNSET))

        def _parse_defaultqueue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        defaultqueue = _parse_defaultqueue(d.pop("defaultqueue", UNSET))

        def _parse_ackqueue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ackqueue = _parse_ackqueue(d.pop("ackqueue", UNSET))

        floating = d.pop("floating", UNSET)

        quick = d.pop("quick", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: FirewallRuleDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = FirewallRuleDirection(_direction)

        def _parse_tracker(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tracker = _parse_tracker(d.pop("tracker", UNSET))

        def _parse_associated_rule_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        associated_rule_id = _parse_associated_rule_id(d.pop("associated_rule_id", UNSET))

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

        put_firewall_rules_endpoint_json_body_item = cls(
            type_=type_,
            interface=interface,
            ipprotocol=ipprotocol,
            source=source,
            destination=destination,
            protocol=protocol,
            icmptype=icmptype,
            source_port=source_port,
            destination_port=destination_port,
            descr=descr,
            disabled=disabled,
            log=log,
            tag=tag,
            statetype=statetype,
            tcp_flags_any=tcp_flags_any,
            tcp_flags_out_of=tcp_flags_out_of,
            tcp_flags_set=tcp_flags_set,
            gateway=gateway,
            sched=sched,
            dnpipe=dnpipe,
            pdnpipe=pdnpipe,
            defaultqueue=defaultqueue,
            ackqueue=ackqueue,
            floating=floating,
            quick=quick,
            direction=direction,
            tracker=tracker,
            associated_rule_id=associated_rule_id,
            created_time=created_time,
            created_by=created_by,
            updated_time=updated_time,
            updated_by=updated_by,
        )

        put_firewall_rules_endpoint_json_body_item.additional_properties = d
        return put_firewall_rules_endpoint_json_body_item

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
