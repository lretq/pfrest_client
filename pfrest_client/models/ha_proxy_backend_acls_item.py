from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_backend_acl_expression import HAProxyBackendACLExpression
from ..types import UNSET, Unset

T = TypeVar("T", bound="HAProxyBackendAclsItem")


@_attrs_define
class HAProxyBackendAclsItem:
    """
    Attributes:
        name (str): The unique name for this backend ACL.<br>
        expression (HAProxyBackendACLExpression): The expression to use to determine the match for this ACL.<br>
        value (str): The value which indicates a match for this ACL.<br>
        casesensitive (bool | Unset): Enables or disables case-sensitive matching for this ACL.<br>
        not_ (bool | Unset): Enables or disables inverting the context of this ACL.<br>
    """

    name: str
    expression: HAProxyBackendACLExpression
    value: str
    casesensitive: bool | Unset = UNSET
    not_: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        expression = self.expression.value

        value = self.value

        casesensitive = self.casesensitive

        not_ = self.not_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "expression": expression,
                "value": value,
            }
        )
        if casesensitive is not UNSET:
            field_dict["casesensitive"] = casesensitive
        if not_ is not UNSET:
            field_dict["not"] = not_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        expression = HAProxyBackendACLExpression(d.pop("expression"))

        value = d.pop("value")

        casesensitive = d.pop("casesensitive", UNSET)

        not_ = d.pop("not", UNSET)

        ha_proxy_backend_acls_item = cls(
            name=name,
            expression=expression,
            value=value,
            casesensitive=casesensitive,
            not_=not_,
        )

        ha_proxy_backend_acls_item.additional_properties = d
        return ha_proxy_backend_acls_item

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
