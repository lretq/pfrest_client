from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_action import ServiceAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostStatusServiceEndpointDataBody")


@_attrs_define
class PostStatusServiceEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        name (str | Unset): The internal name of the service.<br>
        action (ServiceAction | Unset): The action to perform against this service.<br>
        description (None | str | Unset): The full descriptive name of the service.<br>
        enabled (bool | None | Unset): Indicates if the service is enabled.<br>
        status (bool | None | Unset): Indicates if the service is actively running.<br>
    """

    id: int
    name: str | Unset = UNSET
    action: ServiceAction | Unset = UNSET
    description: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    status: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        action: str | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        status: bool | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if action is not UNSET:
            field_dict["action"] = action
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        _action = d.pop("action", UNSET)
        action: ServiceAction | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ServiceAction(_action)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_status(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        post_status_service_endpoint_data_body = cls(
            id=id,
            name=name,
            action=action,
            description=description,
            enabled=enabled,
            status=status,
        )

        post_status_service_endpoint_data_body.additional_properties = d
        return post_status_service_endpoint_data_body

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
