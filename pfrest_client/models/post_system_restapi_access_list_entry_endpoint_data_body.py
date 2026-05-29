from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.restapi_access_list_entry_type import RESTAPIAccessListEntryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSystemRESTAPIAccessListEntryEndpointDataBody")


@_attrs_define
class PostSystemRESTAPIAccessListEntryEndpointDataBody:
    """
    Attributes:
        network (str): The network (in CIDR notation) that this entry applies to. Clients interacting with the REST API
            from this network will be affected by this entry.<br>
        type_ (RESTAPIAccessListEntryType | Unset): The type of access this entry provides. "allow" entries permit
            access to the REST API from the specified networks. "deny" entries block access to the REST API from the
            specified networks.<br> Default: RESTAPIAccessListEntryType.ALLOW.
        weight (int | Unset): The weight of this entry. Entries with lower weights are evaluated first. If multiple
            entries match a request, the entry with the lowest weight will be applied.<br> Default: 1.
        users (list[str] | Unset): The users that this entry applies to. Only users in this list will be affected by
            this entry. Leave empty if this entry should apply to all users.<br>
        sched (str | Unset): The firewall schedule that this entry will use. This entry will only be active during the
                            times specified in the schedule. Leave empty to apply this entry at all times.<br>
        descr (str | Unset): A description of this access list entry. This field is optional.<br>
    """

    network: str
    type_: RESTAPIAccessListEntryType | Unset = RESTAPIAccessListEntryType.ALLOW
    weight: int | Unset = 1
    users: list[str] | Unset = UNSET
    sched: str | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        weight = self.weight

        users: list[str] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        sched = self.sched

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if weight is not UNSET:
            field_dict["weight"] = weight
        if users is not UNSET:
            field_dict["users"] = users
        if sched is not UNSET:
            field_dict["sched"] = sched
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        network = d.pop("network")

        _type_ = d.pop("type", UNSET)
        type_: RESTAPIAccessListEntryType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTAPIAccessListEntryType(_type_)

        weight = d.pop("weight", UNSET)

        users = cast(list[str], d.pop("users", UNSET))

        sched = d.pop("sched", UNSET)

        descr = d.pop("descr", UNSET)

        post_system_restapi_access_list_entry_endpoint_data_body = cls(
            network=network,
            type_=type_,
            weight=weight,
            users=users,
            sched=sched,
            descr=descr,
        )

        post_system_restapi_access_list_entry_endpoint_data_body.additional_properties = d
        return post_system_restapi_access_list_entry_endpoint_data_body

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
