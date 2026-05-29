from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesHAProxyFrontendErrorFileEndpointDataBody")


@_attrs_define
class PatchServicesHAProxyFrontendErrorFileEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        errorcode (int | Unset): The HTTP status code that will trigger this error file to be used.<br>
        errorfile (str | Unset): The HAProxy error file object that should be used for the assigned HTTP status
            code.<br>
    """

    parent_id: int
    id: int
    errorcode: int | Unset = UNSET
    errorfile: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        errorcode = self.errorcode

        errorfile = self.errorfile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if errorcode is not UNSET:
            field_dict["errorcode"] = errorcode
        if errorfile is not UNSET:
            field_dict["errorfile"] = errorfile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        errorcode = d.pop("errorcode", UNSET)

        errorfile = d.pop("errorfile", UNSET)

        patch_services_ha_proxy_frontend_error_file_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            errorcode=errorcode,
            errorfile=errorfile,
        )

        patch_services_ha_proxy_frontend_error_file_endpoint_data_body.additional_properties = d
        return patch_services_ha_proxy_frontend_error_file_endpoint_data_body

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
