from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wire_guard_tunnel_addresses_item import WireGuardTunnelAddressesItem


T = TypeVar("T", bound="PutVPNWireGuardTunnelsEndpointDataBodyItem")


@_attrs_define
class PutVPNWireGuardTunnelsEndpointDataBodyItem:
    """
    Attributes:
        privatekey (str): The private key for this tunnel.<br>
        name (None | str | Unset): The name of the WireGuard interface. This value is automatically assigned by the
            system and cannot be changed.<br>
        enabled (bool | Unset): Enables or disables this tunnels and any associated peers.<br> Default: True.
        descr (str | Unset): A description for this WireGuard tunnel.<br>
        listenport (str | Unset): The port WireGuard will listen on for this tunnel. Valid options are: a TCP/UDP port
            number<br> Default: '51820'.
        publickey (None | str | Unset): The public key for this tunnel. This value is automatically derived from the
            `privatekey` value and cannot be set manually.<br>
        mtu (int | Unset): The MTU for this WireGuard tunnel interface. This value is ignored if this tunnel is assigned
            as a pfSense interface.<br> Default: 1420.
        addresses (list[WireGuardTunnelAddressesItem] | Unset): The IPv4 or IPv6 addresses to assign this WireGuard
            tunnel interface. This field is ignored if this tunnel interface is assigned to an existing pfSense interface
            object.<br>
    """

    privatekey: str
    name: None | str | Unset = UNSET
    enabled: bool | Unset = True
    descr: str | Unset = UNSET
    listenport: str | Unset = "51820"
    publickey: None | str | Unset = UNSET
    mtu: int | Unset = 1420
    addresses: list[WireGuardTunnelAddressesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        privatekey = self.privatekey

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        enabled = self.enabled

        descr = self.descr

        listenport = self.listenport

        publickey: None | str | Unset
        if isinstance(self.publickey, Unset):
            publickey = UNSET
        else:
            publickey = self.publickey

        mtu = self.mtu

        addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "privatekey": privatekey,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if descr is not UNSET:
            field_dict["descr"] = descr
        if listenport is not UNSET:
            field_dict["listenport"] = listenport
        if publickey is not UNSET:
            field_dict["publickey"] = publickey
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if addresses is not UNSET:
            field_dict["addresses"] = addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wire_guard_tunnel_addresses_item import WireGuardTunnelAddressesItem

        d = dict(src_dict)
        privatekey = d.pop("privatekey")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        enabled = d.pop("enabled", UNSET)

        descr = d.pop("descr", UNSET)

        listenport = d.pop("listenport", UNSET)

        def _parse_publickey(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publickey = _parse_publickey(d.pop("publickey", UNSET))

        mtu = d.pop("mtu", UNSET)

        _addresses = d.pop("addresses", UNSET)
        addresses: list[WireGuardTunnelAddressesItem] | Unset = UNSET
        if _addresses is not UNSET:
            addresses = []
            for addresses_item_data in _addresses:
                addresses_item = WireGuardTunnelAddressesItem.from_dict(addresses_item_data)

                addresses.append(addresses_item)

        put_vpn_wire_guard_tunnels_endpoint_data_body_item = cls(
            privatekey=privatekey,
            name=name,
            enabled=enabled,
            descr=descr,
            listenport=listenport,
            publickey=publickey,
            mtu=mtu,
            addresses=addresses,
        )

        put_vpn_wire_guard_tunnels_endpoint_data_body_item.additional_properties = d
        return put_vpn_wire_guard_tunnels_endpoint_data_body_item

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
