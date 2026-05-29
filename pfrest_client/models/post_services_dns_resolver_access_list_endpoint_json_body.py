from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dns_resolver_access_list_action import DNSResolverAccessListAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_resolver_access_list_networks_item import DNSResolverAccessListNetworksItem


T = TypeVar("T", bound="PostServicesDNSResolverAccessListEndpointJsonBody")


@_attrs_define
class PostServicesDNSResolverAccessListEndpointJsonBody:
    """
    Attributes:
        name (str): The name of this access list.<br>
        action (DNSResolverAccessListAction): The action to take when an access list match is found.<br>
        networks (list[DNSResolverAccessListNetworksItem]): The DNS Resolver access list network entries to include in
            this access list.<br>
        description (str | Unset): A description for this access list.<br>
    """

    name: str
    action: DNSResolverAccessListAction
    networks: list[DNSResolverAccessListNetworksItem]
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        action = self.action.value

        networks = []
        for networks_item_data in self.networks:
            networks_item = networks_item_data.to_dict()
            networks.append(networks_item)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "action": action,
                "networks": networks,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_resolver_access_list_networks_item import DNSResolverAccessListNetworksItem

        d = dict(src_dict)
        name = d.pop("name")

        action = DNSResolverAccessListAction(d.pop("action"))

        networks = []
        _networks = d.pop("networks")
        for networks_item_data in _networks:
            networks_item = DNSResolverAccessListNetworksItem.from_dict(networks_item_data)

            networks.append(networks_item)

        description = d.pop("description", UNSET)

        post_services_dns_resolver_access_list_endpoint_json_body = cls(
            name=name,
            action=action,
            networks=networks,
            description=description,
        )

        post_services_dns_resolver_access_list_endpoint_json_body.additional_properties = d
        return post_services_dns_resolver_access_list_endpoint_json_body

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
