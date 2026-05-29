from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostInterfaceBridgeEndpointDataBody")


@_attrs_define
class PostInterfaceBridgeEndpointDataBody:
    """
    Attributes:
        members (list[str]): The member interfaces to include in this bridge.<br>
        descr (str | Unset): A description for this interface bridge.<br>
        bridgeif (None | str | Unset): The real interface name for this bridge interface.<br> Default: 'bridge0'.
    """

    members: list[str]
    descr: str | Unset = UNSET
    bridgeif: None | str | Unset = "bridge0"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        members = self.members

        descr = self.descr

        bridgeif: None | str | Unset
        if isinstance(self.bridgeif, Unset):
            bridgeif = UNSET
        else:
            bridgeif = self.bridgeif

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "members": members,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if bridgeif is not UNSET:
            field_dict["bridgeif"] = bridgeif

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        members = cast(list[str], d.pop("members"))

        descr = d.pop("descr", UNSET)

        def _parse_bridgeif(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bridgeif = _parse_bridgeif(d.pop("bridgeif", UNSET))

        post_interface_bridge_endpoint_data_body = cls(
            members=members,
            descr=descr,
            bridgeif=bridgeif,
        )

        post_interface_bridge_endpoint_data_body.additional_properties = d
        return post_interface_bridge_endpoint_data_body

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
