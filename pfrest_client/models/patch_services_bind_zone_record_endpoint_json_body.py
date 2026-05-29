from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bind_zone_record_type import BINDZoneRecordType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesBINDZoneRecordEndpointJsonBody")


@_attrs_define
class PatchServicesBINDZoneRecordEndpointJsonBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        name (str | Unset): The domain name for this record.<br>
        type_ (BINDZoneRecordType | Unset): The type of record.<br>
        rdata (str | Unset): The data for this record. This can be an IP address, domain name, or other data depending
            on the record type.<br>
        priority (int | Unset): The priority for this record.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be one of [ MX, SRV ]<br>
    """

    parent_id: int
    id: int
    name: str | Unset = UNSET
    type_: BINDZoneRecordType | Unset = UNSET
    rdata: str | Unset = UNSET
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        rdata = self.rdata

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if rdata is not UNSET:
            field_dict["rdata"] = rdata
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BINDZoneRecordType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BINDZoneRecordType(_type_)

        rdata = d.pop("rdata", UNSET)

        priority = d.pop("priority", UNSET)

        patch_services_bind_zone_record_endpoint_json_body = cls(
            parent_id=parent_id,
            id=id,
            name=name,
            type_=type_,
            rdata=rdata,
            priority=priority,
        )

        patch_services_bind_zone_record_endpoint_json_body.additional_properties = d
        return patch_services_bind_zone_record_endpoint_json_body

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
