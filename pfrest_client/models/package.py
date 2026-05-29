from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Package")


@_attrs_define
class Package:
    """
    Attributes:
        name (str | Unset): The name of the pfSense package.<br>
        shortname (None | str | Unset): The package's shortname.<br>
        descr (None | str | Unset): The package's description.<br>
        installed_version (None | str | Unset): The version of the package currently installed.<br>
        latest_version (None | str | Unset): The latest version available for this package.<br>
        update_available (bool | None | Unset): Indicates whether the installed package has an update available.<br>
    """

    name: str | Unset = UNSET
    shortname: None | str | Unset = UNSET
    descr: None | str | Unset = UNSET
    installed_version: None | str | Unset = UNSET
    latest_version: None | str | Unset = UNSET
    update_available: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        shortname: None | str | Unset
        if isinstance(self.shortname, Unset):
            shortname = UNSET
        else:
            shortname = self.shortname

        descr: None | str | Unset
        if isinstance(self.descr, Unset):
            descr = UNSET
        else:
            descr = self.descr

        installed_version: None | str | Unset
        if isinstance(self.installed_version, Unset):
            installed_version = UNSET
        else:
            installed_version = self.installed_version

        latest_version: None | str | Unset
        if isinstance(self.latest_version, Unset):
            latest_version = UNSET
        else:
            latest_version = self.latest_version

        update_available: bool | None | Unset
        if isinstance(self.update_available, Unset):
            update_available = UNSET
        else:
            update_available = self.update_available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if shortname is not UNSET:
            field_dict["shortname"] = shortname
        if descr is not UNSET:
            field_dict["descr"] = descr
        if installed_version is not UNSET:
            field_dict["installed_version"] = installed_version
        if latest_version is not UNSET:
            field_dict["latest_version"] = latest_version
        if update_available is not UNSET:
            field_dict["update_available"] = update_available

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_shortname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shortname = _parse_shortname(d.pop("shortname", UNSET))

        def _parse_descr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        descr = _parse_descr(d.pop("descr", UNSET))

        def _parse_installed_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installed_version = _parse_installed_version(d.pop("installed_version", UNSET))

        def _parse_latest_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_version = _parse_latest_version(d.pop("latest_version", UNSET))

        def _parse_update_available(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        update_available = _parse_update_available(d.pop("update_available", UNSET))

        package = cls(
            name=name,
            shortname=shortname,
            descr=descr,
            installed_version=installed_version,
            latest_version=latest_version,
            update_available=update_available,
        )

        package.additional_properties = d
        return package

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
