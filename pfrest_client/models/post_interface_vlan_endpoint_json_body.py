from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostInterfaceVLANEndpointJsonBody")


@_attrs_define
class PostInterfaceVLANEndpointJsonBody:
    """
    Attributes:
        if_ (str): The real parent interface this VLAN will be applied to.<br>
        tag (int): The VLAN ID tag to use. This must be unique from all other VLANs on the parent interface.<br>
        vlanif (None | str | Unset): Displays the full interface VLAN. This value is automatically populated and cannot
            be set.<br>
        pcp (int | None | Unset): The 802.1p VLAN priority code point (PCP) to assign to this VLAN.<br>
        descr (str | Unset): A description to help document the purpose of this VLAN.<br>
    """

    if_: str
    tag: int
    vlanif: None | str | Unset = UNSET
    pcp: int | None | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        if_ = self.if_

        tag = self.tag

        vlanif: None | str | Unset
        if isinstance(self.vlanif, Unset):
            vlanif = UNSET
        else:
            vlanif = self.vlanif

        pcp: int | None | Unset
        if isinstance(self.pcp, Unset):
            pcp = UNSET
        else:
            pcp = self.pcp

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if": if_,
                "tag": tag,
            }
        )
        if vlanif is not UNSET:
            field_dict["vlanif"] = vlanif
        if pcp is not UNSET:
            field_dict["pcp"] = pcp
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        if_ = d.pop("if")

        tag = d.pop("tag")

        def _parse_vlanif(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vlanif = _parse_vlanif(d.pop("vlanif", UNSET))

        def _parse_pcp(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pcp = _parse_pcp(d.pop("pcp", UNSET))

        descr = d.pop("descr", UNSET)

        post_interface_vlan_endpoint_json_body = cls(
            if_=if_,
            tag=tag,
            vlanif=vlanif,
            pcp=pcp,
            descr=descr,
        )

        post_interface_vlan_endpoint_json_body.additional_properties = d
        return post_interface_vlan_endpoint_json_body

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
