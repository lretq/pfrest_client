from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.traffic_shaper_queue_bandwidthtype import TrafficShaperQueueBandwidthtype
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFirewallTrafficShaperQueueEndpointDataBody")


@_attrs_define
class PostFirewallTrafficShaperQueueEndpointDataBody:
    """
    Attributes:
        name (str): The name to assign this traffic shaper queue.<br>
        qlimit (int): The number of packets that can be held in a queue waiting to be transmitted by the shaper.<br>
        bandwidth (int): The total bandwidth amount allowed by this traffic shaper.<br><br>This field is only available
            when the following conditions are met:<br>- Parent field `scheduler` must be one of [ FAIRQ, CBQ, HFSC ]<br>
        upperlimit_m2 (str): The normal bandwidth limit for this traffic shaper queue. If `upperlimit_m1` is not
            defined, this limit will always be in effect. If `upperlimit_m1` is defined, this limit will take effect after
            the `upperlimit_d` duration has expired.<br><br>This field is only available when the following conditions are
            met:<br>- `upperlimit` must be equal to `true`<br>
        realtime_m2 (str): The maximum bandwidth this traffic shaper queue is allowed to use. Note: This value should
            not exceed 30% of parent queue's maximum bandwidth.<br><br>This field is only available when the following
            conditions are met:<br>- `realtime` must be equal to `true`<br>
        linkshare_m2 (str): The maximum bandwidth this traffic shaper queue is allowed to use. Note: This behaves
            exactly the same as the `bandwidth` field. If this field is set, it will override whatever value is current
            assigned to the `bandwidth` field.<br><br>This field is only available when the following conditions are
            met:<br>- `linkshare` must be equal to `true`<br>
        parent_id (int): The ID of the parent this object is nested under.
        interface (None | str | Unset): The parent interface this traffic shaper queue a child of. This value is
            automatically determined by the queue's parent and cannot be manually set or changed.<br>
        enabled (bool | Unset): Enables or disables the traffic shaper queue.<br>
        priority (int | Unset): The priority level for this traffic shaper queue.<br><br>This field is only available
            when the following conditions are met:<br>- Parent field `scheduler` must be one of [ FAIRQ, CBQ, PRIQ ]<br>
            Default: 1.
        description (str | Unset): A description for this traffic shaper queue.<br>
        default (bool | Unset): Mark this traffic shaper queue as the default queue.<br>
        red (bool | Unset): Use the 'Random Early Detection' scheduler option for this traffic shaper queue.<br>
        rio (bool | Unset): Use the 'Random Early Detection In and Out' scheduler option for this traffic shaper
            queue.<br>
        ecn (bool | Unset): Use the 'Explicit Congestion Notification' scheduler option for this traffic shaper
            queue.<br>
        codel (bool | Unset): Use the 'Codel Active Queue' scheduler option for this traffic shaper queue.<br>
        bandwidthtype (TrafficShaperQueueBandwidthtype | Unset): The scale type of the `bandwidth` field's
            value.<br><br>This field is only available when the following conditions are met:<br>- Parent field `scheduler`
            must be one of [ FAIRQ, CBQ, HFSC ]<br> Default: TrafficShaperQueueBandwidthtype.MB.
        buckets (int | None | Unset): <br><br>This field is only available when the following conditions are met:<br>-
            Parent field `scheduler` must be equal to `'FAIRQ'`<br>
        hogs (int | None | Unset): The bandwidth limit per host.<br><br>This field is only available when the following
            conditions are met:<br>- Parent field `scheduler` must be equal to `'FAIRQ'`<br>
        borrow (bool | Unset): Allow this queue to borrow from other queues when available.<br><br>This field is only
            available when the following conditions are met:<br>- Parent field `scheduler` must be equal to `'CBQ'`<br>
        upperlimit (bool | Unset): Allow setting the maximum bandwidth allowed for the queue. Will force hard bandwidth
            limiting.<br><br>This field is only available when the following conditions are met:<br>- Parent field
            `scheduler` must be equal to `'HFSC'`<br>
        upperlimit_m1 (None | str | Unset): The burst-able bandwidth limit for this traffic shaper queue.<br><br>This
            field is only available when the following conditions are met:<br>- `upperlimit` must be equal to `true`<br>
        upperlimit_d (int | None | Unset): The duration (in milliseconds) that the burst-able bandwidth limit
            (`upperlimit_m1` is in effect.<br><br>This field is only available when the following conditions are met:<br>-
            `upperlimit` must be equal to `true`<br>
        realtime (bool | Unset): Allow setting the guaranteed bandwidth minimum allotted to the queue.<br><br>This field
            is only available when the following conditions are met:<br>- Parent field `scheduler` must be equal to
            `'HFSC'`<br>
        realtime_m1 (None | str | Unset): The guaranteed minimum bandwidth limit for this traffic shaper queue during
            real time.<br><br>This field is only available when the following conditions are met:<br>- `realtime` must be
            equal to `true`<br>
        realtime_d (int | None | Unset): The duration (in milliseconds) that the guaranteed bandwidth limit
            (`realtime_m1`) is in effect.<br><br>This field is only available when the following conditions are met:<br>-
            `realtime` must be equal to `true`<br>
        linkshare (bool | Unset): Allow sharing bandwidth from this queue for other queues as long as the real time
            values have been satisfied.<br><br>This field is only available when the following conditions are met:<br>-
            Parent field `scheduler` must be equal to `'HFSC'`<br>
        linkshare_m1 (None | str | Unset): The initial bandwidth limit for this traffic shaper queue when link
            sharing.<br><br>This field is only available when the following conditions are met:<br>- `linkshare` must be
            equal to `true`<br>
        linkshare_d (int | None | Unset): The duration (in milliseconds) that the initial bandwidth limit
            (`linkshare_m1`) is in effect.<br><br>This field is only available when the following conditions are met:<br>-
            `linkshare` must be equal to `true`<br>
    """

    name: str
    qlimit: int
    bandwidth: int
    upperlimit_m2: str
    realtime_m2: str
    linkshare_m2: str
    parent_id: int
    interface: None | str | Unset = UNSET
    enabled: bool | Unset = UNSET
    priority: int | Unset = 1
    description: str | Unset = UNSET
    default: bool | Unset = UNSET
    red: bool | Unset = UNSET
    rio: bool | Unset = UNSET
    ecn: bool | Unset = UNSET
    codel: bool | Unset = UNSET
    bandwidthtype: TrafficShaperQueueBandwidthtype | Unset = TrafficShaperQueueBandwidthtype.MB
    buckets: int | None | Unset = UNSET
    hogs: int | None | Unset = UNSET
    borrow: bool | Unset = UNSET
    upperlimit: bool | Unset = UNSET
    upperlimit_m1: None | str | Unset = UNSET
    upperlimit_d: int | None | Unset = UNSET
    realtime: bool | Unset = UNSET
    realtime_m1: None | str | Unset = UNSET
    realtime_d: int | None | Unset = UNSET
    linkshare: bool | Unset = UNSET
    linkshare_m1: None | str | Unset = UNSET
    linkshare_d: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        qlimit = self.qlimit

        bandwidth = self.bandwidth

        upperlimit_m2 = self.upperlimit_m2

        realtime_m2 = self.realtime_m2

        linkshare_m2 = self.linkshare_m2

        parent_id = self.parent_id

        interface: None | str | Unset
        if isinstance(self.interface, Unset):
            interface = UNSET
        else:
            interface = self.interface

        enabled = self.enabled

        priority = self.priority

        description = self.description

        default = self.default

        red = self.red

        rio = self.rio

        ecn = self.ecn

        codel = self.codel

        bandwidthtype: str | Unset = UNSET
        if not isinstance(self.bandwidthtype, Unset):
            bandwidthtype = self.bandwidthtype.value

        buckets: int | None | Unset
        if isinstance(self.buckets, Unset):
            buckets = UNSET
        else:
            buckets = self.buckets

        hogs: int | None | Unset
        if isinstance(self.hogs, Unset):
            hogs = UNSET
        else:
            hogs = self.hogs

        borrow = self.borrow

        upperlimit = self.upperlimit

        upperlimit_m1: None | str | Unset
        if isinstance(self.upperlimit_m1, Unset):
            upperlimit_m1 = UNSET
        else:
            upperlimit_m1 = self.upperlimit_m1

        upperlimit_d: int | None | Unset
        if isinstance(self.upperlimit_d, Unset):
            upperlimit_d = UNSET
        else:
            upperlimit_d = self.upperlimit_d

        realtime = self.realtime

        realtime_m1: None | str | Unset
        if isinstance(self.realtime_m1, Unset):
            realtime_m1 = UNSET
        else:
            realtime_m1 = self.realtime_m1

        realtime_d: int | None | Unset
        if isinstance(self.realtime_d, Unset):
            realtime_d = UNSET
        else:
            realtime_d = self.realtime_d

        linkshare = self.linkshare

        linkshare_m1: None | str | Unset
        if isinstance(self.linkshare_m1, Unset):
            linkshare_m1 = UNSET
        else:
            linkshare_m1 = self.linkshare_m1

        linkshare_d: int | None | Unset
        if isinstance(self.linkshare_d, Unset):
            linkshare_d = UNSET
        else:
            linkshare_d = self.linkshare_d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "qlimit": qlimit,
                "bandwidth": bandwidth,
                "upperlimit_m2": upperlimit_m2,
                "realtime_m2": realtime_m2,
                "linkshare_m2": linkshare_m2,
                "parent_id": parent_id,
            }
        )
        if interface is not UNSET:
            field_dict["interface"] = interface
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if priority is not UNSET:
            field_dict["priority"] = priority
        if description is not UNSET:
            field_dict["description"] = description
        if default is not UNSET:
            field_dict["default"] = default
        if red is not UNSET:
            field_dict["red"] = red
        if rio is not UNSET:
            field_dict["rio"] = rio
        if ecn is not UNSET:
            field_dict["ecn"] = ecn
        if codel is not UNSET:
            field_dict["codel"] = codel
        if bandwidthtype is not UNSET:
            field_dict["bandwidthtype"] = bandwidthtype
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if hogs is not UNSET:
            field_dict["hogs"] = hogs
        if borrow is not UNSET:
            field_dict["borrow"] = borrow
        if upperlimit is not UNSET:
            field_dict["upperlimit"] = upperlimit
        if upperlimit_m1 is not UNSET:
            field_dict["upperlimit_m1"] = upperlimit_m1
        if upperlimit_d is not UNSET:
            field_dict["upperlimit_d"] = upperlimit_d
        if realtime is not UNSET:
            field_dict["realtime"] = realtime
        if realtime_m1 is not UNSET:
            field_dict["realtime_m1"] = realtime_m1
        if realtime_d is not UNSET:
            field_dict["realtime_d"] = realtime_d
        if linkshare is not UNSET:
            field_dict["linkshare"] = linkshare
        if linkshare_m1 is not UNSET:
            field_dict["linkshare_m1"] = linkshare_m1
        if linkshare_d is not UNSET:
            field_dict["linkshare_d"] = linkshare_d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        qlimit = d.pop("qlimit")

        bandwidth = d.pop("bandwidth")

        upperlimit_m2 = d.pop("upperlimit_m2")

        realtime_m2 = d.pop("realtime_m2")

        linkshare_m2 = d.pop("linkshare_m2")

        parent_id = d.pop("parent_id")

        def _parse_interface(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interface = _parse_interface(d.pop("interface", UNSET))

        enabled = d.pop("enabled", UNSET)

        priority = d.pop("priority", UNSET)

        description = d.pop("description", UNSET)

        default = d.pop("default", UNSET)

        red = d.pop("red", UNSET)

        rio = d.pop("rio", UNSET)

        ecn = d.pop("ecn", UNSET)

        codel = d.pop("codel", UNSET)

        _bandwidthtype = d.pop("bandwidthtype", UNSET)
        bandwidthtype: TrafficShaperQueueBandwidthtype | Unset
        if isinstance(_bandwidthtype, Unset):
            bandwidthtype = UNSET
        else:
            bandwidthtype = TrafficShaperQueueBandwidthtype(_bandwidthtype)

        def _parse_buckets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        buckets = _parse_buckets(d.pop("buckets", UNSET))

        def _parse_hogs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hogs = _parse_hogs(d.pop("hogs", UNSET))

        borrow = d.pop("borrow", UNSET)

        upperlimit = d.pop("upperlimit", UNSET)

        def _parse_upperlimit_m1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upperlimit_m1 = _parse_upperlimit_m1(d.pop("upperlimit_m1", UNSET))

        def _parse_upperlimit_d(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        upperlimit_d = _parse_upperlimit_d(d.pop("upperlimit_d", UNSET))

        realtime = d.pop("realtime", UNSET)

        def _parse_realtime_m1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        realtime_m1 = _parse_realtime_m1(d.pop("realtime_m1", UNSET))

        def _parse_realtime_d(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        realtime_d = _parse_realtime_d(d.pop("realtime_d", UNSET))

        linkshare = d.pop("linkshare", UNSET)

        def _parse_linkshare_m1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linkshare_m1 = _parse_linkshare_m1(d.pop("linkshare_m1", UNSET))

        def _parse_linkshare_d(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        linkshare_d = _parse_linkshare_d(d.pop("linkshare_d", UNSET))

        post_firewall_traffic_shaper_queue_endpoint_data_body = cls(
            name=name,
            qlimit=qlimit,
            bandwidth=bandwidth,
            upperlimit_m2=upperlimit_m2,
            realtime_m2=realtime_m2,
            linkshare_m2=linkshare_m2,
            parent_id=parent_id,
            interface=interface,
            enabled=enabled,
            priority=priority,
            description=description,
            default=default,
            red=red,
            rio=rio,
            ecn=ecn,
            codel=codel,
            bandwidthtype=bandwidthtype,
            buckets=buckets,
            hogs=hogs,
            borrow=borrow,
            upperlimit=upperlimit,
            upperlimit_m1=upperlimit_m1,
            upperlimit_d=upperlimit_d,
            realtime=realtime,
            realtime_m1=realtime_m1,
            realtime_d=realtime_d,
            linkshare=linkshare,
            linkshare_m1=linkshare_m1,
            linkshare_d=linkshare_d,
        )

        post_firewall_traffic_shaper_queue_endpoint_data_body.additional_properties = d
        return post_firewall_traffic_shaper_queue_endpoint_data_body

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
