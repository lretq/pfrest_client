from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bind_access_list_entries_item import BINDAccessListEntriesItem


T = TypeVar("T", bound="BINDAccessList")


@_attrs_define
class BINDAccessList:
    """
    Attributes:
        name (str | Unset): The name of the access list.<br>
        description (str | Unset): A description for the access list.<br>
        entries (list[BINDAccessListEntriesItem] | Unset): The network entries for this access list.<br>
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    entries: list[BINDAccessListEntriesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        entries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if entries is not UNSET:
            field_dict["entries"] = entries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bind_access_list_entries_item import BINDAccessListEntriesItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _entries = d.pop("entries", UNSET)
        entries: list[BINDAccessListEntriesItem] | Unset = UNSET
        if _entries is not UNSET:
            entries = []
            for entries_item_data in _entries:
                entries_item = BINDAccessListEntriesItem.from_dict(entries_item_data)

                entries.append(entries_item)

        bind_access_list = cls(
            name=name,
            description=description,
            entries=entries,
        )

        bind_access_list.additional_properties = d
        return bind_access_list

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
