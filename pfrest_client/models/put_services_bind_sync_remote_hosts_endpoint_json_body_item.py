from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bind_sync_remote_host_syncprotocol import BINDSyncRemoteHostSyncprotocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem")


@_attrs_define
class PutServicesBINDSyncRemoteHostsEndpointJsonBodyItem:
    """
    Attributes:
        syncprotocol (BINDSyncRemoteHostSyncprotocol): The protocol to use for syncing.<br>
        ipaddress (str): The IP address/hostname of the remote host.<br>
        syncport (str): The remote host port to use for syncing. Valid options are: a TCP/UDP port number<br>
        username (str): The username to use to authenticate when syncing.<br>
        password (str): The password to use to authenticate when syncing.<br>
        syncdestinenable (bool | Unset): Enable this remote host for syncing.<br>
    """

    syncprotocol: BINDSyncRemoteHostSyncprotocol
    ipaddress: str
    syncport: str
    username: str
    password: str
    syncdestinenable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        syncprotocol = self.syncprotocol.value

        ipaddress = self.ipaddress

        syncport = self.syncport

        username = self.username

        password = self.password

        syncdestinenable = self.syncdestinenable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "syncprotocol": syncprotocol,
                "ipaddress": ipaddress,
                "syncport": syncport,
                "username": username,
                "password": password,
            }
        )
        if syncdestinenable is not UNSET:
            field_dict["syncdestinenable"] = syncdestinenable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        syncprotocol = BINDSyncRemoteHostSyncprotocol(d.pop("syncprotocol"))

        ipaddress = d.pop("ipaddress")

        syncport = d.pop("syncport")

        username = d.pop("username")

        password = d.pop("password")

        syncdestinenable = d.pop("syncdestinenable", UNSET)

        put_services_bind_sync_remote_hosts_endpoint_json_body_item = cls(
            syncprotocol=syncprotocol,
            ipaddress=ipaddress,
            syncport=syncport,
            username=username,
            password=password,
            syncdestinenable=syncdestinenable,
        )

        put_services_bind_sync_remote_hosts_endpoint_json_body_item.additional_properties = d
        return put_services_bind_sync_remote_hosts_endpoint_json_body_item

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
