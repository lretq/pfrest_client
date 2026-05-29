from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bind_sync_remote_host_syncprotocol import BINDSyncRemoteHostSyncprotocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesBINDSyncRemoteHostEndpointDataBody")


@_attrs_define
class PatchServicesBINDSyncRemoteHostEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        syncdestinenable (bool | Unset): Enable this remote host for syncing.<br>
        syncprotocol (BINDSyncRemoteHostSyncprotocol | Unset): The protocol to use for syncing.<br>
        ipaddress (str | Unset): The IP address/hostname of the remote host.<br>
        syncport (str | Unset): The remote host port to use for syncing. Valid options are: a TCP/UDP port number<br>
        username (str | Unset): The username to use to authenticate when syncing.<br>
        password (str | Unset): The password to use to authenticate when syncing.<br>
    """

    id: int
    syncdestinenable: bool | Unset = UNSET
    syncprotocol: BINDSyncRemoteHostSyncprotocol | Unset = UNSET
    ipaddress: str | Unset = UNSET
    syncport: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        syncdestinenable = self.syncdestinenable

        syncprotocol: str | Unset = UNSET
        if not isinstance(self.syncprotocol, Unset):
            syncprotocol = self.syncprotocol.value

        ipaddress = self.ipaddress

        syncport = self.syncport

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if syncdestinenable is not UNSET:
            field_dict["syncdestinenable"] = syncdestinenable
        if syncprotocol is not UNSET:
            field_dict["syncprotocol"] = syncprotocol
        if ipaddress is not UNSET:
            field_dict["ipaddress"] = ipaddress
        if syncport is not UNSET:
            field_dict["syncport"] = syncport
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        syncdestinenable = d.pop("syncdestinenable", UNSET)

        _syncprotocol = d.pop("syncprotocol", UNSET)
        syncprotocol: BINDSyncRemoteHostSyncprotocol | Unset
        if isinstance(_syncprotocol, Unset):
            syncprotocol = UNSET
        else:
            syncprotocol = BINDSyncRemoteHostSyncprotocol(_syncprotocol)

        ipaddress = d.pop("ipaddress", UNSET)

        syncport = d.pop("syncport", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        patch_services_bind_sync_remote_host_endpoint_data_body = cls(
            id=id,
            syncdestinenable=syncdestinenable,
            syncprotocol=syncprotocol,
            ipaddress=ipaddress,
            syncport=syncport,
            username=username,
            password=password,
        )

        patch_services_bind_sync_remote_host_endpoint_data_body.additional_properties = d
        return patch_services_bind_sync_remote_host_endpoint_data_body

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
