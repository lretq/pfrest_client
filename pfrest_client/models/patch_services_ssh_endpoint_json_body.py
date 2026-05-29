from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ssh_sshdkeyonly import SSHSshdkeyonly
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesSSHEndpointJsonBody")


@_attrs_define
class PatchServicesSSHEndpointJsonBody:
    """
    Attributes:
        enable (bool | Unset): Enable the SSH server on this system.<br>
        port (str | Unset): The TCP port the SSH server will listen on. Valid options are: a TCP/UDP port number<br>
            Default: '22'.
        sshdkeyonly (SSHSshdkeyonly | Unset): The SSH authentication mode to use. Use `enabled` to require public key
            authentication, use both to require both a public key AND a password, or use `null` to allow a password OR a
            public key.<br>
        sshdagentforwarding (bool | Unset): Enable support for ssh-agent forwarding.<br>
    """

    enable: bool | Unset = UNSET
    port: str | Unset = "22"
    sshdkeyonly: SSHSshdkeyonly | Unset = UNSET
    sshdagentforwarding: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        port = self.port

        sshdkeyonly: str | Unset = UNSET
        if not isinstance(self.sshdkeyonly, Unset):
            sshdkeyonly = self.sshdkeyonly.value

        sshdagentforwarding = self.sshdagentforwarding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if port is not UNSET:
            field_dict["port"] = port
        if sshdkeyonly is not UNSET:
            field_dict["sshdkeyonly"] = sshdkeyonly
        if sshdagentforwarding is not UNSET:
            field_dict["sshdagentforwarding"] = sshdagentforwarding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        port = d.pop("port", UNSET)

        _sshdkeyonly = d.pop("sshdkeyonly", UNSET)
        sshdkeyonly: SSHSshdkeyonly | Unset
        if isinstance(_sshdkeyonly, Unset):
            sshdkeyonly = UNSET
        else:
            sshdkeyonly = SSHSshdkeyonly(_sshdkeyonly)

        sshdagentforwarding = d.pop("sshdagentforwarding", UNSET)

        patch_services_ssh_endpoint_json_body = cls(
            enable=enable,
            port=port,
            sshdkeyonly=sshdkeyonly,
            sshdagentforwarding=sshdagentforwarding,
        )

        patch_services_ssh_endpoint_json_body.additional_properties = d
        return patch_services_ssh_endpoint_json_body

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
