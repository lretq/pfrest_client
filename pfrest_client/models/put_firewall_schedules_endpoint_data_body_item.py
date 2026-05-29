from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_schedule_timerange_item import FirewallScheduleTimerangeItem


T = TypeVar("T", bound="PutFirewallSchedulesEndpointDataBodyItem")


@_attrs_define
class PutFirewallSchedulesEndpointDataBodyItem:
    """
    Attributes:
        name (str): The unique name to assign this schedule.<br>
        timerange (list[FirewallScheduleTimerangeItem]): The date/times this firewall schedule will be active.<br>
        schedlabel (None | str | Unset): A unique ID for this schedule used internally by the system.<br>
        descr (str | Unset): A description of this schedules purpose.<br>
        active (bool | None | Unset): Displays whether the schedule is currently active or not.<br>
    """

    name: str
    timerange: list[FirewallScheduleTimerangeItem]
    schedlabel: None | str | Unset = UNSET
    descr: str | Unset = UNSET
    active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        timerange = []
        for timerange_item_data in self.timerange:
            timerange_item = timerange_item_data.to_dict()
            timerange.append(timerange_item)

        schedlabel: None | str | Unset
        if isinstance(self.schedlabel, Unset):
            schedlabel = UNSET
        else:
            schedlabel = self.schedlabel

        descr = self.descr

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "timerange": timerange,
            }
        )
        if schedlabel is not UNSET:
            field_dict["schedlabel"] = schedlabel
        if descr is not UNSET:
            field_dict["descr"] = descr
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_schedule_timerange_item import FirewallScheduleTimerangeItem

        d = dict(src_dict)
        name = d.pop("name")

        timerange = []
        _timerange = d.pop("timerange")
        for timerange_item_data in _timerange:
            timerange_item = FirewallScheduleTimerangeItem.from_dict(timerange_item_data)

            timerange.append(timerange_item)

        def _parse_schedlabel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schedlabel = _parse_schedlabel(d.pop("schedlabel", UNSET))

        descr = d.pop("descr", UNSET)

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        put_firewall_schedules_endpoint_data_body_item = cls(
            name=name,
            timerange=timerange,
            schedlabel=schedlabel,
            descr=descr,
            active=active,
        )

        put_firewall_schedules_endpoint_data_body_item.additional_properties = d
        return put_firewall_schedules_endpoint_data_body_item

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
