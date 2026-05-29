from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_server_status_conns_type_0_item import OpenVPNServerStatusConnsType0Item
    from ..models.open_vpn_server_status_routes_type_0_item import OpenVPNServerStatusRoutesType0Item


T = TypeVar("T", bound="OpenVPNServerStatus")


@_attrs_define
class OpenVPNServerStatus:
    """
    Attributes:
        name (None | str | Unset): The name of the OpenVPN server.<br>
        mode (None | str | Unset): The mode of the OpenVPN server.<br>
        port (None | str | Unset): The port number of the OpenVPN server. Valid options are: a TCP/UDP port number<br>
        vpnid (int | None | Unset): The VPN ID of the OpenVPN server this status corresponds to.<br>
        mgmt (None | str | Unset): The management interface of the OpenVPN server.<br>
        conns (list[OpenVPNServerStatusConnsType0Item] | None | Unset): The current connections to the OpenVPN
            server.<br>
        routes (list[OpenVPNServerStatusRoutesType0Item] | None | Unset): The current routes of the OpenVPN server.<br>
    """

    name: None | str | Unset = UNSET
    mode: None | str | Unset = UNSET
    port: None | str | Unset = UNSET
    vpnid: int | None | Unset = UNSET
    mgmt: None | str | Unset = UNSET
    conns: list[OpenVPNServerStatusConnsType0Item] | None | Unset = UNSET
    routes: list[OpenVPNServerStatusRoutesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        port: None | str | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        vpnid: int | None | Unset
        if isinstance(self.vpnid, Unset):
            vpnid = UNSET
        else:
            vpnid = self.vpnid

        mgmt: None | str | Unset
        if isinstance(self.mgmt, Unset):
            mgmt = UNSET
        else:
            mgmt = self.mgmt

        conns: list[dict[str, Any]] | None | Unset
        if isinstance(self.conns, Unset):
            conns = UNSET
        elif isinstance(self.conns, list):
            conns = []
            for conns_type_0_item_data in self.conns:
                conns_type_0_item = conns_type_0_item_data.to_dict()
                conns.append(conns_type_0_item)

        else:
            conns = self.conns

        routes: list[dict[str, Any]] | None | Unset
        if isinstance(self.routes, Unset):
            routes = UNSET
        elif isinstance(self.routes, list):
            routes = []
            for routes_type_0_item_data in self.routes:
                routes_type_0_item = routes_type_0_item_data.to_dict()
                routes.append(routes_type_0_item)

        else:
            routes = self.routes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if port is not UNSET:
            field_dict["port"] = port
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if mgmt is not UNSET:
            field_dict["mgmt"] = mgmt
        if conns is not UNSET:
            field_dict["conns"] = conns
        if routes is not UNSET:
            field_dict["routes"] = routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_vpn_server_status_conns_type_0_item import OpenVPNServerStatusConnsType0Item
        from ..models.open_vpn_server_status_routes_type_0_item import OpenVPNServerStatusRoutesType0Item

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_vpnid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vpnid = _parse_vpnid(d.pop("vpnid", UNSET))

        def _parse_mgmt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mgmt = _parse_mgmt(d.pop("mgmt", UNSET))

        def _parse_conns(data: object) -> list[OpenVPNServerStatusConnsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conns_type_0 = []
                _conns_type_0 = data
                for conns_type_0_item_data in _conns_type_0:
                    conns_type_0_item = OpenVPNServerStatusConnsType0Item.from_dict(conns_type_0_item_data)

                    conns_type_0.append(conns_type_0_item)

                return conns_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[OpenVPNServerStatusConnsType0Item] | None | Unset, data)

        conns = _parse_conns(d.pop("conns", UNSET))

        def _parse_routes(data: object) -> list[OpenVPNServerStatusRoutesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                routes_type_0 = []
                _routes_type_0 = data
                for routes_type_0_item_data in _routes_type_0:
                    routes_type_0_item = OpenVPNServerStatusRoutesType0Item.from_dict(routes_type_0_item_data)

                    routes_type_0.append(routes_type_0_item)

                return routes_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[OpenVPNServerStatusRoutesType0Item] | None | Unset, data)

        routes = _parse_routes(d.pop("routes", UNSET))

        open_vpn_server_status = cls(
            name=name,
            mode=mode,
            port=port,
            vpnid=vpnid,
            mgmt=mgmt,
            conns=conns,
            routes=routes,
        )

        open_vpn_server_status.additional_properties = d
        return open_vpn_server_status

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
