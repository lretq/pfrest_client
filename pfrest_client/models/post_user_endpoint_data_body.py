from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUserEndpointDataBody")


@_attrs_define
class PostUserEndpointDataBody:
    """
    Attributes:
        name (str): The username of this local user.<br>
        password (str): The password of this local user.<br>
        uid (int | None | Unset): The UID of this local user. This value is automatically assigned and cannot be
            changed.<br> Default: 2006.
        scope (None | str | Unset): The scope of this local user. This value is automatically assigned and cannot be
            changed.<br> Default: 'user'.
        priv (list[str] | Unset): The privileges assigned to this local user.<br>
        disabled (bool | Unset): Disable this local user.<br>
        descr (str | Unset): The full descriptive name for this local user.<br>
        expires (str | Unset): The expiration date for this user in mm/dd/YYYY format. Use empty string for no
            expiration<br>
        cert (list[str] | Unset): The user certificates to assign this user. Items must be existing certificate
            `refid`s.<br>
        authorizedkeys (str | Unset): The SSH authorized keys to assign this user.<br>
        ipsecpsk (str | Unset): The IPsec pre-shared key to assign this user.<br>
    """

    name: str
    password: str
    uid: int | None | Unset = 2006
    scope: None | str | Unset = "user"
    priv: list[str] | Unset = UNSET
    disabled: bool | Unset = UNSET
    descr: str | Unset = UNSET
    expires: str | Unset = UNSET
    cert: list[str] | Unset = UNSET
    authorizedkeys: str | Unset = UNSET
    ipsecpsk: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        password = self.password

        uid: int | None | Unset
        if isinstance(self.uid, Unset):
            uid = UNSET
        else:
            uid = self.uid

        scope: None | str | Unset
        if isinstance(self.scope, Unset):
            scope = UNSET
        else:
            scope = self.scope

        priv: list[str] | Unset = UNSET
        if not isinstance(self.priv, Unset):
            priv = self.priv

        disabled = self.disabled

        descr = self.descr

        expires = self.expires

        cert: list[str] | Unset = UNSET
        if not isinstance(self.cert, Unset):
            cert = self.cert

        authorizedkeys = self.authorizedkeys

        ipsecpsk = self.ipsecpsk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "password": password,
            }
        )
        if uid is not UNSET:
            field_dict["uid"] = uid
        if scope is not UNSET:
            field_dict["scope"] = scope
        if priv is not UNSET:
            field_dict["priv"] = priv
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if descr is not UNSET:
            field_dict["descr"] = descr
        if expires is not UNSET:
            field_dict["expires"] = expires
        if cert is not UNSET:
            field_dict["cert"] = cert
        if authorizedkeys is not UNSET:
            field_dict["authorizedkeys"] = authorizedkeys
        if ipsecpsk is not UNSET:
            field_dict["ipsecpsk"] = ipsecpsk

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        password = d.pop("password")

        def _parse_uid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        uid = _parse_uid(d.pop("uid", UNSET))

        def _parse_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scope = _parse_scope(d.pop("scope", UNSET))

        priv = cast(list[str], d.pop("priv", UNSET))

        disabled = d.pop("disabled", UNSET)

        descr = d.pop("descr", UNSET)

        expires = d.pop("expires", UNSET)

        cert = cast(list[str], d.pop("cert", UNSET))

        authorizedkeys = d.pop("authorizedkeys", UNSET)

        ipsecpsk = d.pop("ipsecpsk", UNSET)

        post_user_endpoint_data_body = cls(
            name=name,
            password=password,
            uid=uid,
            scope=scope,
            priv=priv,
            disabled=disabled,
            descr=descr,
            expires=expires,
            cert=cert,
            authorizedkeys=authorizedkeys,
            ipsecpsk=ipsecpsk,
        )

        post_user_endpoint_data_body.additional_properties = d
        return post_user_endpoint_data_body

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
