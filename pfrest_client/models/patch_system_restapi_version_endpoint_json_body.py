from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchSystemRESTAPIVersionEndpointJsonBody")


@_attrs_define
class PatchSystemRESTAPIVersionEndpointJsonBody:
    """
    Attributes:
        current_version (None | str | Unset): The current API version installed on this system.<br>
        latest_version (None | str | Unset): The latest API version available to this system.<br>
        latest_version_release_date (None | str | Unset): The latest API version's release date.<br>
        update_available (bool | None | Unset): Indicates if an API update is available for this system.<br>
        install_version (None | str | Unset): Set the API version to update or rollback to.<br>
        available_versions (list[str] | None | Unset): All available versions of the REST API package for this
            system.<br>
    """

    current_version: None | str | Unset = UNSET
    latest_version: None | str | Unset = UNSET
    latest_version_release_date: None | str | Unset = UNSET
    update_available: bool | None | Unset = UNSET
    install_version: None | str | Unset = UNSET
    available_versions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_version: None | str | Unset
        if isinstance(self.current_version, Unset):
            current_version = UNSET
        else:
            current_version = self.current_version

        latest_version: None | str | Unset
        if isinstance(self.latest_version, Unset):
            latest_version = UNSET
        else:
            latest_version = self.latest_version

        latest_version_release_date: None | str | Unset
        if isinstance(self.latest_version_release_date, Unset):
            latest_version_release_date = UNSET
        else:
            latest_version_release_date = self.latest_version_release_date

        update_available: bool | None | Unset
        if isinstance(self.update_available, Unset):
            update_available = UNSET
        else:
            update_available = self.update_available

        install_version: None | str | Unset
        if isinstance(self.install_version, Unset):
            install_version = UNSET
        else:
            install_version = self.install_version

        available_versions: list[str] | None | Unset
        if isinstance(self.available_versions, Unset):
            available_versions = UNSET
        elif isinstance(self.available_versions, list):
            available_versions = self.available_versions

        else:
            available_versions = self.available_versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_version is not UNSET:
            field_dict["current_version"] = current_version
        if latest_version is not UNSET:
            field_dict["latest_version"] = latest_version
        if latest_version_release_date is not UNSET:
            field_dict["latest_version_release_date"] = latest_version_release_date
        if update_available is not UNSET:
            field_dict["update_available"] = update_available
        if install_version is not UNSET:
            field_dict["install_version"] = install_version
        if available_versions is not UNSET:
            field_dict["available_versions"] = available_versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_current_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_version = _parse_current_version(d.pop("current_version", UNSET))

        def _parse_latest_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_version = _parse_latest_version(d.pop("latest_version", UNSET))

        def _parse_latest_version_release_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_version_release_date = _parse_latest_version_release_date(d.pop("latest_version_release_date", UNSET))

        def _parse_update_available(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        update_available = _parse_update_available(d.pop("update_available", UNSET))

        def _parse_install_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        install_version = _parse_install_version(d.pop("install_version", UNSET))

        def _parse_available_versions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                available_versions_type_0 = cast(list[str], data)

                return available_versions_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[str] | None | Unset, data)

        available_versions = _parse_available_versions(d.pop("available_versions", UNSET))

        patch_system_restapi_version_endpoint_json_body = cls(
            current_version=current_version,
            latest_version=latest_version,
            latest_version_release_date=latest_version_release_date,
            update_available=update_available,
            install_version=install_version,
            available_versions=available_versions,
        )

        patch_system_restapi_version_endpoint_json_body.additional_properties = d
        return patch_system_restapi_version_endpoint_json_body

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
