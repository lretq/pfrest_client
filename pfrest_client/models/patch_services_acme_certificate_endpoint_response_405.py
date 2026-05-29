from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.method_not_allowed_error_data_type_0_item import MethodNotAllowedErrorDataType0Item
    from ..models.method_not_allowed_error_data_type_1 import MethodNotAllowedErrorDataType1
    from ..models.method_not_allowed_error_links import MethodNotAllowedErrorLinks


T = TypeVar("T", bound="PatchServicesACMECertificateEndpointResponse405")


@_attrs_define
class PatchServicesACMECertificateEndpointResponse405:
    """
    Attributes:
        code (int | Unset): The HTTP status code that corresponds with the API response. Default: 405.
        status (str | Unset): The HTTP status message that corresponds with the HTTP status code. Default: 'method not
            allowed'.
        response_id (str | Unset): The unique response ID that corresponds with the result of the APIcall. In most
            situations, this will contain an error code.
        message (str | Unset): The descriptive message detailing the results of the API call.
        data (list[MethodNotAllowedErrorDataType0Item] | MethodNotAllowedErrorDataType1 | Unset): The data requested
            from the API. In the event that many objects havebeen requested, this field will be an array of objects.
            Otherwise, it will only returnthe single object requested.
        field_links (MethodNotAllowedErrorLinks | Unset): An array of links to resources that are related to this API
            response.
    """

    code: int | Unset = 405
    status: str | Unset = "method not allowed"
    response_id: str | Unset = UNSET
    message: str | Unset = UNSET
    data: list[MethodNotAllowedErrorDataType0Item] | MethodNotAllowedErrorDataType1 | Unset = UNSET
    field_links: MethodNotAllowedErrorLinks | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        status = self.status

        response_id = self.response_id

        message = self.message

        data: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data.to_dict()

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status
        if response_id is not UNSET:
            field_dict["response_id"] = response_id
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.method_not_allowed_error_data_type_0_item import MethodNotAllowedErrorDataType0Item
        from ..models.method_not_allowed_error_data_type_1 import MethodNotAllowedErrorDataType1
        from ..models.method_not_allowed_error_links import MethodNotAllowedErrorLinks

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        status = d.pop("status", UNSET)

        response_id = d.pop("response_id", UNSET)

        message = d.pop("message", UNSET)

        def _parse_data(
            data: object,
        ) -> list[MethodNotAllowedErrorDataType0Item] | MethodNotAllowedErrorDataType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = MethodNotAllowedErrorDataType0Item.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = MethodNotAllowedErrorDataType1.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: MethodNotAllowedErrorLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = MethodNotAllowedErrorLinks.from_dict(_field_links)

        patch_services_acme_certificate_endpoint_response_405 = cls(
            code=code,
            status=status,
            response_id=response_id,
            message=message,
            data=data,
            field_links=field_links,
        )

        patch_services_acme_certificate_endpoint_response_405.additional_properties = d
        return patch_services_acme_certificate_endpoint_response_405

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
