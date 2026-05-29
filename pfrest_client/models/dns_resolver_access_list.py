from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dns_resolver_access_list_action import DNSResolverAccessListAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dns_resolver_access_list_networks_item import DNSResolverAccessListNetworksItem


T = TypeVar("T", bound="DNSResolverAccessList")


@_attrs_define
class DNSResolverAccessList:
    """
    Attributes:
        name (str | Unset): The name of this access list.<br>
        action (DNSResolverAccessListAction | Unset): The action to take when an access list match is found.<br>
        description (str | Unset): A description for this access list.<br>
        networks (list[DNSResolverAccessListNetworksItem] | Unset): The DNS Resolver access list network entries to
            include in this access list.<br>
    """

    name: str | Unset = UNSET
    action: DNSResolverAccessListAction | Unset = UNSET
    description: str | Unset = UNSET
    networks: list[DNSResolverAccessListNetworksItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        description = self.description

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if action is not UNSET:
            field_dict["action"] = action
        if description is not UNSET:
            field_dict["description"] = description
        if networks is not UNSET:
            field_dict["networks"] = networks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dns_resolver_access_list_networks_item import DNSResolverAccessListNetworksItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _action = d.pop("action", UNSET)
        action: DNSResolverAccessListAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = DNSResolverAccessListAction(_action)

        description = d.pop("description", UNSET)

        _networks = d.pop("networks", UNSET)
        networks: list[DNSResolverAccessListNetworksItem] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = DNSResolverAccessListNetworksItem.from_dict(networks_item_data)

                networks.append(networks_item)

        dns_resolver_access_list = cls(
            name=name,
            action=action,
            description=description,
            networks=networks,
        )

        dns_resolver_access_list.additional_properties = d
        return dns_resolver_access_list

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
