from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bind_access_list_entries_item import BINDAccessListEntriesItem


T = TypeVar("T", bound="PutServicesBINDAccessListsEndpointDataBodyItem")


@_attrs_define
class PutServicesBINDAccessListsEndpointDataBodyItem:
    """
    Attributes:
        name (str): The name of the access list.<br>
        entries (list[BINDAccessListEntriesItem]): The network entries for this access list.<br>
        description (str | Unset): A description for the access list.<br>
    """

    name: str
    entries: list[BINDAccessListEntriesItem]
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "entries": entries,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bind_access_list_entries_item import BINDAccessListEntriesItem

        d = dict(src_dict)
        name = d.pop("name")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = BINDAccessListEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        description = d.pop("description", UNSET)

        put_services_bind_access_lists_endpoint_data_body_item = cls(
            name=name,
            entries=entries,
            description=description,
        )

        put_services_bind_access_lists_endpoint_data_body_item.additional_properties = d
        return put_services_bind_access_lists_endpoint_data_body_item

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
