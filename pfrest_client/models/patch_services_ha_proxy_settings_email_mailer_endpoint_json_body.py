from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesHAProxySettingsEmailMailerEndpointJsonBody")


@_attrs_define
class PatchServicesHAProxySettingsEmailMailerEndpointJsonBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        name (str | Unset): The descriptive name for this mail server.<br>
        mailserver (str | Unset): The IP or hostname of the mail server.<br>
        mailserverport (str | Unset): The port used by this mail server. Valid options are: a TCP/UDP port number<br>
            Default: '53'.
    """

    id: int
    name: str | Unset = UNSET
    mailserver: str | Unset = UNSET
    mailserverport: str | Unset = "53"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        mailserver = self.mailserver

        mailserverport = self.mailserverport

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if mailserver is not UNSET:
            field_dict["mailserver"] = mailserver
        if mailserverport is not UNSET:
            field_dict["mailserverport"] = mailserverport

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        mailserver = d.pop("mailserver", UNSET)

        mailserverport = d.pop("mailserverport", UNSET)

        patch_services_ha_proxy_settings_email_mailer_endpoint_json_body = cls(
            id=id,
            name=name,
            mailserver=mailserver,
            mailserverport=mailserverport,
        )

        patch_services_ha_proxy_settings_email_mailer_endpoint_json_body.additional_properties = d
        return patch_services_ha_proxy_settings_email_mailer_endpoint_json_body

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
