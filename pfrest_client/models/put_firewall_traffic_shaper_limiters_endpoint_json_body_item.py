from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.traffic_shaper_limiter_aqm import TrafficShaperLimiterAqm
from ..models.traffic_shaper_limiter_mask import TrafficShaperLimiterMask
from ..models.traffic_shaper_limiter_sched import TrafficShaperLimiterSched
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.traffic_shaper_limiter_bandwidth_item import TrafficShaperLimiterBandwidthItem
    from ..models.traffic_shaper_limiter_queue_item import TrafficShaperLimiterQueueItem


T = TypeVar("T", bound="PutFirewallTrafficShaperLimitersEndpointJsonBodyItem")


@_attrs_define
class PutFirewallTrafficShaperLimitersEndpointJsonBodyItem:
    """
    Attributes:
        name (str): The unique name for this limiter.<br>
        aqm (TrafficShaperLimiterAqm): The Active Queue Management (AQM) algorithm to use for this limiter. AQM is the
            intelligent drop of network packets inside the limiter, when it becomes full or gets close to becoming full,
            with the goal of reducing network congestion.<br>
        sched (TrafficShaperLimiterSched): The scheduler to use for this limiter. The scheduler manages the sequence of
            network packets in the limiter's queue.<br>
        number (int | None | Unset): A unique number auto-assigned to this limiter. This is only used internally by the
            system and cannot be manually set or changed.<br> Default: 1.
        enabled (bool | Unset): Enables or disables this limiter and its child queues.<br>
        mask (TrafficShaperLimiterMask | Unset): If `source` or `destination` slots is chosen a dynamic pipe with the
            bandwidth, delay, packet loss and queue size given above will be created for each source/destination IP address
            encountered, respectively. This makes it possible to easily specify bandwidth limits per host or subnet.<br>
            Default: TrafficShaperLimiterMask.NONE.
        maskbits (int | Unset): The IPv4 mask bits to use when determine the scope of the dynamic pipe for IPv4
            traffic.<br><br>This field is only available when the following conditions are met:<br>- `mask` must be one of [
            srcaddress, dstaddress ]<br> Default: 32.
        maskbitsv6 (int | Unset): The IPv6 mask bits to use when determine the scope of the dynamic pipe for IPv4
            traffic.<br><br>This field is only available when the following conditions are met:<br>- `mask` must be one of [
            srcaddress, dstaddress ]<br> Default: 128.
        qlimit (int | None | Unset): The length of the limiter's queue which the scheduler and AQM are responsible for.
            Set to `null` to assume default.<br>
        ecn (bool | Unset): Enable or disable ECN. ECN sets a reserved TCP flag when the queue is nearing or exceeding
            capacity. Not all AQMs or schedulers support this.<br><br>This field is only available when the following
            conditions are met:<br>- `aqm` must be one of [ codel, pie, red, gred ]<br>- `sched` must be one of [ fq_codel,
            fq_pie ]<br>
        description (str | Unset): The verbose description for this limiter.<br>
        param_codel_target (int | Unset): The value for the CoDel target parameter.<br><br>This field is only available
            when the following conditions are met:<br>- `aqm` must be equal to `'codel'`<br>
        param_codel_interval (int | Unset): The value for the CoDel interval parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `aqm` must be equal to `'codel'`<br>
        param_pie_target (int | Unset): The value for the PIE target parameter.<br><br>This field is only available when
            the following conditions are met:<br>- `aqm` must be equal to `'pie'`<br>
        param_pie_tupdate (int | Unset): The value for the PIE tupdate parameter.<br><br>This field is only available
            when the following conditions are met:<br>- `aqm` must be equal to `'pie'`<br>
        param_pie_alpha (int | Unset): The value for the PIE alpha parameter.<br><br>This field is only available when
            the following conditions are met:<br>- `aqm` must be equal to `'pie'`<br>
        param_pie_beta (int | Unset): The value for the PIE beta parameter.<br><br>This field is only available when the
            following conditions are met:<br>- `aqm` must be equal to `'pie'`<br>
        param_pie_max_burst (int | Unset): The value for the PIE max_burst parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `aqm` must be equal to `'pie'`<br>
        param_pie_max_ecnth (int | Unset): The value for the PIE ecnth parameter.<br><br>This field is only available
            when the following conditions are met:<br>- `aqm` must be equal to `'pie'`<br>
        pie_onoff (bool | Unset): Enable or disable turning PIE on and off depending on queue load.<br><br>This field is
            only available when the following conditions are met:<br>- `aqm` must be equal to `'pie'`<br>
        pie_capdrop (bool | Unset): Enable or disable cap drop adjustment.<br><br>This field is only available when the
            following conditions are met:<br>- `aqm` must be equal to `'pie'`<br>
        pie_qdelay (bool | Unset): Set queue delay type to timestamps (true) or departure rate estimation
            (false).<br><br>This field is only available when the following conditions are met:<br>- `aqm` must be equal to
            `'pie'`<br>
        pie_pderand (bool | Unset): Enable or disable drop probability de-randomisation.<br><br>This field is only
            available when the following conditions are met:<br>- `aqm` must be equal to `'pie'`<br>
        param_red_w_q (int | Unset): The value for the RED w_q parameter.<br><br>This field is only available when the
            following conditions are met:<br>- `aqm` must be equal to `'red'`<br> Default: 1.
        param_red_min_th (int | Unset): The value for the RED min_th parameter.<br><br>This field is only available when
            the following conditions are met:<br>- `aqm` must be equal to `'red'`<br>
        param_red_max_th (int | Unset): The value for the RED max_th parameter.<br><br>This field is only available when
            the following conditions are met:<br>- `aqm` must be equal to `'red'`<br> Default: 1.
        param_red_max_p (int | Unset): The value for the RED max_p parameter.<br><br>This field is only available when
            the following conditions are met:<br>- `aqm` must be equal to `'red'`<br> Default: 1.
        param_gred_w_q (int | Unset): The value for the GRED w_q parameter.<br><br>This field is only available when the
            following conditions are met:<br>- `aqm` must be equal to `'gred'`<br> Default: 1.
        param_gred_min_th (int | Unset): The value for the GRED min_th parameter.<br><br>This field is only available
            when the following conditions are met:<br>- `aqm` must be equal to `'gred'`<br>
        param_gred_max_th (int | Unset): The value for the GRED max_th parameter.<br><br>This field is only available
            when the following conditions are met:<br>- `aqm` must be equal to `'gred'`<br> Default: 1.
        param_gred_max_p (int | Unset): The value for the GRED max_p parameter.<br><br>This field is only available when
            the following conditions are met:<br>- `aqm` must be equal to `'gred'`<br> Default: 1.
        param_fq_codel_target (int | Unset): The value for the FQ CoDel target parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_codel'`<br>
        param_fq_codel_interval (int | Unset): The value for the FQ CoDel interval parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_codel'`<br>
        param_fq_codel_quantum (int | None | Unset): The value for the FQ CoDel quantum parameter.<br><br>This field is
            only available when the following conditions are met:<br>- `sched` must be equal to `'fq_codel'`<br>
        param_fq_codel_limit (int | None | Unset): The value for the FQ CoDel limit parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_codel'`<br>
        param_fq_codel_flows (int | None | Unset): The value for the FQ CoDel flows parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_codel'`<br>
        param_fq_pie_target (int | Unset): The value for the FQ PIE target parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_pie'`<br>
        param_fq_pie_tupdate (int | Unset): The value for the FQ PIE tupdate parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_pie'`<br>
        param_fq_pie_alpha (int | Unset): The value for the FQ PIE alpha parameter.<br><br>This field is only available
            when the following conditions are met:<br>- `sched` must be equal to `'fq_pie'`<br>
        param_fq_pie_beta (int | Unset): The value for the FQ PIE beta parameter.<br><br>This field is only available
            when the following conditions are met:<br>- `sched` must be equal to `'fq_pie'`<br>
        param_fq_pie_max_burst (int | Unset): The value for the FQ PIE max_burst parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_pie'`<br>
        param_fq_pie_max_ecnth (int | Unset): The value for the FQ PIE ecnth parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_pie'`<br>
        param_fq_pie_quantum (int | None | Unset): The value for the FQ PIE quantum parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_pie'`<br>
        param_fq_pie_limit (int | None | Unset): The value for the FQ PIE limit parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_pie'`<br>
        param_fq_pie_flows (int | None | Unset): The value for the FQ PIE flows parameter.<br><br>This field is only
            available when the following conditions are met:<br>- `sched` must be equal to `'fq_pie'`<br>
        delay (int | None | Unset): The amount of delay (in milliseconds) added to traffic passing through this
            limiter.<br>
        plr (float | None | Unset): The amount of packet loss (in percentage) added to traffic passing through the
            limiter.<br>
        buckets (int | None | Unset): The limiter's bucket size (slots).<br>
        bandwidth (list[TrafficShaperLimiterBandwidthItem] | Unset): The bandwidth profiles for this limiter.<br>
        queue (list[TrafficShaperLimiterQueueItem] | Unset): The child queues for this limiter.<br>
    """

    name: str
    aqm: TrafficShaperLimiterAqm
    sched: TrafficShaperLimiterSched
    number: int | None | Unset = 1
    enabled: bool | Unset = UNSET
    mask: TrafficShaperLimiterMask | Unset = TrafficShaperLimiterMask.NONE
    maskbits: int | Unset = 32
    maskbitsv6: int | Unset = 128
    qlimit: int | None | Unset = UNSET
    ecn: bool | Unset = UNSET
    description: str | Unset = UNSET
    param_codel_target: int | Unset = UNSET
    param_codel_interval: int | Unset = UNSET
    param_pie_target: int | Unset = UNSET
    param_pie_tupdate: int | Unset = UNSET
    param_pie_alpha: int | Unset = UNSET
    param_pie_beta: int | Unset = UNSET
    param_pie_max_burst: int | Unset = UNSET
    param_pie_max_ecnth: int | Unset = UNSET
    pie_onoff: bool | Unset = UNSET
    pie_capdrop: bool | Unset = UNSET
    pie_qdelay: bool | Unset = UNSET
    pie_pderand: bool | Unset = UNSET
    param_red_w_q: int | Unset = 1
    param_red_min_th: int | Unset = UNSET
    param_red_max_th: int | Unset = 1
    param_red_max_p: int | Unset = 1
    param_gred_w_q: int | Unset = 1
    param_gred_min_th: int | Unset = UNSET
    param_gred_max_th: int | Unset = 1
    param_gred_max_p: int | Unset = 1
    param_fq_codel_target: int | Unset = UNSET
    param_fq_codel_interval: int | Unset = UNSET
    param_fq_codel_quantum: int | None | Unset = UNSET
    param_fq_codel_limit: int | None | Unset = UNSET
    param_fq_codel_flows: int | None | Unset = UNSET
    param_fq_pie_target: int | Unset = UNSET
    param_fq_pie_tupdate: int | Unset = UNSET
    param_fq_pie_alpha: int | Unset = UNSET
    param_fq_pie_beta: int | Unset = UNSET
    param_fq_pie_max_burst: int | Unset = UNSET
    param_fq_pie_max_ecnth: int | Unset = UNSET
    param_fq_pie_quantum: int | None | Unset = UNSET
    param_fq_pie_limit: int | None | Unset = UNSET
    param_fq_pie_flows: int | None | Unset = UNSET
    delay: int | None | Unset = UNSET
    plr: float | None | Unset = UNSET
    buckets: int | None | Unset = UNSET
    bandwidth: list[TrafficShaperLimiterBandwidthItem] | Unset = UNSET
    queue: list[TrafficShaperLimiterQueueItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        aqm = self.aqm.value

        sched = self.sched.value

        number: int | None | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        enabled = self.enabled

        mask: str | Unset = UNSET
        if not isinstance(self.mask, Unset):
            mask = self.mask.value

        maskbits = self.maskbits

        maskbitsv6 = self.maskbitsv6

        qlimit: int | None | Unset
        if isinstance(self.qlimit, Unset):
            qlimit = UNSET
        else:
            qlimit = self.qlimit

        ecn = self.ecn

        description = self.description

        param_codel_target = self.param_codel_target

        param_codel_interval = self.param_codel_interval

        param_pie_target = self.param_pie_target

        param_pie_tupdate = self.param_pie_tupdate

        param_pie_alpha = self.param_pie_alpha

        param_pie_beta = self.param_pie_beta

        param_pie_max_burst = self.param_pie_max_burst

        param_pie_max_ecnth = self.param_pie_max_ecnth

        pie_onoff = self.pie_onoff

        pie_capdrop = self.pie_capdrop

        pie_qdelay = self.pie_qdelay

        pie_pderand = self.pie_pderand

        param_red_w_q = self.param_red_w_q

        param_red_min_th = self.param_red_min_th

        param_red_max_th = self.param_red_max_th

        param_red_max_p = self.param_red_max_p

        param_gred_w_q = self.param_gred_w_q

        param_gred_min_th = self.param_gred_min_th

        param_gred_max_th = self.param_gred_max_th

        param_gred_max_p = self.param_gred_max_p

        param_fq_codel_target = self.param_fq_codel_target

        param_fq_codel_interval = self.param_fq_codel_interval

        param_fq_codel_quantum: int | None | Unset
        if isinstance(self.param_fq_codel_quantum, Unset):
            param_fq_codel_quantum = UNSET
        else:
            param_fq_codel_quantum = self.param_fq_codel_quantum

        param_fq_codel_limit: int | None | Unset
        if isinstance(self.param_fq_codel_limit, Unset):
            param_fq_codel_limit = UNSET
        else:
            param_fq_codel_limit = self.param_fq_codel_limit

        param_fq_codel_flows: int | None | Unset
        if isinstance(self.param_fq_codel_flows, Unset):
            param_fq_codel_flows = UNSET
        else:
            param_fq_codel_flows = self.param_fq_codel_flows

        param_fq_pie_target = self.param_fq_pie_target

        param_fq_pie_tupdate = self.param_fq_pie_tupdate

        param_fq_pie_alpha = self.param_fq_pie_alpha

        param_fq_pie_beta = self.param_fq_pie_beta

        param_fq_pie_max_burst = self.param_fq_pie_max_burst

        param_fq_pie_max_ecnth = self.param_fq_pie_max_ecnth

        param_fq_pie_quantum: int | None | Unset
        if isinstance(self.param_fq_pie_quantum, Unset):
            param_fq_pie_quantum = UNSET
        else:
            param_fq_pie_quantum = self.param_fq_pie_quantum

        param_fq_pie_limit: int | None | Unset
        if isinstance(self.param_fq_pie_limit, Unset):
            param_fq_pie_limit = UNSET
        else:
            param_fq_pie_limit = self.param_fq_pie_limit

        param_fq_pie_flows: int | None | Unset
        if isinstance(self.param_fq_pie_flows, Unset):
            param_fq_pie_flows = UNSET
        else:
            param_fq_pie_flows = self.param_fq_pie_flows

        delay: int | None | Unset
        if isinstance(self.delay, Unset):
            delay = UNSET
        else:
            delay = self.delay

        plr: float | None | Unset
        if isinstance(self.plr, Unset):
            plr = UNSET
        else:
            plr = self.plr

        buckets: int | None | Unset
        if isinstance(self.buckets, Unset):
            buckets = UNSET
        else:
            buckets = self.buckets

        bandwidth: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bandwidth, Unset):
            bandwidth = []
            for bandwidth_item_data in self.bandwidth:
                bandwidth_item = bandwidth_item_data.to_dict()
                bandwidth.append(bandwidth_item)

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
                "name": name,
                "aqm": aqm,
                "sched": sched,
            }
        )
        if number is not UNSET:
            field_dict["number"] = number
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if mask is not UNSET:
            field_dict["mask"] = mask
        if maskbits is not UNSET:
            field_dict["maskbits"] = maskbits
        if maskbitsv6 is not UNSET:
            field_dict["maskbitsv6"] = maskbitsv6
        if qlimit is not UNSET:
            field_dict["qlimit"] = qlimit
        if ecn is not UNSET:
            field_dict["ecn"] = ecn
        if description is not UNSET:
            field_dict["description"] = description
        if param_codel_target is not UNSET:
            field_dict["param_codel_target"] = param_codel_target
        if param_codel_interval is not UNSET:
            field_dict["param_codel_interval"] = param_codel_interval
        if param_pie_target is not UNSET:
            field_dict["param_pie_target"] = param_pie_target
        if param_pie_tupdate is not UNSET:
            field_dict["param_pie_tupdate"] = param_pie_tupdate
        if param_pie_alpha is not UNSET:
            field_dict["param_pie_alpha"] = param_pie_alpha
        if param_pie_beta is not UNSET:
            field_dict["param_pie_beta"] = param_pie_beta
        if param_pie_max_burst is not UNSET:
            field_dict["param_pie_max_burst"] = param_pie_max_burst
        if param_pie_max_ecnth is not UNSET:
            field_dict["param_pie_max_ecnth"] = param_pie_max_ecnth
        if pie_onoff is not UNSET:
            field_dict["pie_onoff"] = pie_onoff
        if pie_capdrop is not UNSET:
            field_dict["pie_capdrop"] = pie_capdrop
        if pie_qdelay is not UNSET:
            field_dict["pie_qdelay"] = pie_qdelay
        if pie_pderand is not UNSET:
            field_dict["pie_pderand"] = pie_pderand
        if param_red_w_q is not UNSET:
            field_dict["param_red_w_q"] = param_red_w_q
        if param_red_min_th is not UNSET:
            field_dict["param_red_min_th"] = param_red_min_th
        if param_red_max_th is not UNSET:
            field_dict["param_red_max_th"] = param_red_max_th
        if param_red_max_p is not UNSET:
            field_dict["param_red_max_p"] = param_red_max_p
        if param_gred_w_q is not UNSET:
            field_dict["param_gred_w_q"] = param_gred_w_q
        if param_gred_min_th is not UNSET:
            field_dict["param_gred_min_th"] = param_gred_min_th
        if param_gred_max_th is not UNSET:
            field_dict["param_gred_max_th"] = param_gred_max_th
        if param_gred_max_p is not UNSET:
            field_dict["param_gred_max_p"] = param_gred_max_p
        if param_fq_codel_target is not UNSET:
            field_dict["param_fq_codel_target"] = param_fq_codel_target
        if param_fq_codel_interval is not UNSET:
            field_dict["param_fq_codel_interval"] = param_fq_codel_interval
        if param_fq_codel_quantum is not UNSET:
            field_dict["param_fq_codel_quantum"] = param_fq_codel_quantum
        if param_fq_codel_limit is not UNSET:
            field_dict["param_fq_codel_limit"] = param_fq_codel_limit
        if param_fq_codel_flows is not UNSET:
            field_dict["param_fq_codel_flows"] = param_fq_codel_flows
        if param_fq_pie_target is not UNSET:
            field_dict["param_fq_pie_target"] = param_fq_pie_target
        if param_fq_pie_tupdate is not UNSET:
            field_dict["param_fq_pie_tupdate"] = param_fq_pie_tupdate
        if param_fq_pie_alpha is not UNSET:
            field_dict["param_fq_pie_alpha"] = param_fq_pie_alpha
        if param_fq_pie_beta is not UNSET:
            field_dict["param_fq_pie_beta"] = param_fq_pie_beta
        if param_fq_pie_max_burst is not UNSET:
            field_dict["param_fq_pie_max_burst"] = param_fq_pie_max_burst
        if param_fq_pie_max_ecnth is not UNSET:
            field_dict["param_fq_pie_max_ecnth"] = param_fq_pie_max_ecnth
        if param_fq_pie_quantum is not UNSET:
            field_dict["param_fq_pie_quantum"] = param_fq_pie_quantum
        if param_fq_pie_limit is not UNSET:
            field_dict["param_fq_pie_limit"] = param_fq_pie_limit
        if param_fq_pie_flows is not UNSET:
            field_dict["param_fq_pie_flows"] = param_fq_pie_flows
        if delay is not UNSET:
            field_dict["delay"] = delay
        if plr is not UNSET:
            field_dict["plr"] = plr
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if bandwidth is not UNSET:
            field_dict["bandwidth"] = bandwidth
        if queue is not UNSET:
            field_dict["queue"] = queue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.traffic_shaper_limiter_bandwidth_item import TrafficShaperLimiterBandwidthItem
        from ..models.traffic_shaper_limiter_queue_item import TrafficShaperLimiterQueueItem

        d = dict(src_dict)
        name = d.pop("name")

        aqm = TrafficShaperLimiterAqm(d.pop("aqm"))

        sched = TrafficShaperLimiterSched(d.pop("sched"))

        def _parse_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number = _parse_number(d.pop("number", UNSET))

        enabled = d.pop("enabled", UNSET)

        _mask = d.pop("mask", UNSET)
        mask: TrafficShaperLimiterMask | Unset
        if isinstance(_mask, Unset):
            mask = UNSET
        else:
            mask = TrafficShaperLimiterMask(_mask)

        maskbits = d.pop("maskbits", UNSET)

        maskbitsv6 = d.pop("maskbitsv6", UNSET)

        def _parse_qlimit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        qlimit = _parse_qlimit(d.pop("qlimit", UNSET))

        ecn = d.pop("ecn", UNSET)

        description = d.pop("description", UNSET)

        param_codel_target = d.pop("param_codel_target", UNSET)

        param_codel_interval = d.pop("param_codel_interval", UNSET)

        param_pie_target = d.pop("param_pie_target", UNSET)

        param_pie_tupdate = d.pop("param_pie_tupdate", UNSET)

        param_pie_alpha = d.pop("param_pie_alpha", UNSET)

        param_pie_beta = d.pop("param_pie_beta", UNSET)

        param_pie_max_burst = d.pop("param_pie_max_burst", UNSET)

        param_pie_max_ecnth = d.pop("param_pie_max_ecnth", UNSET)

        pie_onoff = d.pop("pie_onoff", UNSET)

        pie_capdrop = d.pop("pie_capdrop", UNSET)

        pie_qdelay = d.pop("pie_qdelay", UNSET)

        pie_pderand = d.pop("pie_pderand", UNSET)

        param_red_w_q = d.pop("param_red_w_q", UNSET)

        param_red_min_th = d.pop("param_red_min_th", UNSET)

        param_red_max_th = d.pop("param_red_max_th", UNSET)

        param_red_max_p = d.pop("param_red_max_p", UNSET)

        param_gred_w_q = d.pop("param_gred_w_q", UNSET)

        param_gred_min_th = d.pop("param_gred_min_th", UNSET)

        param_gred_max_th = d.pop("param_gred_max_th", UNSET)

        param_gred_max_p = d.pop("param_gred_max_p", UNSET)

        param_fq_codel_target = d.pop("param_fq_codel_target", UNSET)

        param_fq_codel_interval = d.pop("param_fq_codel_interval", UNSET)

        def _parse_param_fq_codel_quantum(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        param_fq_codel_quantum = _parse_param_fq_codel_quantum(d.pop("param_fq_codel_quantum", UNSET))

        def _parse_param_fq_codel_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        param_fq_codel_limit = _parse_param_fq_codel_limit(d.pop("param_fq_codel_limit", UNSET))

        def _parse_param_fq_codel_flows(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        param_fq_codel_flows = _parse_param_fq_codel_flows(d.pop("param_fq_codel_flows", UNSET))

        param_fq_pie_target = d.pop("param_fq_pie_target", UNSET)

        param_fq_pie_tupdate = d.pop("param_fq_pie_tupdate", UNSET)

        param_fq_pie_alpha = d.pop("param_fq_pie_alpha", UNSET)

        param_fq_pie_beta = d.pop("param_fq_pie_beta", UNSET)

        param_fq_pie_max_burst = d.pop("param_fq_pie_max_burst", UNSET)

        param_fq_pie_max_ecnth = d.pop("param_fq_pie_max_ecnth", UNSET)

        def _parse_param_fq_pie_quantum(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        param_fq_pie_quantum = _parse_param_fq_pie_quantum(d.pop("param_fq_pie_quantum", UNSET))

        def _parse_param_fq_pie_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        param_fq_pie_limit = _parse_param_fq_pie_limit(d.pop("param_fq_pie_limit", UNSET))

        def _parse_param_fq_pie_flows(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        param_fq_pie_flows = _parse_param_fq_pie_flows(d.pop("param_fq_pie_flows", UNSET))

        def _parse_delay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        delay = _parse_delay(d.pop("delay", UNSET))

        def _parse_plr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        plr = _parse_plr(d.pop("plr", UNSET))

        def _parse_buckets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        buckets = _parse_buckets(d.pop("buckets", UNSET))

        _bandwidth = d.pop("bandwidth", UNSET)
        bandwidth: list[TrafficShaperLimiterBandwidthItem] | Unset = UNSET
        if _bandwidth is not UNSET:
            bandwidth = []
            for bandwidth_item_data in _bandwidth:
                bandwidth_item = TrafficShaperLimiterBandwidthItem.from_dict(bandwidth_item_data)

                bandwidth.append(bandwidth_item)

        _queue = d.pop("queue", UNSET)
        queue: list[TrafficShaperLimiterQueueItem] | Unset = UNSET
        if _queue is not UNSET:
            queue = []
            for queue_item_data in _queue:
                queue_item = TrafficShaperLimiterQueueItem.from_dict(queue_item_data)

                queue.append(queue_item)

        put_firewall_traffic_shaper_limiters_endpoint_json_body_item = cls(
            name=name,
            aqm=aqm,
            sched=sched,
            number=number,
            enabled=enabled,
            mask=mask,
            maskbits=maskbits,
            maskbitsv6=maskbitsv6,
            qlimit=qlimit,
            ecn=ecn,
            description=description,
            param_codel_target=param_codel_target,
            param_codel_interval=param_codel_interval,
            param_pie_target=param_pie_target,
            param_pie_tupdate=param_pie_tupdate,
            param_pie_alpha=param_pie_alpha,
            param_pie_beta=param_pie_beta,
            param_pie_max_burst=param_pie_max_burst,
            param_pie_max_ecnth=param_pie_max_ecnth,
            pie_onoff=pie_onoff,
            pie_capdrop=pie_capdrop,
            pie_qdelay=pie_qdelay,
            pie_pderand=pie_pderand,
            param_red_w_q=param_red_w_q,
            param_red_min_th=param_red_min_th,
            param_red_max_th=param_red_max_th,
            param_red_max_p=param_red_max_p,
            param_gred_w_q=param_gred_w_q,
            param_gred_min_th=param_gred_min_th,
            param_gred_max_th=param_gred_max_th,
            param_gred_max_p=param_gred_max_p,
            param_fq_codel_target=param_fq_codel_target,
            param_fq_codel_interval=param_fq_codel_interval,
            param_fq_codel_quantum=param_fq_codel_quantum,
            param_fq_codel_limit=param_fq_codel_limit,
            param_fq_codel_flows=param_fq_codel_flows,
            param_fq_pie_target=param_fq_pie_target,
            param_fq_pie_tupdate=param_fq_pie_tupdate,
            param_fq_pie_alpha=param_fq_pie_alpha,
            param_fq_pie_beta=param_fq_pie_beta,
            param_fq_pie_max_burst=param_fq_pie_max_burst,
            param_fq_pie_max_ecnth=param_fq_pie_max_ecnth,
            param_fq_pie_quantum=param_fq_pie_quantum,
            param_fq_pie_limit=param_fq_pie_limit,
            param_fq_pie_flows=param_fq_pie_flows,
            delay=delay,
            plr=plr,
            buckets=buckets,
            bandwidth=bandwidth,
            queue=queue,
        )

        put_firewall_traffic_shaper_limiters_endpoint_json_body_item.additional_properties = d
        return put_firewall_traffic_shaper_limiters_endpoint_json_body_item

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
