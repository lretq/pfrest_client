from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostInterfaceApplyEndpointJsonBody")


@_attrs_define
class PostInterfaceApplyEndpointJsonBody:
    """
    Attributes:
        applied (bool | None | Unset): Displays `true` when all interfaces are applied and there are no pending changes
            left.Displays `false` when there are pending interface changes that have not been applied.<br>
        pending_interfaces (list[str] | None | Unset): Displays a list of interfaces that have pending changes waiting
            to be applied.<br>
    """

    applied: bool | None | Unset = UNSET
    pending_interfaces: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied: bool | None | Unset
        if isinstance(self.applied, Unset):
            applied = UNSET
        else:
            applied = self.applied

        pending_interfaces: list[str] | None | Unset
        if isinstance(self.pending_interfaces, Unset):
            pending_interfaces = UNSET
        elif isinstance(self.pending_interfaces, list):
            pending_interfaces = self.pending_interfaces

        else:
            pending_interfaces = self.pending_interfaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if applied is not UNSET:
            field_dict["applied"] = applied
        if pending_interfaces is not UNSET:
            field_dict["pending_interfaces"] = pending_interfaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_applied(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        applied = _parse_applied(d.pop("applied", UNSET))

        def _parse_pending_interfaces(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pending_interfaces_type_0 = cast(list[str], data)

                return pending_interfaces_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[str] | None | Unset, data)

        pending_interfaces = _parse_pending_interfaces(d.pop("pending_interfaces", UNSET))

        post_interface_apply_endpoint_json_body = cls(
            applied=applied,
            pending_interfaces=pending_interfaces,
        )

        post_interface_apply_endpoint_json_body.additional_properties = d
        return post_interface_apply_endpoint_json_body

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
