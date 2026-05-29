from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.web_gui_settings_protocol import WebGUISettingsProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebGUISettings")


@_attrs_define
class WebGUISettings:
    """
    Attributes:
        protocol (WebGUISettingsProtocol | Unset): The protocol to use for the web GUI.<br> Default:
            WebGUISettingsProtocol.HTTPS.
        port (str | Unset): The port on which the web GUI listens. Valid options are: a TCP/UDP port number<br> Default:
            '443'.
        sslcertref (str | Unset): The SSL/TLS certificate to use for the web GUI.<br>
    """

    protocol: WebGUISettingsProtocol | Unset = WebGUISettingsProtocol.HTTPS
    port: str | Unset = "443"
    sslcertref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        port = self.port

        sslcertref = self.sslcertref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if port is not UNSET:
            field_dict["port"] = port
        if sslcertref is not UNSET:
            field_dict["sslcertref"] = sslcertref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _protocol = d.pop("protocol", UNSET)
        protocol: WebGUISettingsProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = WebGUISettingsProtocol(_protocol)

        port = d.pop("port", UNSET)

        sslcertref = d.pop("sslcertref", UNSET)

        web_gui_settings = cls(
            protocol=protocol,
            port=port,
            sslcertref=sslcertref,
        )

        web_gui_settings.additional_properties = d
        return web_gui_settings

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
