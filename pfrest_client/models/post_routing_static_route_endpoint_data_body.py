from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostRoutingStaticRouteEndpointDataBody")


@_attrs_define
class PostRoutingStaticRouteEndpointDataBody:
    """
    Attributes:
        network (str): Sets the destination network for this static route in CIDR notation.<br>
        gateway (str): Sets which gateway this route applies to.<br>
        descr (str | Unset): Sets a description for administrative reference.<br>
        disabled (bool | Unset): Disable this static route.<br>
    """

    network: str
    gateway: str
    descr: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network

        gateway = self.gateway

        descr = self.descr

        disabled = self.disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
                "gateway": gateway,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network = d.pop("network")

        gateway = d.pop("gateway")

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        post_routing_static_route_endpoint_data_body = cls(
            network=network,
            gateway=gateway,
            descr=descr,
            disabled=disabled,
        )

        post_routing_static_route_endpoint_data_body.additional_properties = d
        return post_routing_static_route_endpoint_data_body

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
