from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wire_guard_peer_allowedips_item import WireGuardPeerAllowedipsItem


T = TypeVar("T", bound="WireGuardPeer")


@_attrs_define
class WireGuardPeer:
    """
    Attributes:
        enabled (bool | Unset): Enables or disables this WireGuard peer.<br>
        tun (str | Unset): The WireGuard tunnel for this peer.<br> Default: 'unassigned'.
        endpoint (None | str | Unset): The IP address or hostname of the remote peer. Set to `null` to make this a
            dynamic endpoint.<br>
        port (str | Unset): The port used by the remote peer. Valid options are: a TCP/UDP port number<br><br>This field
            is only available when the following conditions are met:<br>- `endpoint` must not be equal to `NULL`<br>
            Default: '51820'.
        descr (str | Unset): The description for this peer.<br>
        persistentkeepalive (int | None | Unset): The interval (in seconds) for Keep Alive packets sent to this peer.
            Set to `null` to disable.<br>
        publickey (str | Unset): The public key for this peer.<br>
        presharedkey (None | str | Unset): The pre-shared key for this tunnel.<br>
        allowedips (list[WireGuardPeerAllowedipsItem] | Unset): The allowed IP/subnets for this WireGuard peer.<br>
    """

    enabled: bool | Unset = UNSET
    tun: str | Unset = "unassigned"
    endpoint: None | str | Unset = UNSET
    port: str | Unset = "51820"
    descr: str | Unset = UNSET
    persistentkeepalive: int | None | Unset = UNSET
    publickey: str | Unset = UNSET
    presharedkey: None | str | Unset = UNSET
    allowedips: list[WireGuardPeerAllowedipsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        tun = self.tun

        endpoint: None | str | Unset
        if isinstance(self.endpoint, Unset):
            endpoint = UNSET
        else:
            endpoint = self.endpoint

        port = self.port

        descr = self.descr

        persistentkeepalive: int | None | Unset
        if isinstance(self.persistentkeepalive, Unset):
            persistentkeepalive = UNSET
        else:
            persistentkeepalive = self.persistentkeepalive

        publickey = self.publickey

        presharedkey: None | str | Unset
        if isinstance(self.presharedkey, Unset):
            presharedkey = UNSET
        else:
            presharedkey = self.presharedkey

        allowedips: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allowedips, Unset):
            allowedips = []
            for allowedips_item_data in self.allowedips:
                allowedips_item = allowedips_item_data.to_dict()
                allowedips.append(allowedips_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if tun is not UNSET:
            field_dict["tun"] = tun
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if port is not UNSET:
            field_dict["port"] = port
        if descr is not UNSET:
            field_dict["descr"] = descr
        if persistentkeepalive is not UNSET:
            field_dict["persistentkeepalive"] = persistentkeepalive
        if publickey is not UNSET:
            field_dict["publickey"] = publickey
        if presharedkey is not UNSET:
            field_dict["presharedkey"] = presharedkey
        if allowedips is not UNSET:
            field_dict["allowedips"] = allowedips

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wire_guard_peer_allowedips_item import WireGuardPeerAllowedipsItem

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        tun = d.pop("tun", UNSET)

        def _parse_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint = _parse_endpoint(d.pop("endpoint", UNSET))

        port = d.pop("port", UNSET)

        descr = d.pop("descr", UNSET)

        def _parse_persistentkeepalive(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        persistentkeepalive = _parse_persistentkeepalive(d.pop("persistentkeepalive", UNSET))

        publickey = d.pop("publickey", UNSET)

        def _parse_presharedkey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        presharedkey = _parse_presharedkey(d.pop("presharedkey", UNSET))

        _allowedips = d.pop("allowedips", UNSET)
        allowedips: list[WireGuardPeerAllowedipsItem] | Unset = UNSET
        if _allowedips is not UNSET:
            allowedips = []
            for allowedips_item_data in _allowedips:
                allowedips_item = WireGuardPeerAllowedipsItem.from_dict(allowedips_item_data)

                allowedips.append(allowedips_item)

        wire_guard_peer = cls(
            enabled=enabled,
            tun=tun,
            endpoint=endpoint,
            port=port,
            descr=descr,
            persistentkeepalive=persistentkeepalive,
            publickey=publickey,
            presharedkey=presharedkey,
            allowedips=allowedips,
        )

        wire_guard_peer.additional_properties = d
        return wire_guard_peer

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
