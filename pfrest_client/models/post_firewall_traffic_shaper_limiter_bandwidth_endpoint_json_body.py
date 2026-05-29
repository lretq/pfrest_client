from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.traffic_shaper_limiter_bandwidth_bwscale import TrafficShaperLimiterBandwidthBwscale
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody")


@_attrs_define
class PostFirewallTrafficShaperLimiterBandwidthEndpointJsonBody:
    """
    Attributes:
        bw (int): The amount of bandwidth this profile allows.<br>
        bwscale (TrafficShaperLimiterBandwidthBwscale): The scale factor of the `bw` fields value.<br>
        parent_id (int): The ID of the parent this object is nested under.
        bwsched (str | Unset): The schedule to assign this bandwidth profile. When this firewall schedule is active,
            this bandwidth profile will be used.<br> Default: 'none'.
    """

    bw: int
    bwscale: TrafficShaperLimiterBandwidthBwscale
    parent_id: int
    bwsched: str | Unset = "none"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bw = self.bw

        bwscale = self.bwscale.value

        parent_id = self.parent_id

        bwsched = self.bwsched

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bw": bw,
                "bwscale": bwscale,
                "parent_id": parent_id,
            }
        )
        if bwsched is not UNSET:
            field_dict["bwsched"] = bwsched

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bw = d.pop("bw")

        bwscale = TrafficShaperLimiterBandwidthBwscale(d.pop("bwscale"))

        parent_id = d.pop("parent_id")

        bwsched = d.pop("bwsched", UNSET)

        post_firewall_traffic_shaper_limiter_bandwidth_endpoint_json_body = cls(
            bw=bw,
            bwscale=bwscale,
            parent_id=parent_id,
            bwsched=bwsched,
        )

        post_firewall_traffic_shaper_limiter_bandwidth_endpoint_json_body.additional_properties = d
        return post_firewall_traffic_shaper_limiter_bandwidth_endpoint_json_body

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
