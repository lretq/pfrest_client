from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.firewall_schedule_timerange_item import FirewallScheduleTimerangeItem


T = TypeVar("T", bound="FirewallSchedule")


@_attrs_define
class FirewallSchedule:
    """
    Attributes:
        schedlabel (None | str | Unset): A unique ID for this schedule used internally by the system.<br>
        name (str | Unset): The unique name to assign this schedule.<br>
        descr (str | Unset): A description of this schedules purpose.<br>
        active (bool | None | Unset): Displays whether the schedule is currently active or not.<br>
        timerange (list[FirewallScheduleTimerangeItem] | Unset): The date/times this firewall schedule will be
            active.<br>
    """

    schedlabel: None | str | Unset = UNSET
    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    active: bool | None | Unset = UNSET
    timerange: list[FirewallScheduleTimerangeItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedlabel: None | str | Unset
        if isinstance(self.schedlabel, Unset):
            schedlabel = UNSET
        else:
            schedlabel = self.schedlabel

        name = self.name

        descr = self.descr

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        timerange: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timerange, Unset):
            timerange = []
            for timerange_item_data in self.timerange:
                timerange_item = timerange_item_data.to_dict()
                timerange.append(timerange_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if schedlabel is not UNSET:
            field_dict["schedlabel"] = schedlabel
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if active is not UNSET:
            field_dict["active"] = active
        if timerange is not UNSET:
            field_dict["timerange"] = timerange

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.firewall_schedule_timerange_item import FirewallScheduleTimerangeItem

        d = dict(src_dict)

        def _parse_schedlabel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        schedlabel = _parse_schedlabel(d.pop("schedlabel", UNSET))

        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        _timerange = d.pop("timerange", UNSET)
        timerange: list[FirewallScheduleTimerangeItem] | Unset = UNSET
        if _timerange is not UNSET:
            timerange = []
            for timerange_item_data in _timerange:
                timerange_item = FirewallScheduleTimerangeItem.from_dict(timerange_item_data)

                timerange.append(timerange_item)

        firewall_schedule = cls(
            schedlabel=schedlabel,
            name=name,
            descr=descr,
            active=active,
            timerange=timerange,
        )

        firewall_schedule.additional_properties = d
        return firewall_schedule

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
