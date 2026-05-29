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


T = TypeVar("T", bound="PatchFirewallTrafficShaperEndpointJsonBody")


@_attrs_define
class PatchFirewallTrafficShaperEndpointJsonBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        enabled (bool | Unset): Enables or disables this traffic shaper.<br> Default: True.
        interface (str | Unset): The interface this traffic shaper will be applied to.<br>
        name (None | str | Unset): The name of this traffic shaper. This value is automatically set by the system and
            cannot be changed.<br>
        scheduler (TrafficShaperScheduler | Unset): The scheduler type to use for this traffic shaper. Changing this
            value will automatically update any child queues assigned to this traffic shaper.<br>
        bandwidthtype (TrafficShaperBandwidthtype | Unset): The scale type of the `bandwidth` field's value.<br>
        bandwidth (int | Unset): The total bandwidth amount allowed by this traffic shaper.<br>
        qlimit (int | None | Unset): The number of packets that can be held in a queue waiting to be transmitted by the
            shaper.<br><br>This field is only available when the following conditions are met:<br>- `scheduler` must not be
            one of [ CODELQ ]<br> Default: 50.
        tbrconfig (int | None | Unset): The size, in bytes, of the token bucket regulator. If `null`, heuristics based
            on the interface bandwidth are used to determine the size.<br>
        queue (list[TrafficShaperQueueItem] | Unset): The child queues assigned to this traffic shaper.<br>
    """

    id: int
    enabled: bool | Unset = True
    interface: str | Unset = UNSET
    name: None | str | Unset = UNSET
    scheduler: TrafficShaperScheduler | Unset = UNSET
    bandwidthtype: TrafficShaperBandwidthtype | Unset = UNSET
    bandwidth: int | Unset = UNSET
    qlimit: int | None | Unset = 50
    tbrconfig: int | None | Unset = UNSET
    queue: list[TrafficShaperQueueItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enabled = self.enabled

        interface = self.interface

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        scheduler: str | Unset = UNSET
        if not isinstance(self.scheduler, Unset):
            scheduler = self.scheduler.value

        bandwidthtype: str | Unset = UNSET
        if not isinstance(self.bandwidthtype, Unset):
            bandwidthtype = self.bandwidthtype.value

        bandwidth = self.bandwidth

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
                "id": id,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if interface is not UNSET:
            field_dict["interface"] = interface
        if name is not UNSET:
            field_dict["name"] = name
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if bandwidthtype is not UNSET:
            field_dict["bandwidthtype"] = bandwidthtype
        if bandwidth is not UNSET:
            field_dict["bandwidth"] = bandwidth
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
        id = d.pop("id")

        enabled = d.pop("enabled", UNSET)

        interface = d.pop("interface", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _scheduler = d.pop("scheduler", UNSET)
        scheduler: TrafficShaperScheduler | Unset
        if isinstance(_scheduler, Unset):
            scheduler = UNSET
        else:
            scheduler = TrafficShaperScheduler(_scheduler)

        _bandwidthtype = d.pop("bandwidthtype", UNSET)
        bandwidthtype: TrafficShaperBandwidthtype | Unset
        if isinstance(_bandwidthtype, Unset):
            bandwidthtype = UNSET
        else:
            bandwidthtype = TrafficShaperBandwidthtype(_bandwidthtype)

        bandwidth = d.pop("bandwidth", UNSET)

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

        patch_firewall_traffic_shaper_endpoint_json_body = cls(
            id=id,
            enabled=enabled,
            interface=interface,
            name=name,
            scheduler=scheduler,
            bandwidthtype=bandwidthtype,
            bandwidth=bandwidth,
            qlimit=qlimit,
            tbrconfig=tbrconfig,
            queue=queue,
        )

        patch_firewall_traffic_shaper_endpoint_json_body.additional_properties = d
        return patch_firewall_traffic_shaper_endpoint_json_body

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
