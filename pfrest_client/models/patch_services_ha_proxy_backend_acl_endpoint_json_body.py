from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_backend_acl_expression import HAProxyBackendACLExpression
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesHAProxyBackendACLEndpointJsonBody")


@_attrs_define
class PatchServicesHAProxyBackendACLEndpointJsonBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        name (str | Unset): The unique name for this backend ACL.<br>
        expression (HAProxyBackendACLExpression | Unset): The expression to use to determine the match for this ACL.<br>
        value (str | Unset): The value which indicates a match for this ACL.<br>
        casesensitive (bool | Unset): Enables or disables case-sensitive matching for this ACL.<br>
        not_ (bool | Unset): Enables or disables inverting the context of this ACL.<br>
    """

    parent_id: int
    id: int
    name: str | Unset = UNSET
    expression: HAProxyBackendACLExpression | Unset = UNSET
    value: str | Unset = UNSET
    casesensitive: bool | Unset = UNSET
    not_: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        name = self.name

        expression: str | Unset = UNSET
        if not isinstance(self.expression, Unset):
            expression = self.expression.value

        value = self.value

        casesensitive = self.casesensitive

        not_ = self.not_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if expression is not UNSET:
            field_dict["expression"] = expression
        if value is not UNSET:
            field_dict["value"] = value
        if casesensitive is not UNSET:
            field_dict["casesensitive"] = casesensitive
        if not_ is not UNSET:
            field_dict["not"] = not_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        name = d.pop("name", UNSET)

        _expression = d.pop("expression", UNSET)
        expression: HAProxyBackendACLExpression | Unset
        if isinstance(_expression, Unset):
            expression = UNSET
        else:
            expression = HAProxyBackendACLExpression(_expression)

        value = d.pop("value", UNSET)

        casesensitive = d.pop("casesensitive", UNSET)

        not_ = d.pop("not", UNSET)

        patch_services_ha_proxy_backend_acl_endpoint_json_body = cls(
            parent_id=parent_id,
            id=id,
            name=name,
            expression=expression,
            value=value,
            casesensitive=casesensitive,
            not_=not_,
        )

        patch_services_ha_proxy_backend_acl_endpoint_json_body.additional_properties = d
        return patch_services_ha_proxy_backend_acl_endpoint_json_body

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
