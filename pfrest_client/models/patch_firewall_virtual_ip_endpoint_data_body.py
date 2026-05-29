from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.virtual_ip_carp_mode import VirtualIPCarpMode
from ..models.virtual_ip_mode import VirtualIPMode
from ..models.virtual_ip_type import VirtualIPType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchFirewallVirtualIPEndpointDataBody")


@_attrs_define
class PatchFirewallVirtualIPEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        uniqid (None | str | Unset): The unique ID for this virtual IP.<br>
        mode (VirtualIPMode | Unset): The virtual IP mode to use for this virtual IP.<br>
        interface (str | Unset): The interface this virtual IP will apply to.<br>
        type_ (VirtualIPType | Unset): The virtual IP scope type. The `network` option is only applicable to the
            `proxyarp` and `other` virtual IP modes.<br> Default: VirtualIPType.SINGLE.
        subnet (str | Unset): The address for this virtual IP.<br>
        subnet_bits (int | Unset): The subnet bits for this virtual IP. For `proxyarp` and `other` virtual IPs, this
            value specifies a block of many IP address. For all other virtual IP modes, this specifies the subnet mask<br>
        descr (str | Unset): A description for administrative reference<br>
        noexpand (bool | Unset): Disable expansion of this entry into IPs on NAT lists (e.g. 192.168.1.0/24 expands to
            256 entries.)<br><br>This field is only available when the following conditions are met:<br>- `mode` must be one
            of [ proxyarp, other ]<br>
        vhid (int | Unset): The VHID group that the machines will share.<br><br>This field is only available when the
            following conditions are met:<br>- `mode` must be equal to `'carp'`<br>
        advbase (int | Unset): The base frequency that this machine will advertise.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be equal to `'carp'`<br> Default: 1.
        advskew (int | Unset): The frequency skew that this machine will advertise.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be equal to `'carp'`<br>
        password (str | Unset): The VHID group password shared by all CARP members.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be equal to `'carp'`<br>
        carp_status (None | str | Unset): The current CARP status of this virtual IP. This will display show whether
            this CARP node is the primary or backup peer.<br><br>This field is only available when the following conditions
            are met:<br>- `mode` must be equal to `'carp'`<br>
        carp_mode (VirtualIPCarpMode | Unset): The CARP mode to use for this virtual IP. Please note this field is
            exclusive to pfSense Plus and has no effect on CE.<br><br>This field is only available when the following
            conditions are met:<br>- `mode` must be equal to `'carp'`<br> Default: VirtualIPCarpMode.MCAST.
        carp_peer (str | Unset): The IP address of the CARP peer. Please note this field is exclusive to pfSense Plus
            and has no effect on CE.<br><br>This field is only available when the following conditions are met:<br>-
            `carp_mode` must be equal to `'ucast'`<br>
    """

    id: int
    uniqid: None | str | Unset = UNSET
    mode: VirtualIPMode | Unset = UNSET
    interface: str | Unset = UNSET
    type_: VirtualIPType | Unset = VirtualIPType.SINGLE
    subnet: str | Unset = UNSET
    subnet_bits: int | Unset = UNSET
    descr: str | Unset = UNSET
    noexpand: bool | Unset = UNSET
    vhid: int | Unset = UNSET
    advbase: int | Unset = 1
    advskew: int | Unset = UNSET
    password: str | Unset = UNSET
    carp_status: None | str | Unset = UNSET
    carp_mode: VirtualIPCarpMode | Unset = VirtualIPCarpMode.MCAST
    carp_peer: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uniqid: None | str | Unset
        if isinstance(self.uniqid, Unset):
            uniqid = UNSET
        else:
            uniqid = self.uniqid

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        interface = self.interface

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        subnet = self.subnet

        subnet_bits = self.subnet_bits

        descr = self.descr

        noexpand = self.noexpand

        vhid = self.vhid

        advbase = self.advbase

        advskew = self.advskew

        password = self.password

        carp_status: None | str | Unset
        if isinstance(self.carp_status, Unset):
            carp_status = UNSET
        else:
            carp_status = self.carp_status

        carp_mode: str | Unset = UNSET
        if not isinstance(self.carp_mode, Unset):
            carp_mode = self.carp_mode.value

        carp_peer = self.carp_peer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if uniqid is not UNSET:
            field_dict["uniqid"] = uniqid
        if mode is not UNSET:
            field_dict["mode"] = mode
        if interface is not UNSET:
            field_dict["interface"] = interface
        if type_ is not UNSET:
            field_dict["type"] = type_
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if subnet_bits is not UNSET:
            field_dict["subnet_bits"] = subnet_bits
        if descr is not UNSET:
            field_dict["descr"] = descr
        if noexpand is not UNSET:
            field_dict["noexpand"] = noexpand
        if vhid is not UNSET:
            field_dict["vhid"] = vhid
        if advbase is not UNSET:
            field_dict["advbase"] = advbase
        if advskew is not UNSET:
            field_dict["advskew"] = advskew
        if password is not UNSET:
            field_dict["password"] = password
        if carp_status is not UNSET:
            field_dict["carp_status"] = carp_status
        if carp_mode is not UNSET:
            field_dict["carp_mode"] = carp_mode
        if carp_peer is not UNSET:
            field_dict["carp_peer"] = carp_peer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_uniqid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uniqid = _parse_uniqid(d.pop("uniqid", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: VirtualIPMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = VirtualIPMode(_mode)

        interface = d.pop("interface", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: VirtualIPType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VirtualIPType(_type_)

        subnet = d.pop("subnet", UNSET)

        subnet_bits = d.pop("subnet_bits", UNSET)

        descr = d.pop("descr", UNSET)

        noexpand = d.pop("noexpand", UNSET)

        vhid = d.pop("vhid", UNSET)

        advbase = d.pop("advbase", UNSET)

        advskew = d.pop("advskew", UNSET)

        password = d.pop("password", UNSET)

        def _parse_carp_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carp_status = _parse_carp_status(d.pop("carp_status", UNSET))

        _carp_mode = d.pop("carp_mode", UNSET)
        carp_mode: VirtualIPCarpMode | Unset
        if isinstance(_carp_mode, Unset):
            carp_mode = UNSET
        else:
            carp_mode = VirtualIPCarpMode(_carp_mode)

        carp_peer = d.pop("carp_peer", UNSET)

        patch_firewall_virtual_ip_endpoint_data_body = cls(
            id=id,
            uniqid=uniqid,
            mode=mode,
            interface=interface,
            type_=type_,
            subnet=subnet,
            subnet_bits=subnet_bits,
            descr=descr,
            noexpand=noexpand,
            vhid=vhid,
            advbase=advbase,
            advskew=advskew,
            password=password,
            carp_status=carp_status,
            carp_mode=carp_mode,
            carp_peer=carp_peer,
        )

        patch_firewall_virtual_ip_endpoint_data_body.additional_properties = d
        return patch_firewall_virtual_ip_endpoint_data_body

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
