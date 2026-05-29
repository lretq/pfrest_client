from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.traffic_shaper_bandwidthtype import TrafficShaperBandwidthtype
from ..models.traffic_shaper_scheduler import TrafficShaperScheduler
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.traffic_shaper_queue_item import TrafficShaperQueueItem


T = TypeVar("T", bound="PutFirewallTrafficShapersEndpointDataBodyItem")


@_attrs_define
class PutFirewallTrafficShapersEndpointDataBodyItem:
    """
    Attributes:
        interface (str): The interface this traffic shaper will be applied to.<br>
        scheduler (TrafficShaperScheduler): The scheduler type to use for this traffic shaper. Changing this value will
            automatically update any child queues assigned to this traffic shaper.<br>
        bandwidthtype (TrafficShaperBandwidthtype): The scale type of the `bandwidth` field's value.<br>
        bandwidth (int): The total bandwidth amount allowed by this traffic shaper.<br>
        enabled (bool | Unset): Enables or disables this traffic shaper.<br> Default: True.
        name (None | str | Unset): The name of this traffic shaper. This value is automatically set by the system and
            cannot be changed.<br>
        qlimit (int | None | Unset): The number of packets that can be held in a queue waiting to be transmitted by the
            shaper.<br><br>This field is only available when the following conditions are met:<br>- `scheduler` must not be
            one of [ CODELQ ]<br> Default: 50.
        tbrconfig (int | None | Unset): The size, in bytes, of the token bucket regulator. If `null`, heuristics based
            on the interface bandwidth are used to determine the size.<br>
        queue (list[TrafficShaperQueueItem] | Unset): The child queues assigned to this traffic shaper.<br>
    """

    interface: str
    scheduler: TrafficShaperScheduler
    bandwidthtype: TrafficShaperBandwidthtype
    bandwidth: int
    enabled: bool | Unset = True
    name: None | str | Unset = UNSET
    qlimit: int | None | Unset = 50
    tbrconfig: int | None | Unset = UNSET
    queue: list[TrafficShaperQueueItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        scheduler = self.scheduler.value

        bandwidthtype = self.bandwidthtype.value

        bandwidth = self.bandwidth

        enabled = self.enabled

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        qlimit: int | None | Unset
        if isinstance(self.qlimit, Unset):
            qlimit = UNSET
        else:
            qlimit = self.qlimit

        tbrconfig: int | None | Unset
        if isinstance(self.tbrconfig, Unset):
            tbrconfig = UNSET
        else:
            tbrconfig = self.tbrconfig

        queue: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.queue, Unset):
            queue = []
            for queue_item_data in self.queue:
                queue_item = queue_item_data.to_dict()
                queue.append(queue_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interface": interface,
                "scheduler": scheduler,
                "bandwidthtype": bandwidthtype,
                "bandwidth": bandwidth,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if qlimit is not UNSET:
            field_dict["qlimit"] = qlimit
        if tbrconfig is not UNSET:
            field_dict["tbrconfig"] = tbrconfig
        if queue is not UNSET:
            field_dict["queue"] = queue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.traffic_shaper_queue_item import TrafficShaperQueueItem

        d = dict(src_dict)
        interface = d.pop("interface")

        scheduler = TrafficShaperScheduler(d.pop("scheduler"))

        bandwidthtype = TrafficShaperBandwidthtype(d.pop("bandwidthtype"))

        bandwidth = d.pop("bandwidth")

        enabled = d.pop("enabled", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_qlimit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        qlimit = _parse_qlimit(d.pop("qlimit", UNSET))

        def _parse_tbrconfig(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tbrconfig = _parse_tbrconfig(d.pop("tbrconfig", UNSET))

        _queue = d.pop("queue", UNSET)
        queue: list[TrafficShaperQueueItem] | Unset = UNSET
        if _queue is not UNSET:
            queue = []
            for queue_item_data in _queue:
                queue_item = TrafficShaperQueueItem.from_dict(queue_item_data)

                queue.append(queue_item)

        put_firewall_traffic_shapers_endpoint_data_body_item = cls(
            interface=interface,
            scheduler=scheduler,
            bandwidthtype=bandwidthtype,
            bandwidth=bandwidth,
            enabled=enabled,
            name=name,
            qlimit=qlimit,
            tbrconfig=tbrconfig,
            queue=queue,
        )

        put_firewall_traffic_shapers_endpoint_data_body_item.additional_properties = d
        return put_firewall_traffic_shapers_endpoint_data_body_item

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
