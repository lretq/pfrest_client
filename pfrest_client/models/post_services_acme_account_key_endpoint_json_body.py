from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesACMEAccountKeyEndpointJsonBody")


@_attrs_define
class PostServicesACMEAccountKeyEndpointJsonBody:
    """
    Attributes:
        name (str): The name of the ACME account key.<br>
        acmeserver (str): The ACME server this account key will belong to.<br>
        descr (str | Unset): A description of the ACME account key.<br>
        email (str | Unset): The email address associated with the ACME account key.<br>
        accountkey (str | Unset): The RSA private key for the ACME account key.<br>
    """

    name: str
    acmeserver: str
    descr: str | Unset = UNSET
    email: str | Unset = UNSET
    accountkey: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        acmeserver = self.acmeserver

        descr = self.descr

        email = self.email

        accountkey = self.accountkey

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "acmeserver": acmeserver,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if email is not UNSET:
            field_dict["email"] = email
        if accountkey is not UNSET:
            field_dict["accountkey"] = accountkey

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        acmeserver = d.pop("acmeserver")

        descr = d.pop("descr", UNSET)

        email = d.pop("email", UNSET)

        accountkey = d.pop("accountkey", UNSET)

        post_services_acme_account_key_endpoint_json_body = cls(
            name=name,
            acmeserver=acmeserver,
            descr=descr,
            email=email,
            accountkey=accountkey,
        )

        post_services_acme_account_key_endpoint_json_body.additional_properties = d
        return post_services_acme_account_key_endpoint_json_body

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
