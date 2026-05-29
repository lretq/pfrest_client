from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigHistoryRevision")


@_attrs_define
class ConfigHistoryRevision:
    """
    Attributes:
        time (int | Unset): The time the configuration change was made.<br>
        description (str | Unset): The description of the configuration change.<br>
        version (str | Unset): The configuration version associated with this change.<br>
        filesize (int | Unset): The file size (in bytes) of the configuration file associated with this change.<br>
    """

    time: int | Unset = UNSET
    description: str | Unset = UNSET
    version: str | Unset = UNSET
    filesize: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        description = self.description

        version = self.version

        filesize = self.filesize

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
        if filesize is not UNSET:
            field_dict["filesize"] = filesize

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        description = d.pop("description", UNSET)

        version = d.pop("version", UNSET)

        filesize = d.pop("filesize", UNSET)

        config_history_revision = cls(
            time=time,
            description=description,
            version=version,
            filesize=filesize,
        )

        config_history_revision.additional_properties = d
        return config_history_revision

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
