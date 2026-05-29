from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HAProxyFrontendErrorFile")


@_attrs_define
class HAProxyFrontendErrorFile:
    """
    Attributes:
        errorcode (int | Unset): The HTTP status code that will trigger this error file to be used.<br>
        errorfile (str | Unset): The HAProxy error file object that should be used for the assigned HTTP status
            code.<br>
    """

    errorcode: int | Unset = UNSET
    errorfile: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errorcode = self.errorcode

        errorfile = self.errorfile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errorcode is not UNSET:
            field_dict["errorcode"] = errorcode
        if errorfile is not UNSET:
            field_dict["errorfile"] = errorfile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        errorcode = d.pop("errorcode", UNSET)

        errorfile = d.pop("errorfile", UNSET)

        ha_proxy_frontend_error_file = cls(
            errorcode=errorcode,
            errorfile=errorfile,
        )

        ha_proxy_frontend_error_file.additional_properties = d
        return ha_proxy_frontend_error_file

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
