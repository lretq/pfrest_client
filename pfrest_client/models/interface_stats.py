from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterfaceStats")


@_attrs_define
class InterfaceStats:
    """
    Attributes:
        name (None | str | Unset): The name of the interface.<br>
        descr (None | str | Unset): The description of the interface.<br>
        hwif (None | str | Unset): The hardware interface name of the interface.<br>
        macaddr (None | str | Unset): The MAC address of the interface.<br>
        mtu (None | str | Unset): The MTU of the interface.<br>
        enable (bool | Unset): Whether the interface is enabled.<br>
        status (None | str | Unset): The status of the interface.<br>
        ipaddr (None | str | Unset): The IPv4 address of the interface.<br>
        subnet (None | str | Unset): The IPv4 subnet of the interface.<br>
        linklocal (None | str | Unset): The IPv6 link-local address of the interface.<br>
        ipaddrv6 (None | str | Unset): The IPv6 address of the interface.<br>
        subnetv6 (None | str | Unset): The IPv6 subnet of the interface.<br>
        inerrs (int | Unset): The number of inbound errors on the interface.<br>
        outerrs (int | Unset): The number of outbound errors on the interface.<br>
        collisions (int | Unset): The number of collisions on the interface.<br>
        inbytes (int | Unset): The number of inbound bytes on the interface.<br>
        inbytespass (int | Unset): The number of inbound bytes passed on the interface.<br>
        outbytes (int | Unset): The number of outbound bytes on the interface.<br>
        outbytespass (int | Unset): The number of outbound bytes passed on the interface.<br>
        inpkts (int | Unset): The number of inbound packets on the interface.<br>
        inpktspass (int | Unset): The number of inbound packets passed on the interface.<br>
        outpkts (int | Unset): The number of outbound packets on the interface.<br>
        outpktspass (int | Unset): The number of outbound packets passed on the interface.<br>
        dhcplink (None | str | Unset): The DHCP link status of the interface.<br>
        media (None | str | Unset): The speed/duplex of the interface.<br>
        gateway (None | str | Unset): The IPv4 gateway of the interface.<br>
        gatewayv6 (None | str | Unset): The IPv6 gateway of the interface.<br>
    """

    name: None | str | Unset = UNSET
    descr: None | str | Unset = UNSET
    hwif: None | str | Unset = UNSET
    macaddr: None | str | Unset = UNSET
    mtu: None | str | Unset = UNSET
    enable: bool | Unset = UNSET
    status: None | str | Unset = UNSET
    ipaddr: None | str | Unset = UNSET
    subnet: None | str | Unset = UNSET
    linklocal: None | str | Unset = UNSET
    ipaddrv6: None | str | Unset = UNSET
    subnetv6: None | str | Unset = UNSET
    inerrs: int | Unset = UNSET
    outerrs: int | Unset = UNSET
    collisions: int | Unset = UNSET
    inbytes: int | Unset = UNSET
    inbytespass: int | Unset = UNSET
    outbytes: int | Unset = UNSET
    outbytespass: int | Unset = UNSET
    inpkts: int | Unset = UNSET
    inpktspass: int | Unset = UNSET
    outpkts: int | Unset = UNSET
    outpktspass: int | Unset = UNSET
    dhcplink: None | str | Unset = UNSET
    media: None | str | Unset = UNSET
    gateway: None | str | Unset = UNSET
    gatewayv6: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        descr: None | str | Unset
        if isinstance(self.descr, Unset):
            descr = UNSET
        else:
            descr = self.descr

        hwif: None | str | Unset
        if isinstance(self.hwif, Unset):
            hwif = UNSET
        else:
            hwif = self.hwif

        macaddr: None | str | Unset
        if isinstance(self.macaddr, Unset):
            macaddr = UNSET
        else:
            macaddr = self.macaddr

        mtu: None | str | Unset
        if isinstance(self.mtu, Unset):
            mtu = UNSET
        else:
            mtu = self.mtu

        enable = self.enable

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        ipaddr: None | str | Unset
        if isinstance(self.ipaddr, Unset):
            ipaddr = UNSET
        else:
            ipaddr = self.ipaddr

        subnet: None | str | Unset
        if isinstance(self.subnet, Unset):
            subnet = UNSET
        else:
            subnet = self.subnet

        linklocal: None | str | Unset
        if isinstance(self.linklocal, Unset):
            linklocal = UNSET
        else:
            linklocal = self.linklocal

        ipaddrv6: None | str | Unset
        if isinstance(self.ipaddrv6, Unset):
            ipaddrv6 = UNSET
        else:
            ipaddrv6 = self.ipaddrv6

        subnetv6: None | str | Unset
        if isinstance(self.subnetv6, Unset):
            subnetv6 = UNSET
        else:
            subnetv6 = self.subnetv6

        inerrs = self.inerrs

        outerrs = self.outerrs

        collisions = self.collisions

        inbytes = self.inbytes

        inbytespass = self.inbytespass

        outbytes = self.outbytes

        outbytespass = self.outbytespass

        inpkts = self.inpkts

        inpktspass = self.inpktspass

        outpkts = self.outpkts

        outpktspass = self.outpktspass

        dhcplink: None | str | Unset
        if isinstance(self.dhcplink, Unset):
            dhcplink = UNSET
        else:
            dhcplink = self.dhcplink

        media: None | str | Unset
        if isinstance(self.media, Unset):
            media = UNSET
        else:
            media = self.media

        gateway: None | str | Unset
        if isinstance(self.gateway, Unset):
            gateway = UNSET
        else:
            gateway = self.gateway

        gatewayv6: None | str | Unset
        if isinstance(self.gatewayv6, Unset):
            gatewayv6 = UNSET
        else:
            gatewayv6 = self.gatewayv6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if hwif is not UNSET:
            field_dict["hwif"] = hwif
        if macaddr is not UNSET:
            field_dict["macaddr"] = macaddr
        if mtu is not UNSET:
            field_dict["mtu"] = mtu
        if enable is not UNSET:
            field_dict["enable"] = enable
        if status is not UNSET:
            field_dict["status"] = status
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if linklocal is not UNSET:
            field_dict["linklocal"] = linklocal
        if ipaddrv6 is not UNSET:
            field_dict["ipaddrv6"] = ipaddrv6
        if subnetv6 is not UNSET:
            field_dict["subnetv6"] = subnetv6
        if inerrs is not UNSET:
            field_dict["inerrs"] = inerrs
        if outerrs is not UNSET:
            field_dict["outerrs"] = outerrs
        if collisions is not UNSET:
            field_dict["collisions"] = collisions
        if inbytes is not UNSET:
            field_dict["inbytes"] = inbytes
        if inbytespass is not UNSET:
            field_dict["inbytespass"] = inbytespass
        if outbytes is not UNSET:
            field_dict["outbytes"] = outbytes
        if outbytespass is not UNSET:
            field_dict["outbytespass"] = outbytespass
        if inpkts is not UNSET:
            field_dict["inpkts"] = inpkts
        if inpktspass is not UNSET:
            field_dict["inpktspass"] = inpktspass
        if outpkts is not UNSET:
            field_dict["outpkts"] = outpkts
        if outpktspass is not UNSET:
            field_dict["outpktspass"] = outpktspass
        if dhcplink is not UNSET:
            field_dict["dhcplink"] = dhcplink
        if media is not UNSET:
            field_dict["media"] = media
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if gatewayv6 is not UNSET:
            field_dict["gatewayv6"] = gatewayv6

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_descr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        descr = _parse_descr(d.pop("descr", UNSET))

        def _parse_hwif(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hwif = _parse_hwif(d.pop("hwif", UNSET))

        def _parse_macaddr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        macaddr = _parse_macaddr(d.pop("macaddr", UNSET))

        def _parse_mtu(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mtu = _parse_mtu(d.pop("mtu", UNSET))

        enable = d.pop("enable", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_ipaddr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ipaddr = _parse_ipaddr(d.pop("ipaddr", UNSET))

        def _parse_subnet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subnet = _parse_subnet(d.pop("subnet", UNSET))

        def _parse_linklocal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linklocal = _parse_linklocal(d.pop("linklocal", UNSET))

        def _parse_ipaddrv6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ipaddrv6 = _parse_ipaddrv6(d.pop("ipaddrv6", UNSET))

        def _parse_subnetv6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subnetv6 = _parse_subnetv6(d.pop("subnetv6", UNSET))

        inerrs = d.pop("inerrs", UNSET)

        outerrs = d.pop("outerrs", UNSET)

        collisions = d.pop("collisions", UNSET)

        inbytes = d.pop("inbytes", UNSET)

        inbytespass = d.pop("inbytespass", UNSET)

        outbytes = d.pop("outbytes", UNSET)

        outbytespass = d.pop("outbytespass", UNSET)

        inpkts = d.pop("inpkts", UNSET)

        inpktspass = d.pop("inpktspass", UNSET)

        outpkts = d.pop("outpkts", UNSET)

        outpktspass = d.pop("outpktspass", UNSET)

        def _parse_dhcplink(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhcplink = _parse_dhcplink(d.pop("dhcplink", UNSET))

        def _parse_media(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media = _parse_media(d.pop("media", UNSET))

        def _parse_gateway(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gateway = _parse_gateway(d.pop("gateway", UNSET))

        def _parse_gatewayv6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gatewayv6 = _parse_gatewayv6(d.pop("gatewayv6", UNSET))

        interface_stats = cls(
            name=name,
            descr=descr,
            hwif=hwif,
            macaddr=macaddr,
            mtu=mtu,
            enable=enable,
            status=status,
            ipaddr=ipaddr,
            subnet=subnet,
            linklocal=linklocal,
            ipaddrv6=ipaddrv6,
            subnetv6=subnetv6,
            inerrs=inerrs,
            outerrs=outerrs,
            collisions=collisions,
            inbytes=inbytes,
            inbytespass=inbytespass,
            outbytes=outbytes,
            outbytespass=outbytespass,
            inpkts=inpkts,
            inpktspass=inpktspass,
            outpkts=outpkts,
            outpktspass=outpktspass,
            dhcplink=dhcplink,
            media=media,
            gateway=gateway,
            gatewayv6=gatewayv6,
        )

        interface_stats.additional_properties = d
        return interface_stats

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
