from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutingGatewayGroupPriority")


@_attrs_define
class RoutingGatewayGroupPriority:
    """
    Attributes:
        gateway (str | Unset): The name of the gateway to prioritize in this gateway group.<br>
        tier (int | Unset): The priority of this gateway in the group. Lower numbered tiers are higher priority.<br>
        virtual_ip (str | Unset): The virtual IP to use for this gateway group. Use `address` to use the interface's
            current IP.<br> Default: 'address'.
    """

    gateway: str | Unset = UNSET
    tier: int | Unset = UNSET
    virtual_ip: str | Unset = "address"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway = self.gateway

        tier = self.tier

        virtual_ip = self.virtual_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if tier is not UNSET:
            field_dict["tier"] = tier
        if virtual_ip is not UNSET:
            field_dict["virtual_ip"] = virtual_ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gateway = d.pop("gateway", UNSET)

        tier = d.pop("tier", UNSET)

        virtual_ip = d.pop("virtual_ip", UNSET)

        routing_gateway_group_priority = cls(
            gateway=gateway,
            tier=tier,
            virtual_ip=virtual_ip,
        )

        routing_gateway_group_priority.additional_properties = d
        return routing_gateway_group_priority

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
