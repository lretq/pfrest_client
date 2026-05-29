from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wire_guard_settings_interface_group import WireGuardSettingsInterfaceGroup
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchVPNWireGuardSettingsEndpointDataBody")


@_attrs_define
class PatchVPNWireGuardSettingsEndpointDataBody:
    """
    Attributes:
        enable (bool | Unset): Enables or disables WireGuard on this system. WireGuard cannot be disabled when one or
            more tunnels is assigned to a pfSense interface.<br>
        keep_conf (bool | Unset): Enables or disables keeping the WireGuard configuration when the package is
            uninstalled/reinstalled.<br> Default: True.
        resolve_interval_track (bool | Unset): Enables or disables tracking the 'Aliases Hostnames Resolve Interval'
            value as the `resolve_internal` value instead of specifying a value directly.<br>
        resolve_interval (int | Unset): The interval (in seconds) for re-resolving endpoint host/domain
            names.<br><br>This field is only available when the following conditions are met:<br>- `resolve_interval_track`
            must be equal to `false`<br> Default: 300.
        interface_group (WireGuardSettingsInterfaceGroup | Unset): Configures which WireGuard tunnels are members of the
            WireGuard interface group.<br> Default: WireGuardSettingsInterfaceGroup.ALL.
        hide_secrets (bool | Unset): Enables or disables hiding all secrets (private and pre-shared keys) in the user
            interface.<br>
        hide_peers (bool | Unset): Enables or disables initially hiding all peers in the user interface.<br>
    """

    enable: bool | Unset = UNSET
    keep_conf: bool | Unset = True
    resolve_interval_track: bool | Unset = UNSET
    resolve_interval: int | Unset = 300
    interface_group: WireGuardSettingsInterfaceGroup | Unset = WireGuardSettingsInterfaceGroup.ALL
    hide_secrets: bool | Unset = UNSET
    hide_peers: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        keep_conf = self.keep_conf

        resolve_interval_track = self.resolve_interval_track

        resolve_interval = self.resolve_interval

        interface_group: str | Unset = UNSET
        if not isinstance(self.interface_group, Unset):
            interface_group = self.interface_group.value

        hide_secrets = self.hide_secrets

        hide_peers = self.hide_peers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if keep_conf is not UNSET:
            field_dict["keep_conf"] = keep_conf
        if resolve_interval_track is not UNSET:
            field_dict["resolve_interval_track"] = resolve_interval_track
        if resolve_interval is not UNSET:
            field_dict["resolve_interval"] = resolve_interval
        if interface_group is not UNSET:
            field_dict["interface_group"] = interface_group
        if hide_secrets is not UNSET:
            field_dict["hide_secrets"] = hide_secrets
        if hide_peers is not UNSET:
            field_dict["hide_peers"] = hide_peers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        keep_conf = d.pop("keep_conf", UNSET)

        resolve_interval_track = d.pop("resolve_interval_track", UNSET)

        resolve_interval = d.pop("resolve_interval", UNSET)

        _interface_group = d.pop("interface_group", UNSET)
        interface_group: WireGuardSettingsInterfaceGroup | Unset
        if isinstance(_interface_group, Unset):
            interface_group = UNSET
        else:
            interface_group = WireGuardSettingsInterfaceGroup(_interface_group)

        hide_secrets = d.pop("hide_secrets", UNSET)

        hide_peers = d.pop("hide_peers", UNSET)

        patch_vpn_wire_guard_settings_endpoint_data_body = cls(
            enable=enable,
            keep_conf=keep_conf,
            resolve_interval_track=resolve_interval_track,
            resolve_interval=resolve_interval,
            interface_group=interface_group,
            hide_secrets=hide_secrets,
            hide_peers=hide_peers,
        )

        patch_vpn_wire_guard_settings_endpoint_data_body.additional_properties = d
        return patch_vpn_wire_guard_settings_endpoint_data_body

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
