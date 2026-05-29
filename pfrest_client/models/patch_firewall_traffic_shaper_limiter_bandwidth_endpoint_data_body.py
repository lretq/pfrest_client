from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.traffic_shaper_limiter_bandwidth_bwscale import TrafficShaperLimiterBandwidthBwscale
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody")


@_attrs_define
class PatchFirewallTrafficShaperLimiterBandwidthEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        bw (int | Unset): The amount of bandwidth this profile allows.<br>
        bwscale (TrafficShaperLimiterBandwidthBwscale | Unset): The scale factor of the `bw` fields value.<br>
        bwsched (str | Unset): The schedule to assign this bandwidth profile. When this firewall schedule is active,
            this bandwidth profile will be used.<br> Default: 'none'.
    """

    parent_id: int
    id: int
    bw: int | Unset = UNSET
    bwscale: TrafficShaperLimiterBandwidthBwscale | Unset = UNSET
    bwsched: str | Unset = "none"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        bw = self.bw

        bwscale: str | Unset = UNSET
        if not isinstance(self.bwscale, Unset):
            bwscale = self.bwscale.value

        bwsched = self.bwsched

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if bw is not UNSET:
            field_dict["bw"] = bw
        if bwscale is not UNSET:
            field_dict["bwscale"] = bwscale
        if bwsched is not UNSET:
            field_dict["bwsched"] = bwsched

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        bw = d.pop("bw", UNSET)

        _bwscale = d.pop("bwscale", UNSET)
        bwscale: TrafficShaperLimiterBandwidthBwscale | Unset
        if isinstance(_bwscale, Unset):
            bwscale = UNSET
        else:
            bwscale = TrafficShaperLimiterBandwidthBwscale(_bwscale)

        bwsched = d.pop("bwsched", UNSET)

        patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            bw=bw,
            bwscale=bwscale,
            bwsched=bwsched,
        )

        patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_data_body.additional_properties = d
        return patch_firewall_traffic_shaper_limiter_bandwidth_endpoint_data_body

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
