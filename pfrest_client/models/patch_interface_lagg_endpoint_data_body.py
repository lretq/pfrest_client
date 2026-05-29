from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interface_lagg_lacptimeout import InterfaceLAGGLacptimeout
from ..models.interface_lagg_lagghash import InterfaceLAGGLagghash
from ..models.interface_lagg_proto import InterfaceLAGGProto
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchInterfaceLAGGEndpointDataBody")


@_attrs_define
class PatchInterfaceLAGGEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        laggif (None | str | Unset): The real name of the LAGG interface.<br>
        descr (str | Unset): A description to help document the purpose of this LAGG interface.<br>
        members (list[str] | Unset): A list of member interfaces to include in the LAGG.<br>
        proto (InterfaceLAGGProto | Unset): The LAGG protocol to use.<br>
        lacptimeout (InterfaceLAGGLacptimeout | Unset): The LACP timeout mode to use.<br><br>This field is only
            available when the following conditions are met:<br>- `proto` must be equal to `'lacp'`<br> Default:
            InterfaceLAGGLacptimeout.SLOW.
        lagghash (InterfaceLAGGLagghash | Unset): The LAGG hash algorithm to use.<br><br>This field is only available
            when the following conditions are met:<br>- `proto` must be one of [ lacp, loadbalance ]<br> Default:
            InterfaceLAGGLagghash.L2L3L4.
        failovermaster (str | Unset): The failover master interface to use.<br><br>This field is only available when the
            following conditions are met:<br>- `proto` must be equal to `'failover'`<br> Default: 'auto'.
    """

    id: int
    laggif: None | str | Unset = UNSET
    descr: str | Unset = UNSET
    members: list[str] | Unset = UNSET
    proto: InterfaceLAGGProto | Unset = UNSET
    lacptimeout: InterfaceLAGGLacptimeout | Unset = InterfaceLAGGLacptimeout.SLOW
    lagghash: InterfaceLAGGLagghash | Unset = InterfaceLAGGLagghash.L2L3L4
    failovermaster: str | Unset = "auto"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        laggif: None | str | Unset
        if isinstance(self.laggif, Unset):
            laggif = UNSET
        else:
            laggif = self.laggif

        descr = self.descr

        members: list[str] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        proto: str | Unset = UNSET
        if not isinstance(self.proto, Unset):
            proto = self.proto.value

        lacptimeout: str | Unset = UNSET
        if not isinstance(self.lacptimeout, Unset):
            lacptimeout = self.lacptimeout.value

        lagghash: str | Unset = UNSET
        if not isinstance(self.lagghash, Unset):
            lagghash = self.lagghash.value

        failovermaster = self.failovermaster

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if laggif is not UNSET:
            field_dict["laggif"] = laggif
        if descr is not UNSET:
            field_dict["descr"] = descr
        if members is not UNSET:
            field_dict["members"] = members
        if proto is not UNSET:
            field_dict["proto"] = proto
        if lacptimeout is not UNSET:
            field_dict["lacptimeout"] = lacptimeout
        if lagghash is not UNSET:
            field_dict["lagghash"] = lagghash
        if failovermaster is not UNSET:
            field_dict["failovermaster"] = failovermaster

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_laggif(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        laggif = _parse_laggif(d.pop("laggif", UNSET))

        descr = d.pop("descr", UNSET)

        members = cast(list[str], d.pop("members", UNSET))

        _proto = d.pop("proto", UNSET)
        proto: InterfaceLAGGProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = InterfaceLAGGProto(_proto)

        _lacptimeout = d.pop("lacptimeout", UNSET)
        lacptimeout: InterfaceLAGGLacptimeout | Unset
        if isinstance(_lacptimeout, Unset):
            lacptimeout = UNSET
        else:
            lacptimeout = InterfaceLAGGLacptimeout(_lacptimeout)

        _lagghash = d.pop("lagghash", UNSET)
        lagghash: InterfaceLAGGLagghash | Unset
        if isinstance(_lagghash, Unset):
            lagghash = UNSET
        else:
            lagghash = InterfaceLAGGLagghash(_lagghash)

        failovermaster = d.pop("failovermaster", UNSET)

        patch_interface_lagg_endpoint_data_body = cls(
            id=id,
            laggif=laggif,
            descr=descr,
            members=members,
            proto=proto,
            lacptimeout=lacptimeout,
            lagghash=lagghash,
            failovermaster=failovermaster,
        )

        patch_interface_lagg_endpoint_data_body.additional_properties = d
        return patch_interface_lagg_endpoint_data_body

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
