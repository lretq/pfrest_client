from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostSystemRESTAPISettingsSyncEndpointDataBody")


@_attrs_define
class PostSystemRESTAPISettingsSyncEndpointDataBody:
    """
    Attributes:
        sync_data (str): The serialized REST API settings data to be synced.<br>
    """

    sync_data: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sync_data = self.sync_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sync_data": sync_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sync_data = d.pop("sync_data")

        post_system_restapi_settings_sync_endpoint_data_body = cls(
            sync_data=sync_data,
        )

        post_system_restapi_settings_sync_endpoint_data_body.additional_properties = d
        return post_system_restapi_settings_sync_endpoint_data_body

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
