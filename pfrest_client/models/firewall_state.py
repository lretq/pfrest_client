from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallState")


@_attrs_define
class FirewallState:
    """
    Attributes:
        interface (None | str | Unset): The interface that initially received the traffic which registered the
            state.<br>
        protocol (None | str | Unset): The protocol listed in the state.<br>
        direction (None | str | Unset): The direction of traffic listed in the state.<br>
        source (None | str | Unset): The source address listed in the state. Note: Depending on the `protocol`, this
            value may contain the source port as well.<br>
        destination (None | str | Unset): The destination address listed in the state. Note: Depending on the
            `protocol`, this value may contain the destination port as well.<br>
        state (None | str | Unset): The current status of the firewall state.<br>
        age (None | str | Unset): The age of the firewall state in HH:MM:SS format.<br>
        expires_in (None | str | Unset): The amount of time remaining until the state expires in HH:MM:SS format.<br>
        packets_total (int | None | Unset): The total number of packets observed by the state.<br>
        packets_in (int | None | Unset): The total number of inbound packets observed by the state.<br>
        packets_out (int | None | Unset): The total number of outbound packets observed by the state.<br>
        bytes_total (int | None | Unset): The total number of traffic (in bytes) observed by the state.<br>
        bytes_in (int | None | Unset): The total number of inbound traffic (in bytes) observed by the state.<br>
        bytes_out (int | None | Unset): The total number of outbound traffic (in bytes) observed by the state.<br>
    """

    interface: None | str | Unset = UNSET
    protocol: None | str | Unset = UNSET
    direction: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    destination: None | str | Unset = UNSET
    state: None | str | Unset = UNSET
    age: None | str | Unset = UNSET
    expires_in: None | str | Unset = UNSET
    packets_total: int | None | Unset = UNSET
    packets_in: int | None | Unset = UNSET
    packets_out: int | None | Unset = UNSET
    bytes_total: int | None | Unset = UNSET
    bytes_in: int | None | Unset = UNSET
    bytes_out: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface: None | str | Unset
        if isinstance(self.interface, Unset):
            interface = UNSET
        else:
            interface = self.interface

        protocol: None | str | Unset
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        direction: None | str | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        else:
            direction = self.direction

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        destination: None | str | Unset
        if isinstance(self.destination, Unset):
            destination = UNSET
        else:
            destination = self.destination

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        age: None | str | Unset
        if isinstance(self.age, Unset):
            age = UNSET
        else:
            age = self.age

        expires_in: None | str | Unset
        if isinstance(self.expires_in, Unset):
            expires_in = UNSET
        else:
            expires_in = self.expires_in

        packets_total: int | None | Unset
        if isinstance(self.packets_total, Unset):
            packets_total = UNSET
        else:
            packets_total = self.packets_total

        packets_in: int | None | Unset
        if isinstance(self.packets_in, Unset):
            packets_in = UNSET
        else:
            packets_in = self.packets_in

        packets_out: int | None | Unset
        if isinstance(self.packets_out, Unset):
            packets_out = UNSET
        else:
            packets_out = self.packets_out

        bytes_total: int | None | Unset
        if isinstance(self.bytes_total, Unset):
            bytes_total = UNSET
        else:
            bytes_total = self.bytes_total

        bytes_in: int | None | Unset
        if isinstance(self.bytes_in, Unset):
            bytes_in = UNSET
        else:
            bytes_in = self.bytes_in

        bytes_out: int | None | Unset
        if isinstance(self.bytes_out, Unset):
            bytes_out = UNSET
        else:
            bytes_out = self.bytes_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface is not UNSET:
            field_dict["interface"] = interface
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if direction is not UNSET:
            field_dict["direction"] = direction
        if source is not UNSET:
            field_dict["source"] = source
        if destination is not UNSET:
            field_dict["destination"] = destination
        if state is not UNSET:
            field_dict["state"] = state
        if age is not UNSET:
            field_dict["age"] = age
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if packets_total is not UNSET:
            field_dict["packets_total"] = packets_total
        if packets_in is not UNSET:
            field_dict["packets_in"] = packets_in
        if packets_out is not UNSET:
            field_dict["packets_out"] = packets_out
        if bytes_total is not UNSET:
            field_dict["bytes_total"] = bytes_total
        if bytes_in is not UNSET:
            field_dict["bytes_in"] = bytes_in
        if bytes_out is not UNSET:
            field_dict["bytes_out"] = bytes_out

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_interface(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interface = _parse_interface(d.pop("interface", UNSET))

        def _parse_protocol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direction = _parse_direction(d.pop("direction", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_destination(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination = _parse_destination(d.pop("destination", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_age(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        age = _parse_age(d.pop("age", UNSET))

        def _parse_expires_in(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expires_in = _parse_expires_in(d.pop("expires_in", UNSET))

        def _parse_packets_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        packets_total = _parse_packets_total(d.pop("packets_total", UNSET))

        def _parse_packets_in(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        packets_in = _parse_packets_in(d.pop("packets_in", UNSET))

        def _parse_packets_out(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        packets_out = _parse_packets_out(d.pop("packets_out", UNSET))

        def _parse_bytes_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bytes_total = _parse_bytes_total(d.pop("bytes_total", UNSET))

        def _parse_bytes_in(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bytes_in = _parse_bytes_in(d.pop("bytes_in", UNSET))

        def _parse_bytes_out(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bytes_out = _parse_bytes_out(d.pop("bytes_out", UNSET))

        firewall_state = cls(
            interface=interface,
            protocol=protocol,
            direction=direction,
            source=source,
            destination=destination,
            state=state,
            age=age,
            expires_in=expires_in,
            packets_total=packets_total,
            packets_in=packets_in,
            packets_out=packets_out,
            bytes_total=bytes_total,
            bytes_in=bytes_in,
            bytes_out=bytes_out,
        )

        firewall_state.additional_properties = d
        return firewall_state

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
