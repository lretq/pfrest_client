from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostServicesHAProxyBackendErrorFileEndpointDataBody")


@_attrs_define
class PostServicesHAProxyBackendErrorFileEndpointDataBody:
    """
    Attributes:
        errorcode (int): The HTTP status code that will trigger this error file to be used.<br>
        errorfile (str): The HAProxy error file object that should be used for the assigned HTTP status code.<br>
        parent_id (int): The ID of the parent this object is nested under.
    """

    errorcode: int
    errorfile: str
    parent_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errorcode = self.errorcode

        errorfile = self.errorfile

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "errorcode": errorcode,
                "errorfile": errorfile,
                "parent_id": parent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        errorcode = d.pop("errorcode")

        errorfile = d.pop("errorfile")

        parent_id = d.pop("parent_id")

        post_services_ha_proxy_backend_error_file_endpoint_data_body = cls(
            errorcode=errorcode,
            errorfile=errorfile,
            parent_id=parent_id,
        )

        post_services_ha_proxy_backend_error_file_endpoint_data_body.additional_properties = d
        return post_services_ha_proxy_backend_error_file_endpoint_data_body

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
