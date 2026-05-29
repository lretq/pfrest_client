from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesServiceWatchdogEndpointDataBody")


@_attrs_define
class PatchServicesServiceWatchdogEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        name (str | Unset): The name of the service to be watched.<br>
        description (None | str | Unset): The description for the service being watched.<br>
        notify (bool | Unset): Enable or disable notifications being sent when Service Watchdogs finds this service
            stopped.<br>
        enabled (bool | None | Unset): Indicates if this Service Watchdog is enabled or disabled. This value is
            unused.<br> Default: True.
    """

    id: int
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    notify: bool | Unset = UNSET
    enabled: bool | None | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        notify = self.notify

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if notify is not UNSET:
            field_dict["notify"] = notify
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        notify = d.pop("notify", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        patch_services_service_watchdog_endpoint_data_body = cls(
            id=id,
            name=name,
            description=description,
            notify=notify,
            enabled=enabled,
        )

        patch_services_service_watchdog_endpoint_data_body.additional_properties = d
        return patch_services_service_watchdog_endpoint_data_body

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
