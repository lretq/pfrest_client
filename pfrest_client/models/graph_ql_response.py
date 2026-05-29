from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph_ql_response_data import GraphQLResponseData
    from ..models.graph_ql_response_errors_item import GraphQLResponseErrorsItem


T = TypeVar("T", bound="GraphQLResponse")


@_attrs_define
class GraphQLResponse:
    """
    Attributes:
        data (GraphQLResponseData | Unset): The GraphQL response data.
        errors (list[GraphQLResponseErrorsItem] | Unset): The GraphQL response errors.
    """

    data: GraphQLResponseData | Unset = UNSET
    errors: list[GraphQLResponseErrorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph_ql_response_data import GraphQLResponseData
        from ..models.graph_ql_response_errors_item import GraphQLResponseErrorsItem

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: GraphQLResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GraphQLResponseData.from_dict(_data)

        _errors = d.pop("errors", UNSET)
        errors: list[GraphQLResponseErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = GraphQLResponseErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        graph_ql_response = cls(
            data=data,
            errors=errors,
        )

        graph_ql_response.additional_properties = d
        return graph_ql_response

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
