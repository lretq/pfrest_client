from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.routing_gateway_group_trigger import RoutingGatewayGroupTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.routing_gateway_group_priorities_item import RoutingGatewayGroupPrioritiesItem


T = TypeVar("T", bound="RoutingGatewayGroup")


@_attrs_define
class RoutingGatewayGroup:
    """
    Attributes:
        name (str | Unset): The name of the gateway group.<br>
        trigger (RoutingGatewayGroupTrigger | Unset): The trigger that will cause a gateway to be excluded from the
            group.<br> Default: RoutingGatewayGroupTrigger.DOWN.
        descr (str | Unset): A description of the gateway group.<br>
        ipprotocol (None | str | Unset): The assumed IP protocol of the gateways in this group.<br> Default: 'unknown'.
        priorities (list[RoutingGatewayGroupPrioritiesItem] | Unset): The priorities of the gateways in this group.<br>
    """

    name: str | Unset = UNSET
    trigger: RoutingGatewayGroupTrigger | Unset = RoutingGatewayGroupTrigger.DOWN
    descr: str | Unset = UNSET
    ipprotocol: None | str | Unset = "unknown"
    priorities: list[RoutingGatewayGroupPrioritiesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        descr = self.descr

        ipprotocol: None | str | Unset
        if isinstance(self.ipprotocol, Unset):
            ipprotocol = UNSET
        else:
            ipprotocol = self.ipprotocol

        priorities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.priorities, Unset):
            priorities = []
            for priorities_item_data in self.priorities:
                priorities_item = priorities_item_data.to_dict()
                priorities.append(priorities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if descr is not UNSET:
            field_dict["descr"] = descr
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if priorities is not UNSET:
            field_dict["priorities"] = priorities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.routing_gateway_group_priorities_item import RoutingGatewayGroupPrioritiesItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: RoutingGatewayGroupTrigger | Unset
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = RoutingGatewayGroupTrigger(_trigger)

        descr = d.pop("descr", UNSET)

        def _parse_ipprotocol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ipprotocol = _parse_ipprotocol(d.pop("ipprotocol", UNSET))

        _priorities = d.pop("priorities", UNSET)
        priorities: list[RoutingGatewayGroupPrioritiesItem] | Unset = UNSET
        if _priorities is not UNSET:
            priorities = []
            for priorities_item_data in _priorities:
                priorities_item = RoutingGatewayGroupPrioritiesItem.from_dict(priorities_item_data)

                priorities.append(priorities_item)

        routing_gateway_group = cls(
            name=name,
            trigger=trigger,
            descr=descr,
            ipprotocol=ipprotocol,
            priorities=priorities,
        )

        routing_gateway_group.additional_properties = d
        return routing_gateway_group

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
