from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_group_scope import UserGroupScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGroup")


@_attrs_define
class UserGroup:
    """
    Attributes:
        name (str | Unset): The name for this user group.<br>
        gid (int | None | Unset): The GID of this user group. This value is automatically assigned and cannot be
            changed.<br> Default: 2002.
        scope (UserGroupScope | Unset): The scope of this user group. Use `local` for user groups that only apply to
            this system. use `remote` for groups that also apply to remote authentication servers. Please note the `system`
            scope is reserved for built-in, system-defined user groups and cannot be assigned manually.<br> Default:
            UserGroupScope.LOCAL.
        description (str | Unset): The description to assign to this user group.<br>
        member (list[str] | Unset): The local user names to assign to this user group.<br>
        priv (list[str] | Unset): The privileges to assign to this user group.<br>
    """

    name: str | Unset = UNSET
    gid: int | None | Unset = 2002
    scope: UserGroupScope | Unset = UserGroupScope.LOCAL
    description: str | Unset = UNSET
    member: list[str] | Unset = UNSET
    priv: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        gid: int | None | Unset
        if isinstance(self.gid, Unset):
            gid = UNSET
        else:
            gid = self.gid

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        description = self.description

        member: list[str] | Unset = UNSET
        if not isinstance(self.member, Unset):
            member = self.member

        priv: list[str] | Unset = UNSET
        if not isinstance(self.priv, Unset):
            priv = self.priv

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if gid is not UNSET:
            field_dict["gid"] = gid
        if scope is not UNSET:
            field_dict["scope"] = scope
        if description is not UNSET:
            field_dict["description"] = description
        if member is not UNSET:
            field_dict["member"] = member
        if priv is not UNSET:
            field_dict["priv"] = priv

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_gid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gid = _parse_gid(d.pop("gid", UNSET))

        _scope = d.pop("scope", UNSET)
        scope: UserGroupScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = UserGroupScope(_scope)

        description = d.pop("description", UNSET)

        member = cast(list[str], d.pop("member", UNSET))

        priv = cast(list[str], d.pop("priv", UNSET))

        user_group = cls(
            name=name,
            gid=gid,
            scope=scope,
            description=description,
            member=member,
            priv=priv,
        )

        user_group.additional_properties = d
        return user_group

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
