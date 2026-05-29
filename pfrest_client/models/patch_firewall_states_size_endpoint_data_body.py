from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchFirewallStatesSizeEndpointDataBody")


@_attrs_define
class PatchFirewallStatesSizeEndpointDataBody:
    """
    Attributes:
        maximumstates (int | Unset): The maximum number of firewall state entries allowed by this firewall.<br> Default:
            6512000.
        defaultmaximumstates (int | None | Unset): The default number of firewall state entries allowed by this
            firewall.<br>
        currentstates (int | None | Unset): The number of firewall state entries currently registered in the states
            table.<br>
    """

    maximumstates: int | Unset = 6512000
    defaultmaximumstates: int | None | Unset = UNSET
    currentstates: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maximumstates = self.maximumstates

        defaultmaximumstates: int | None | Unset
        if isinstance(self.defaultmaximumstates, Unset):
            defaultmaximumstates = UNSET
        else:
            defaultmaximumstates = self.defaultmaximumstates

        currentstates: int | None | Unset
        if isinstance(self.currentstates, Unset):
            currentstates = UNSET
        else:
            currentstates = self.currentstates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maximumstates is not UNSET:
            field_dict["maximumstates"] = maximumstates
        if defaultmaximumstates is not UNSET:
            field_dict["defaultmaximumstates"] = defaultmaximumstates
        if currentstates is not UNSET:
            field_dict["currentstates"] = currentstates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        maximumstates = d.pop("maximumstates", UNSET)

        def _parse_defaultmaximumstates(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        defaultmaximumstates = _parse_defaultmaximumstates(d.pop("defaultmaximumstates", UNSET))

        def _parse_currentstates(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        currentstates = _parse_currentstates(d.pop("currentstates", UNSET))

        patch_firewall_states_size_endpoint_data_body = cls(
            maximumstates=maximumstates,
            defaultmaximumstates=defaultmaximumstates,
            currentstates=currentstates,
        )

        patch_firewall_states_size_endpoint_data_body.additional_properties = d
        return patch_firewall_states_size_endpoint_data_body

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
