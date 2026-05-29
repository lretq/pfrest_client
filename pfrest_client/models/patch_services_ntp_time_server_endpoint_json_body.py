from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ntp_time_server_type import NTPTimeServerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesNTPTimeServerEndpointJsonBody")


@_attrs_define
class PatchServicesNTPTimeServerEndpointJsonBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        timeserver (str | Unset): The IP or hostname of the remote NTP time server, pool or peer.<br>
        type_ (NTPTimeServerType | Unset): The type of this timeserver. Use `server` is `timeserver` is a standalone NTP
            server, use `pool` if `timeserver` represents an NTP pool, or `peer` if `timeserver` is an NTP peer. Note: If
            the `timeserver` value ends with the `pool.ntp.org` suffix, this field will be forced to use `pool`.<br>
            Default: NTPTimeServerType.SERVER.
        prefer (bool | Unset): Enable NTP favoring the use of this server more than all others.<br>
        noselect (bool | Unset): Prevent NTP from using this timeserver, but continue collecting stats.<br><br>This
            field is only available when the following conditions are met:<br>- `type` must not be equal to `'pool'`<br>
    """

    id: int
    timeserver: str | Unset = UNSET
    type_: NTPTimeServerType | Unset = NTPTimeServerType.SERVER
    prefer: bool | Unset = UNSET
    noselect: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        timeserver = self.timeserver

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        prefer = self.prefer

        noselect = self.noselect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if timeserver is not UNSET:
            field_dict["timeserver"] = timeserver
        if type_ is not UNSET:
            field_dict["type"] = type_
        if prefer is not UNSET:
            field_dict["prefer"] = prefer
        if noselect is not UNSET:
            field_dict["noselect"] = noselect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        timeserver = d.pop("timeserver", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: NTPTimeServerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NTPTimeServerType(_type_)

        prefer = d.pop("prefer", UNSET)

        noselect = d.pop("noselect", UNSET)

        patch_services_ntp_time_server_endpoint_json_body = cls(
            id=id,
            timeserver=timeserver,
            type_=type_,
            prefer=prefer,
            noselect=noselect,
        )

        patch_services_ntp_time_server_endpoint_json_body.additional_properties = d
        return patch_services_ntp_time_server_endpoint_json_body

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
