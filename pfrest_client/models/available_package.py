from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailablePackage")


@_attrs_define
class AvailablePackage:
    """
    Attributes:
        name (str | Unset): The name of the pfSense package.<br>
        shortname (None | str | Unset): The package's shortname.<br>
        descr (None | str | Unset): The package's description.<br>
        version (None | str | Unset): The latest version available for this package.<br>
        installed (bool | None | Unset): Indicates whether the package is currently installed or not.<br>
        deps (list[str] | None | Unset): Dependencies for this package that are also installed when this package is
            installed.<br>
    """

    name: str | Unset = UNSET
    shortname: None | str | Unset = UNSET
    descr: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    installed: bool | None | Unset = UNSET
    deps: list[str] | None | Unset = UNSET
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

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        installed: bool | None | Unset
        if isinstance(self.installed, Unset):
            installed = UNSET
        else:
            installed = self.installed

        deps: list[str] | None | Unset
        if isinstance(self.deps, Unset):
            deps = UNSET
        elif isinstance(self.deps, list):
            deps = self.deps

        else:
            deps = self.deps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if shortname is not UNSET:
            field_dict["shortname"] = shortname
        if descr is not UNSET:
            field_dict["descr"] = descr
        if version is not UNSET:
            field_dict["version"] = version
        if installed is not UNSET:
            field_dict["installed"] = installed
        if deps is not UNSET:
            field_dict["deps"] = deps

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

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_installed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        installed = _parse_installed(d.pop("installed", UNSET))

        def _parse_deps(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                deps_type_0 = cast(list[str], data)

                return deps_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[str] | None | Unset, data)

        deps = _parse_deps(d.pop("deps", UNSET))

        available_package = cls(
            name=name,
            shortname=shortname,
            descr=descr,
            version=version,
            installed=installed,
            deps=deps,
        )

        available_package.additional_properties = d
        return available_package

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
