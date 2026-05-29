from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutingGatewayStatus")


@_attrs_define
class RoutingGatewayStatus:
    """
    Attributes:
        name (None | str | Unset): The name of the gateway this status corresponds to.<br>
        srcip (None | str | Unset): The current source IP being used to send monitoring probes to this gateway.<br>
        monitorip (None | str | Unset): The current IP being monitored for this gateway.<br>
        delay (float | None | Unset): The current latency (in milliseconds) for this gateway.<br>
        stddev (float | None | Unset): The standard deviation in latency (in milliseconds) for this gateway.<br>
        loss (float | None | Unset): The current amount of packet loss (in percentage) for this gateway. This uses a
            whole percentage (0.0-100.0).<br>
        status (None | str | Unset): The current status of this gateway. Typically, this will indicate if the gateway is
            consider online or offline.<br>
        substatus (None | str | Unset): The current sub-status of this gateway. Typically, this provide details into
            problems this gateway is seeing such as latency or packet loss.<br>
    """

    name: None | str | Unset = UNSET
    srcip: None | str | Unset = UNSET
    monitorip: None | str | Unset = UNSET
    delay: float | None | Unset = UNSET
    stddev: float | None | Unset = UNSET
    loss: float | None | Unset = UNSET
    status: None | str | Unset = UNSET
    substatus: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        srcip: None | str | Unset
        if isinstance(self.srcip, Unset):
            srcip = UNSET
        else:
            srcip = self.srcip

        monitorip: None | str | Unset
        if isinstance(self.monitorip, Unset):
            monitorip = UNSET
        else:
            monitorip = self.monitorip

        delay: float | None | Unset
        if isinstance(self.delay, Unset):
            delay = UNSET
        else:
            delay = self.delay

        stddev: float | None | Unset
        if isinstance(self.stddev, Unset):
            stddev = UNSET
        else:
            stddev = self.stddev

        loss: float | None | Unset
        if isinstance(self.loss, Unset):
            loss = UNSET
        else:
            loss = self.loss

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        substatus: None | str | Unset
        if isinstance(self.substatus, Unset):
            substatus = UNSET
        else:
            substatus = self.substatus

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if srcip is not UNSET:
            field_dict["srcip"] = srcip
        if monitorip is not UNSET:
            field_dict["monitorip"] = monitorip
        if delay is not UNSET:
            field_dict["delay"] = delay
        if stddev is not UNSET:
            field_dict["stddev"] = stddev
        if loss is not UNSET:
            field_dict["loss"] = loss
        if status is not UNSET:
            field_dict["status"] = status
        if substatus is not UNSET:
            field_dict["substatus"] = substatus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_srcip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        srcip = _parse_srcip(d.pop("srcip", UNSET))

        def _parse_monitorip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monitorip = _parse_monitorip(d.pop("monitorip", UNSET))

        def _parse_delay(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        delay = _parse_delay(d.pop("delay", UNSET))

        def _parse_stddev(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        stddev = _parse_stddev(d.pop("stddev", UNSET))

        def _parse_loss(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        loss = _parse_loss(d.pop("loss", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_substatus(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        substatus = _parse_substatus(d.pop("substatus", UNSET))

        routing_gateway_status = cls(
            name=name,
            srcip=srcip,
            monitorip=monitorip,
            delay=delay,
            stddev=stddev,
            loss=loss,
            status=status,
            substatus=substatus,
        )

        routing_gateway_status.additional_properties = d
        return routing_gateway_status

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
