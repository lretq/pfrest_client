from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesHAProxySettingsEmailMailerEndpointJsonBody")


@_attrs_define
class PostServicesHAProxySettingsEmailMailerEndpointJsonBody:
    """
    Attributes:
        name (str): The descriptive name for this mail server.<br>
        mailserver (str): The IP or hostname of the mail server.<br>
        mailserverport (str | Unset): The port used by this mail server. Valid options are: a TCP/UDP port number<br>
            Default: '53'.
    """

    name: str
    mailserver: str
    mailserverport: str | Unset = "53"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mailserver = self.mailserver

        mailserverport = self.mailserverport

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "mailserver": mailserver,
            }
        )
        if mailserverport is not UNSET:
            field_dict["mailserverport"] = mailserverport

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        mailserver = d.pop("mailserver")

        mailserverport = d.pop("mailserverport", UNSET)

        post_services_ha_proxy_settings_email_mailer_endpoint_json_body = cls(
            name=name,
            mailserver=mailserver,
            mailserverport=mailserverport,
        )

        post_services_ha_proxy_settings_email_mailer_endpoint_json_body.additional_properties = d
        return post_services_ha_proxy_settings_email_mailer_endpoint_json_body

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
