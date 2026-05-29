from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph_ql_variables import GraphQLVariables


T = TypeVar("T", bound="PostGraphQLEndpointDataBody")


@_attrs_define
class PostGraphQLEndpointDataBody:
    """
    Attributes:
        query (str | Unset): The GraphQL query/mutation to execute.<br>
        variables (GraphQLVariables | Unset): The variables to pass to the GraphQL query or mutation. In general, this
            will be an object containing the variables to pass to the query or mutation.<br>
    """

    query: str | Unset = UNSET
    variables: GraphQLVariables | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph_ql_variables import GraphQLVariables

        d = dict(src_dict)
        query = d.pop("query", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: GraphQLVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = GraphQLVariables.from_dict(_variables)

        post_graph_ql_endpoint_data_body = cls(
            query=query,
            variables=variables,
        )

        post_graph_ql_endpoint_data_body.additional_properties = d
        return post_graph_ql_endpoint_data_body

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
