from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.firewall_schedule_time_range_month_item import FirewallScheduleTimeRangeMonthItem
from ..models.firewall_schedule_time_range_position_type_0_item import FirewallScheduleTimeRangePositionType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostFirewallScheduleTimeRangeEndpointDataBody")


@_attrs_define
class PostFirewallScheduleTimeRangeEndpointDataBody:
    """
    Attributes:
        month (list[FirewallScheduleTimeRangeMonthItem]): The month for each specified `day` value. Each value specified
            must correspond with a `day` field value and must match the order exactly. For example, a `month` value of `[3,
            6]` and a `day` value of `[2, 17]` would evaluate to March 2nd and June 17th respectively.<br><br>This field is
            only available when the following conditions are met:<br>- `position` must be equal to `NULL`<br>
        day (list[int]): The day for each specified `month` value. Each value specified must correspond with a `month`
            field value and must match the order exactly. For example, a `month` value of `[3, 6]` and a `day` value of `[2,
            17]` would evaluate to March 2nd and June 17th respectively.<br><br>This field is only available when the
            following conditions are met:<br>- `position` must be equal to `NULL`<br>
        hour (str): The start time and end time for this time range in 24-hour format (i.e. HH:MM-HH:MM).<br>
        parent_id (int): The ID of the parent this object is nested under.
        position (list[FirewallScheduleTimeRangePositionType0Item] | None | Unset): The day of the week this schedule
            should be active for. Use `1` for every Monday, `2` for every Tuesday, `3` for every Wednesday, `4` for every
            Thursday, `5` for every Friday, `6` for every Saturday, or `7` for every Sunday. If this field has a value
            specified, the `month` and `day` fields will be unavailable.<br>
        rangedescr (str | Unset): A description detailing this firewall schedule time range's purpose.<br>
    """

    month: list[FirewallScheduleTimeRangeMonthItem]
    day: list[int]
    hour: str
    parent_id: int
    position: list[FirewallScheduleTimeRangePositionType0Item] | None | Unset = UNSET
    rangedescr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        month = []
        for month_item_data in self.month:
            month_item = month_item_data.value
            month.append(month_item)

        day = self.day

        hour = self.hour

        parent_id = self.parent_id

        position: list[int] | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, list):
            position = []
            for position_type_0_item_data in self.position:
                position_type_0_item = position_type_0_item_data.value
                position.append(position_type_0_item)

        else:
            position = self.position

        rangedescr = self.rangedescr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "day": day,
                "hour": hour,
                "parent_id": parent_id,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if rangedescr is not UNSET:
            field_dict["rangedescr"] = rangedescr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        month = []
        _month = d.pop("month")
        for month_item_data in _month:
            month_item = FirewallScheduleTimeRangeMonthItem(month_item_data)

            month.append(month_item)

        day = cast(list[int], d.pop("day"))

        hour = d.pop("hour")

        parent_id = d.pop("parent_id")

        def _parse_position(data: object) -> list[FirewallScheduleTimeRangePositionType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                position_type_0 = []
                _position_type_0 = data
                for position_type_0_item_data in _position_type_0:
                    position_type_0_item = FirewallScheduleTimeRangePositionType0Item(position_type_0_item_data)

                    position_type_0.append(position_type_0_item)

                return position_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[FirewallScheduleTimeRangePositionType0Item] | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        rangedescr = d.pop("rangedescr", UNSET)

        post_firewall_schedule_time_range_endpoint_data_body = cls(
            month=month,
            day=day,
            hour=hour,
            parent_id=parent_id,
            position=position,
            rangedescr=rangedescr,
        )

        post_firewall_schedule_time_range_endpoint_data_body.additional_properties = d
        return post_firewall_schedule_time_range_endpoint_data_body

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
