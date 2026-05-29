from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostRoutingGatewayGroupPriorityEndpointDataBody")


@_attrs_define
class PostRoutingGatewayGroupPriorityEndpointDataBody:
    """
    Attributes:
        gateway (str): The name of the gateway to prioritize in this gateway group.<br>
        tier (int): The priority of this gateway in the group. Lower numbered tiers are higher priority.<br>
        parent_id (int): The ID of the parent this object is nested under.
        virtual_ip (str | Unset): The virtual IP to use for this gateway group. Use `address` to use the interface's
            current IP.<br> Default: 'address'.
    """

    gateway: str
    tier: int
    parent_id: int
    virtual_ip: str | Unset = "address"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway = self.gateway

        tier = self.tier

        parent_id = self.parent_id

        virtual_ip = self.virtual_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gateway": gateway,
                "tier": tier,
                "parent_id": parent_id,
            }
        )
        if virtual_ip is not UNSET:
            field_dict["virtual_ip"] = virtual_ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gateway = d.pop("gateway")

        tier = d.pop("tier")

        parent_id = d.pop("parent_id")

        virtual_ip = d.pop("virtual_ip", UNSET)

        post_routing_gateway_group_priority_endpoint_data_body = cls(
            gateway=gateway,
            tier=tier,
            parent_id=parent_id,
            virtual_ip=virtual_ip,
        )

        post_routing_gateway_group_priority_endpoint_data_body.additional_properties = d
        return post_routing_gateway_group_priority_endpoint_data_body

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
