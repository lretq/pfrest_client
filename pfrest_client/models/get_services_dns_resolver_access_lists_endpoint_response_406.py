from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.not_acceptable_error_data_type_0_item import NotAcceptableErrorDataType0Item
    from ..models.not_acceptable_error_data_type_1 import NotAcceptableErrorDataType1
    from ..models.not_acceptable_error_links import NotAcceptableErrorLinks


T = TypeVar("T", bound="GetServicesDNSResolverAccessListsEndpointResponse406")


@_attrs_define
class GetServicesDNSResolverAccessListsEndpointResponse406:
    """
    Attributes:
        code (int | Unset): The HTTP status code that corresponds with the API response. Default: 406.
        status (str | Unset): The HTTP status message that corresponds with the HTTP status code. Default: 'not
            acceptable'.
        response_id (str | Unset): The unique response ID that corresponds with the result of the APIcall. In most
            situations, this will contain an error code.
        message (str | Unset): The descriptive message detailing the results of the API call.
        data (list[NotAcceptableErrorDataType0Item] | NotAcceptableErrorDataType1 | Unset): The data requested from the
            API. In the event that many objects havebeen requested, this field will be an array of objects. Otherwise, it
            will only returnthe single object requested.
        field_links (NotAcceptableErrorLinks | Unset): An array of links to resources that are related to this API
            response.
    """

    code: int | Unset = 406
    status: str | Unset = "not acceptable"
    response_id: str | Unset = UNSET
    message: str | Unset = UNSET
    data: list[NotAcceptableErrorDataType0Item] | NotAcceptableErrorDataType1 | Unset = UNSET
    field_links: NotAcceptableErrorLinks | Unset = UNSET
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
        from ..models.not_acceptable_error_data_type_0_item import NotAcceptableErrorDataType0Item
        from ..models.not_acceptable_error_data_type_1 import NotAcceptableErrorDataType1
        from ..models.not_acceptable_error_links import NotAcceptableErrorLinks

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        status = d.pop("status", UNSET)

        response_id = d.pop("response_id", UNSET)

        message = d.pop("message", UNSET)

        def _parse_data(data: object) -> list[NotAcceptableErrorDataType0Item] | NotAcceptableErrorDataType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = NotAcceptableErrorDataType0Item.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = NotAcceptableErrorDataType1.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data", UNSET))

        _field_links = d.pop("_links", UNSET)
        field_links: NotAcceptableErrorLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = NotAcceptableErrorLinks.from_dict(_field_links)

        get_services_dns_resolver_access_lists_endpoint_response_406 = cls(
            code=code,
            status=status,
            response_id=response_id,
            message=message,
            data=data,
            field_links=field_links,
        )

        get_services_dns_resolver_access_lists_endpoint_response_406.additional_properties = d
        return get_services_dns_resolver_access_lists_endpoint_response_406

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
