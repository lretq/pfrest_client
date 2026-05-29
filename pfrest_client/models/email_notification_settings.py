from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.email_notification_settings_authentication_mechanism import (
    EmailNotificationSettingsAuthenticationMechanism,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailNotificationSettings")


@_attrs_define
class EmailNotificationSettings:
    """
    Attributes:
        disable (bool | Unset): Disables SMTP notifications.<br>
        ipaddress (str | Unset): The IP address or hostname of the SMTP server.<br>
        port (str | Unset): The port number of the SMTP server. Valid options are: a TCP/UDP port number<br> Default:
            '25'.
        timeout (int | Unset): The timeout (in seconds) for the SMTP connection.<br> Default: 20.
        ssl (bool | Unset): Enables or disables SSL/TLS for the SMTP connection.<br>
        sslvalidate (bool | Unset): Enables or disables SSL/TLS certificate validation for the SMTP connection.<br>
            Default: True.
        fromaddress (str | Unset): The email address to use as the "From" address in notifications.<br>
        notifyemailaddress (str | Unset): The email address to send notifications to.<br>
        authentication_mechanism (EmailNotificationSettingsAuthenticationMechanism | Unset): The authentication
            mechanism to use for the SMTP connection.<br> Default: EmailNotificationSettingsAuthenticationMechanism.PLAIN.
        username (str | Unset): The username to use for SMTP authentication.<br><br>This field is only available when
            the following conditions are met:<br>- `authentication_mechanism` must be equal to `'LOGIN'`<br>
        password (str | Unset): The password to use for SMTP authentication.<br><br>This field is only available when
            the following conditions are met:<br>- `authentication_mechanism` must be equal to `'LOGIN'`<br>
    """

    disable: bool | Unset = UNSET
    ipaddress: str | Unset = UNSET
    port: str | Unset = "25"
    timeout: int | Unset = 20
    ssl: bool | Unset = UNSET
    sslvalidate: bool | Unset = True
    fromaddress: str | Unset = UNSET
    notifyemailaddress: str | Unset = UNSET
    authentication_mechanism: EmailNotificationSettingsAuthenticationMechanism | Unset = (
        EmailNotificationSettingsAuthenticationMechanism.PLAIN
    )
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable = self.disable

        ipaddress = self.ipaddress

        port = self.port

        timeout = self.timeout

        ssl = self.ssl

        sslvalidate = self.sslvalidate

        fromaddress = self.fromaddress

        notifyemailaddress = self.notifyemailaddress

        authentication_mechanism: str | Unset = UNSET
        if not isinstance(self.authentication_mechanism, Unset):
            authentication_mechanism = self.authentication_mechanism.value

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable is not UNSET:
            field_dict["disable"] = disable
        if ipaddress is not UNSET:
            field_dict["ipaddress"] = ipaddress
        if port is not UNSET:
            field_dict["port"] = port
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if ssl is not UNSET:
            field_dict["ssl"] = ssl
        if sslvalidate is not UNSET:
            field_dict["sslvalidate"] = sslvalidate
        if fromaddress is not UNSET:
            field_dict["fromaddress"] = fromaddress
        if notifyemailaddress is not UNSET:
            field_dict["notifyemailaddress"] = notifyemailaddress
        if authentication_mechanism is not UNSET:
            field_dict["authentication_mechanism"] = authentication_mechanism
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disable = d.pop("disable", UNSET)

        ipaddress = d.pop("ipaddress", UNSET)

        port = d.pop("port", UNSET)

        timeout = d.pop("timeout", UNSET)

        ssl = d.pop("ssl", UNSET)

        sslvalidate = d.pop("sslvalidate", UNSET)

        fromaddress = d.pop("fromaddress", UNSET)

        notifyemailaddress = d.pop("notifyemailaddress", UNSET)

        _authentication_mechanism = d.pop("authentication_mechanism", UNSET)
        authentication_mechanism: EmailNotificationSettingsAuthenticationMechanism | Unset
        if isinstance(_authentication_mechanism, Unset):
            authentication_mechanism = UNSET
        else:
            authentication_mechanism = EmailNotificationSettingsAuthenticationMechanism(_authentication_mechanism)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        email_notification_settings = cls(
            disable=disable,
            ipaddress=ipaddress,
            port=port,
            timeout=timeout,
            ssl=ssl,
            sslvalidate=sslvalidate,
            fromaddress=fromaddress,
            notifyemailaddress=notifyemailaddress,
            authentication_mechanism=authentication_mechanism,
            username=username,
            password=password,
        )

        email_notification_settings.additional_properties = d
        return email_notification_settings

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
