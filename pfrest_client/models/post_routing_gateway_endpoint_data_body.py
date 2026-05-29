from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.routing_gateway_gw_down_kill_states import RoutingGatewayGwDownKillStates
from ..models.routing_gateway_ipprotocol import RoutingGatewayIpprotocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostRoutingGatewayEndpointDataBody")


@_attrs_define
class PostRoutingGatewayEndpointDataBody:
    """
    Attributes:
        name (str): Sets a name for the gateway.<br>
        ipprotocol (RoutingGatewayIpprotocol): Sets the Internet Protocol version this gateway uses.<br>
        interface (str): Sets the interface this gateway will apply to.<br>
        gateway (str): Sets the IP address of the remote gateway.<br>
        descr (str | Unset): Sets a descriptions for the gateway.<br>
        disabled (bool | Unset): Disable this gateway.<br>
        monitor_disable (bool | Unset): Disable gateway monitoring for this gateway.<br>
        monitor (None | str | Unset): Sets a different IP address to use when monitoring this gateway. This is typically
            only
                            necessary if the gateway IP does not accept ICMP probes.<br><br>This field is only available
            when the following conditions are met:<br>- `monitor_disable` must be equal to `false`<br>
        action_disable (bool | Unset): Disable actions from taking place when gateway events occur. The gateway will
            always be
                            considered up.<br>
        force_down (bool | Unset): Always consider this gateway to be up.<br>
        dpinger_dont_add_static_route (bool | Unset): Prevents gateway monitoring from adding a static route for this
            gateway's monitor IP.<br>
        gw_down_kill_states (RoutingGatewayGwDownKillStates | Unset): Controls the state killing behavior when this
            specific gateway goes down. Killing states for specific down gateways only affects states created by policy
            routing rules and reply-to. Has no effect if gateway monitoring or its action are disabled or if the gateway is
            forced down. May not have any effect on dynamic gateways during a link loss event.<br>
        nonlocalgateway (bool | Unset): Allows or disallows gateway IPs that are not a part of the parent interface's
            subnet(s).<br> Default: True.
        weight (int | Unset): Sets the weight for this gateway when used in a Gateway Group.<br> Default: 1.
        data_payload (int | Unset): Sets the data payload to send in ICMP packets to gateway monitor IP.<br> Default: 1.
        latencylow (int | Unset): Sets the threshold to consider latency as low.<br> Default: 200.
        latencyhigh (int | Unset): Sets the threshold to consider latency as high. This value must be greater than
            `latencylow`.<br> Default: 500.
        losslow (int | Unset): Sets the threshold to consider packet loss as low.<br> Default: 10.
        losshigh (int | Unset): Sets the threshold to consider packet loss as high. This value must be greater than
            `losslow`.<br> Default: 20.
        interval (int | Unset): Sets how often ICMP probes will be sent in milliseconds.<br> Default: 500.
        loss_interval (int | Unset): Sets the time interval in milliseconds before packets are treated as lost.<br>
            Default: 2000.
        time_period (int | Unset): Sets the time period in milliseconds over which results are averaged.<br> Default:
            60000.
        alert_interval (int | Unset): Sets the time interval in milliseconds between checking for an alert
            conditions.<br> Default: 1000.
    """

    name: str
    ipprotocol: RoutingGatewayIpprotocol
    interface: str
    gateway: str
    descr: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    monitor_disable: bool | Unset = UNSET
    monitor: None | str | Unset = UNSET
    action_disable: bool | Unset = UNSET
    force_down: bool | Unset = UNSET
    dpinger_dont_add_static_route: bool | Unset = UNSET
    gw_down_kill_states: RoutingGatewayGwDownKillStates | Unset = UNSET
    nonlocalgateway: bool | Unset = True
    weight: int | Unset = 1
    data_payload: int | Unset = 1
    latencylow: int | Unset = 200
    latencyhigh: int | Unset = 500
    losslow: int | Unset = 10
    losshigh: int | Unset = 20
    interval: int | Unset = 500
    loss_interval: int | Unset = 2000
    time_period: int | Unset = 60000
    alert_interval: int | Unset = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ipprotocol = self.ipprotocol.value

        interface = self.interface

        gateway = self.gateway

        descr = self.descr

        disabled = self.disabled

        monitor_disable = self.monitor_disable

        monitor: None | str | Unset
        if isinstance(self.monitor, Unset):
            monitor = UNSET
        else:
            monitor = self.monitor

        action_disable = self.action_disable

        force_down = self.force_down

        dpinger_dont_add_static_route = self.dpinger_dont_add_static_route

        gw_down_kill_states: str | Unset = UNSET
        if not isinstance(self.gw_down_kill_states, Unset):
            gw_down_kill_states = self.gw_down_kill_states.value

        nonlocalgateway = self.nonlocalgateway

        weight = self.weight

        data_payload = self.data_payload

        latencylow = self.latencylow

        latencyhigh = self.latencyhigh

        losslow = self.losslow

        losshigh = self.losshigh

        interval = self.interval

        loss_interval = self.loss_interval

        time_period = self.time_period

        alert_interval = self.alert_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "ipprotocol": ipprotocol,
                "interface": interface,
                "gateway": gateway,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if monitor_disable is not UNSET:
            field_dict["monitor_disable"] = monitor_disable
        if monitor is not UNSET:
            field_dict["monitor"] = monitor
        if action_disable is not UNSET:
            field_dict["action_disable"] = action_disable
        if force_down is not UNSET:
            field_dict["force_down"] = force_down
        if dpinger_dont_add_static_route is not UNSET:
            field_dict["dpinger_dont_add_static_route"] = dpinger_dont_add_static_route
        if gw_down_kill_states is not UNSET:
            field_dict["gw_down_kill_states"] = gw_down_kill_states
        if nonlocalgateway is not UNSET:
            field_dict["nonlocalgateway"] = nonlocalgateway
        if weight is not UNSET:
            field_dict["weight"] = weight
        if data_payload is not UNSET:
            field_dict["data_payload"] = data_payload
        if latencylow is not UNSET:
            field_dict["latencylow"] = latencylow
        if latencyhigh is not UNSET:
            field_dict["latencyhigh"] = latencyhigh
        if losslow is not UNSET:
            field_dict["losslow"] = losslow
        if losshigh is not UNSET:
            field_dict["losshigh"] = losshigh
        if interval is not UNSET:
            field_dict["interval"] = interval
        if loss_interval is not UNSET:
            field_dict["loss_interval"] = loss_interval
        if time_period is not UNSET:
            field_dict["time_period"] = time_period
        if alert_interval is not UNSET:
            field_dict["alert_interval"] = alert_interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        ipprotocol = RoutingGatewayIpprotocol(d.pop("ipprotocol"))

        interface = d.pop("interface")

        gateway = d.pop("gateway")

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        monitor_disable = d.pop("monitor_disable", UNSET)

        def _parse_monitor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monitor = _parse_monitor(d.pop("monitor", UNSET))

        action_disable = d.pop("action_disable", UNSET)

        force_down = d.pop("force_down", UNSET)

        dpinger_dont_add_static_route = d.pop("dpinger_dont_add_static_route", UNSET)

        _gw_down_kill_states = d.pop("gw_down_kill_states", UNSET)
        gw_down_kill_states: RoutingGatewayGwDownKillStates | Unset
        if isinstance(_gw_down_kill_states, Unset):
            gw_down_kill_states = UNSET
        else:
            gw_down_kill_states = RoutingGatewayGwDownKillStates(_gw_down_kill_states)

        nonlocalgateway = d.pop("nonlocalgateway", UNSET)

        weight = d.pop("weight", UNSET)

        data_payload = d.pop("data_payload", UNSET)

        latencylow = d.pop("latencylow", UNSET)

        latencyhigh = d.pop("latencyhigh", UNSET)

        losslow = d.pop("losslow", UNSET)

        losshigh = d.pop("losshigh", UNSET)

        interval = d.pop("interval", UNSET)

        loss_interval = d.pop("loss_interval", UNSET)

        time_period = d.pop("time_period", UNSET)

        alert_interval = d.pop("alert_interval", UNSET)

        post_routing_gateway_endpoint_data_body = cls(
            name=name,
            ipprotocol=ipprotocol,
            interface=interface,
            gateway=gateway,
            descr=descr,
            disabled=disabled,
            monitor_disable=monitor_disable,
            monitor=monitor,
            action_disable=action_disable,
            force_down=force_down,
            dpinger_dont_add_static_route=dpinger_dont_add_static_route,
            gw_down_kill_states=gw_down_kill_states,
            nonlocalgateway=nonlocalgateway,
            weight=weight,
            data_payload=data_payload,
            latencylow=latencylow,
            latencyhigh=latencyhigh,
            losslow=losslow,
            losshigh=losshigh,
            interval=interval,
            loss_interval=loss_interval,
            time_period=time_period,
            alert_interval=alert_interval,
        )

        post_routing_gateway_endpoint_data_body.additional_properties = d
        return post_routing_gateway_endpoint_data_body

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
