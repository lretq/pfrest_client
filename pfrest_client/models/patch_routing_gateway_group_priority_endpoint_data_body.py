from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchRoutingGatewayGroupPriorityEndpointDataBody")


@_attrs_define
class PatchRoutingGatewayGroupPriorityEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        gateway (str | Unset): The name of the gateway to prioritize in this gateway group.<br>
        tier (int | Unset): The priority of this gateway in the group. Lower numbered tiers are higher priority.<br>
        virtual_ip (str | Unset): The virtual IP to use for this gateway group. Use `address` to use the interface's
            current IP.<br> Default: 'address'.
    """

    parent_id: int
    id: int
    gateway: str | Unset = UNSET
    tier: int | Unset = UNSET
    virtual_ip: str | Unset = "address"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        gateway = self.gateway

        tier = self.tier

        virtual_ip = self.virtual_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
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
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        gateway = d.pop("gateway", UNSET)

        tier = d.pop("tier", UNSET)

        virtual_ip = d.pop("virtual_ip", UNSET)

        patch_routing_gateway_group_priority_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            gateway=gateway,
            tier=tier,
            virtual_ip=virtual_ip,
        )

        patch_routing_gateway_group_priority_endpoint_data_body.additional_properties = d
        return patch_routing_gateway_group_priority_endpoint_data_body

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
