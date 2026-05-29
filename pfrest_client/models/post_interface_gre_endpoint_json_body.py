from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostInterfaceGREEndpointJsonBody")


@_attrs_define
class PostInterfaceGREEndpointJsonBody:
    """
    Attributes:
        if_ (str): The pfSense interface interface serving as the local address to be used for the GRE tunnel.<br>
        remote_addr (str): The remote address to use for the GRE tunnel.<br>
        tunnel_remote_addr (str): The remote IPv4 address to use for the GRE tunnel.<br><br>This field is only available
            when the following conditions are met:<br>- `tunnel_local_addr` must not be equal to `NULL`<br>
        tunnel_remote_addr6 (str): The remote IPv6 address to use for the GRE tunnel.<br><br>This field is only
            available when the following conditions are met:<br>- `tunnel_local_addr6` must not be equal to `NULL`<br>
        greif (None | str | Unset): The real interface name for this GRE interface.<br>
        descr (str | Unset): A description for this GRE interface.<br>
        add_static_route (bool | Unset): Whether to add an explicit static route for the remote inner tunnel
            address/subnet via the local tunnel address.<br>
        tunnel_local_addr (None | str | Unset): The local IPv4 address to use for the GRE tunnel.<br>
        tunnel_remote_net (int | Unset): The remote IPv4 subnet bitmask to use for the GRE tunnel.<br><br>This field is
            only available when the following conditions are met:<br>- `tunnel_local_addr` must not be equal to `NULL`<br>
            Default: 32.
        tunnel_local_addr6 (None | str | Unset): The local IPv6 address to use for the GRE tunnel.<br>
        tunnel_remote_net6 (int | Unset): The remote IPv6 subnet bitmask to use for the GRE tunnel.<br><br>This field is
            only available when the following conditions are met:<br>- `tunnel_local_addr6` must not be equal to `NULL`<br>
            Default: 128.
    """

    if_: str
    remote_addr: str
    tunnel_remote_addr: str
    tunnel_remote_addr6: str
    greif: None | str | Unset = UNSET
    descr: str | Unset = UNSET
    add_static_route: bool | Unset = UNSET
    tunnel_local_addr: None | str | Unset = UNSET
    tunnel_remote_net: int | Unset = 32
    tunnel_local_addr6: None | str | Unset = UNSET
    tunnel_remote_net6: int | Unset = 128
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if_ = self.if_

        remote_addr = self.remote_addr

        tunnel_remote_addr = self.tunnel_remote_addr

        tunnel_remote_addr6 = self.tunnel_remote_addr6

        greif: None | str | Unset
        if isinstance(self.greif, Unset):
            greif = UNSET
        else:
            greif = self.greif

        descr = self.descr

        add_static_route = self.add_static_route

        tunnel_local_addr: None | str | Unset
        if isinstance(self.tunnel_local_addr, Unset):
            tunnel_local_addr = UNSET
        else:
            tunnel_local_addr = self.tunnel_local_addr

        tunnel_remote_net = self.tunnel_remote_net

        tunnel_local_addr6: None | str | Unset
        if isinstance(self.tunnel_local_addr6, Unset):
            tunnel_local_addr6 = UNSET
        else:
            tunnel_local_addr6 = self.tunnel_local_addr6

        tunnel_remote_net6 = self.tunnel_remote_net6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if": if_,
                "remote_addr": remote_addr,
                "tunnel_remote_addr": tunnel_remote_addr,
                "tunnel_remote_addr6": tunnel_remote_addr6,
            }
        )
        if greif is not UNSET:
            field_dict["greif"] = greif
        if descr is not UNSET:
            field_dict["descr"] = descr
        if add_static_route is not UNSET:
            field_dict["add_static_route"] = add_static_route
        if tunnel_local_addr is not UNSET:
            field_dict["tunnel_local_addr"] = tunnel_local_addr
        if tunnel_remote_net is not UNSET:
            field_dict["tunnel_remote_net"] = tunnel_remote_net
        if tunnel_local_addr6 is not UNSET:
            field_dict["tunnel_local_addr6"] = tunnel_local_addr6
        if tunnel_remote_net6 is not UNSET:
            field_dict["tunnel_remote_net6"] = tunnel_remote_net6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        if_ = d.pop("if")

        remote_addr = d.pop("remote_addr")

        tunnel_remote_addr = d.pop("tunnel_remote_addr")

        tunnel_remote_addr6 = d.pop("tunnel_remote_addr6")

        def _parse_greif(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        greif = _parse_greif(d.pop("greif", UNSET))

        descr = d.pop("descr", UNSET)

        add_static_route = d.pop("add_static_route", UNSET)

        def _parse_tunnel_local_addr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tunnel_local_addr = _parse_tunnel_local_addr(d.pop("tunnel_local_addr", UNSET))

        tunnel_remote_net = d.pop("tunnel_remote_net", UNSET)

        def _parse_tunnel_local_addr6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tunnel_local_addr6 = _parse_tunnel_local_addr6(d.pop("tunnel_local_addr6", UNSET))

        tunnel_remote_net6 = d.pop("tunnel_remote_net6", UNSET)

        post_interface_gre_endpoint_json_body = cls(
            if_=if_,
            remote_addr=remote_addr,
            tunnel_remote_addr=tunnel_remote_addr,
            tunnel_remote_addr6=tunnel_remote_addr6,
            greif=greif,
            descr=descr,
            add_static_route=add_static_route,
            tunnel_local_addr=tunnel_local_addr,
            tunnel_remote_net=tunnel_remote_net,
            tunnel_local_addr6=tunnel_local_addr6,
            tunnel_remote_net6=tunnel_remote_net6,
        )

        post_interface_gre_endpoint_json_body.additional_properties = d
        return post_interface_gre_endpoint_json_body

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
