from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.routing_gateway_group_trigger import RoutingGatewayGroupTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.routing_gateway_group_priorities_item import RoutingGatewayGroupPrioritiesItem


T = TypeVar("T", bound="PostRoutingGatewayGroupEndpointJsonBody")


@_attrs_define
class PostRoutingGatewayGroupEndpointJsonBody:
    """
    Attributes:
        name (str): The name of the gateway group.<br>
        priorities (list[RoutingGatewayGroupPrioritiesItem]): The priorities of the gateways in this group.<br>
        trigger (RoutingGatewayGroupTrigger | Unset): The trigger that will cause a gateway to be excluded from the
            group.<br> Default: RoutingGatewayGroupTrigger.DOWN.
        descr (str | Unset): A description of the gateway group.<br>
        ipprotocol (None | str | Unset): The assumed IP protocol of the gateways in this group.<br> Default: 'unknown'.
    """

    name: str
    priorities: list[RoutingGatewayGroupPrioritiesItem]
    trigger: RoutingGatewayGroupTrigger | Unset = RoutingGatewayGroupTrigger.DOWN
    descr: str | Unset = UNSET
    ipprotocol: None | str | Unset = "unknown"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        priorities = []
        for priorities_item_data in self.priorities:
            priorities_item = priorities_item_data.to_dict()
            priorities.append(priorities_item)

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        descr = self.descr

        ipprotocol: None | str | Unset
        if isinstance(self.ipprotocol, Unset):
            ipprotocol = UNSET
        else:
            ipprotocol = self.ipprotocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "priorities": priorities,
            }
        )
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if descr is not UNSET:
            field_dict["descr"] = descr
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.routing_gateway_group_priorities_item import RoutingGatewayGroupPrioritiesItem

        d = dict(src_dict)
        name = d.pop("name")

        priorities = []
        _priorities = d.pop("priorities")
        for priorities_item_data in _priorities:
            priorities_item = RoutingGatewayGroupPrioritiesItem.from_dict(priorities_item_data)

            priorities.append(priorities_item)

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

        post_routing_gateway_group_endpoint_json_body = cls(
            name=name,
            priorities=priorities,
            trigger=trigger,
            descr=descr,
            ipprotocol=ipprotocol,
        )

        post_routing_gateway_group_endpoint_json_body.additional_properties = d
        return post_routing_gateway_group_endpoint_json_body

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
