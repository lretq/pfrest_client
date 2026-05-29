from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.graph_ql_response_errors_item_extensions import GraphQLResponseErrorsItemExtensions
    from ..models.graph_ql_response_errors_item_locations_item import GraphQLResponseErrorsItemLocationsItem


T = TypeVar("T", bound="GraphQLResponseErrorsItem")


@_attrs_define
class GraphQLResponseErrorsItem:
    """
    Attributes:
        message (str | Unset): The error message.
        extensions (GraphQLResponseErrorsItemExtensions | Unset): The error extensions.
        locations (list[GraphQLResponseErrorsItemLocationsItem] | Unset): The error locations.
        path (list[str] | Unset): The error path.
    """

    message: str | Unset = UNSET
    extensions: GraphQLResponseErrorsItemExtensions | Unset = UNSET
    locations: list[GraphQLResponseErrorsItemLocationsItem] | Unset = UNSET
    path: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        extensions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions.to_dict()

        locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        path: list[str] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if locations is not UNSET:
            field_dict["locations"] = locations
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph_ql_response_errors_item_extensions import GraphQLResponseErrorsItemExtensions
        from ..models.graph_ql_response_errors_item_locations_item import GraphQLResponseErrorsItemLocationsItem

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _extensions = d.pop("extensions", UNSET)
        extensions: GraphQLResponseErrorsItemExtensions | Unset
        if isinstance(_extensions, Unset):
            extensions = UNSET
        else:
            extensions = GraphQLResponseErrorsItemExtensions.from_dict(_extensions)

        _locations = d.pop("locations", UNSET)
        locations: list[GraphQLResponseErrorsItemLocationsItem] | Unset = UNSET
        if _locations is not UNSET:
            locations = []
            for locations_item_data in _locations:
                locations_item = GraphQLResponseErrorsItemLocationsItem.from_dict(locations_item_data)

                locations.append(locations_item)

        path = cast(list[str], d.pop("path", UNSET))

        graph_ql_response_errors_item = cls(
            message=message,
            extensions=extensions,
            locations=locations,
            path=path,
        )

        graph_ql_response_errors_item.additional_properties = d
        return graph_ql_response_errors_item

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
