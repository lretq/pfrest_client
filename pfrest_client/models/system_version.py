from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemVersion")


@_attrs_define
class SystemVersion:
    """
    Attributes:
        version (None | str | Unset): The official pfSense version release name. (e.g. X.X.X-RELEASE)<br>
        base (None | str | Unset): The base pfSense version. For pfSense CE, this will be the major and minor version
            but not the patch. For pfSense Plus, this will be the version year and month but not the patch.<br>
        patch (None | str | Unset): The pfSense build's patch version.<br>
        buildtime (None | str | Unset): The datetime string of when the pfSense version was initially built.<br>
    """

    version: None | str | Unset = UNSET
    base: None | str | Unset = UNSET
    patch: None | str | Unset = UNSET
    buildtime: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        base: None | str | Unset
        if isinstance(self.base, Unset):
            base = UNSET
        else:
            base = self.base

        patch: None | str | Unset
        if isinstance(self.patch, Unset):
            patch = UNSET
        else:
            patch = self.patch

        buildtime: None | str | Unset
        if isinstance(self.buildtime, Unset):
            buildtime = UNSET
        else:
            buildtime = self.buildtime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if base is not UNSET:
            field_dict["base"] = base
        if patch is not UNSET:
            field_dict["patch"] = patch
        if buildtime is not UNSET:
            field_dict["buildtime"] = buildtime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        base = _parse_base(d.pop("base", UNSET))

        def _parse_patch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        patch = _parse_patch(d.pop("patch", UNSET))

        def _parse_buildtime(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        buildtime = _parse_buildtime(d.pop("buildtime", UNSET))

        system_version = cls(
            version=version,
            base=base,
            patch=patch,
            buildtime=buildtime,
        )

        system_version.additional_properties = d
        return system_version

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
