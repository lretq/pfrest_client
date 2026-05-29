from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.firewall_alias_type import FirewallAliasType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FirewallAlias")


@_attrs_define
class FirewallAlias:
    """
    Attributes:
        name (str | Unset): Sets the name for the alias. This name must be unique from all other aliases.<br>
        type_ (FirewallAliasType | Unset): Sets the type of alias this object will be. This directly impacts what values
            can be
                            specified in the `address` field.<br>
        descr (str | Unset): Sets a description to help specify the purpose or contents of the alias.<br>
        address (list[str] | Unset): Sets the host, network or port entries for the alias. When `type` is set to `host`,
            each
                            entry must be a valid IP address or FQDN. When `type` is set to `network`, each entry must be a
            valid
                            network CIDR or FQDN. When `type` is set to `port`, each entry must be a valid port or port
            range. You
                            may also specify an existing alias's `name` as an entry to created nested aliases.<br>
        detail (list[str] | Unset): Sets descriptions for each alias `address`. Values must match the order of the
            `address`
                            value it relates to. For example, the first value specified here is the description for the
            first
                            value specified in the `address` field. This value cannot contain <br>
    """

    name: str | Unset = UNSET
    type_: FirewallAliasType | Unset = UNSET
    descr: str | Unset = UNSET
    address: list[str] | Unset = UNSET
    detail: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        descr = self.descr

        address: list[str] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address

        detail: list[str] | Unset = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if descr is not UNSET:
            field_dict["descr"] = descr
        if address is not UNSET:
            field_dict["address"] = address
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FirewallAliasType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FirewallAliasType(_type_)

        descr = d.pop("descr", UNSET)

        address = cast(list[str], d.pop("address", UNSET))

        detail = cast(list[str], d.pop("detail", UNSET))

        firewall_alias = cls(
            name=name,
            type_=type_,
            descr=descr,
            address=address,
            detail=detail,
        )

        firewall_alias.additional_properties = d
        return firewall_alias

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
