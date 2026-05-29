from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BINDView")


@_attrs_define
class BINDView:
    """
    Attributes:
        name (str | Unset): The name of the view.<br>
        descr (str | Unset): A description for the view.<br>
        recursion (bool | Unset): Enables or disables recursion for the view.<br>
        match_clients (list[str] | Unset): The access lists to match clients against.<br>
        allow_recursion (list[str] | Unset): The access lists to allow recursion for.<br>
        bind_custom_options (str | Unset): Custom BIND options for the view.<br>
    """

    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    recursion: bool | Unset = UNSET
    match_clients: list[str] | Unset = UNSET
    allow_recursion: list[str] | Unset = UNSET
    bind_custom_options: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        descr = self.descr

        recursion = self.recursion

        match_clients: list[str] | Unset = UNSET
        if not isinstance(self.match_clients, Unset):
            match_clients = self.match_clients

        allow_recursion: list[str] | Unset = UNSET
        if not isinstance(self.allow_recursion, Unset):
            allow_recursion = self.allow_recursion

        bind_custom_options = self.bind_custom_options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if recursion is not UNSET:
            field_dict["recursion"] = recursion
        if match_clients is not UNSET:
            field_dict["match_clients"] = match_clients
        if allow_recursion is not UNSET:
            field_dict["allow_recursion"] = allow_recursion
        if bind_custom_options is not UNSET:
            field_dict["bind_custom_options"] = bind_custom_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        recursion = d.pop("recursion", UNSET)

        match_clients = cast(list[str], d.pop("match_clients", UNSET))

        allow_recursion = cast(list[str], d.pop("allow_recursion", UNSET))

        bind_custom_options = d.pop("bind_custom_options", UNSET)

        bind_view = cls(
            name=name,
            descr=descr,
            recursion=recursion,
            match_clients=match_clients,
            allow_recursion=allow_recursion,
            bind_custom_options=bind_custom_options,
        )

        bind_view.additional_properties = d
        return bind_view

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
