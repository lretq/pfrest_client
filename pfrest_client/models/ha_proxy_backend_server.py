from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_backend_server_status import HAProxyBackendServerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="HAProxyBackendServer")


@_attrs_define
class HAProxyBackendServer:
    """
    Attributes:
        name (str | Unset): The unique name for this backend server.<br>
        status (HAProxyBackendServerStatus | Unset): The eligibility status for this backend server.<br> Default:
            HAProxyBackendServerStatus.ACTIVE.
        address (str | Unset): The hostname or IP address of this backend server. Hostname values are only resolved at
            service startup.<br>
        port (str | Unset): The port to forward to for this backend server. Valid options are: a TCP/UDP port number<br>
        weight (int | Unset): The weight of this backend server when load balancing.<br> Default: 1.
        ssl (bool | Unset): Enables or disables using SSL/TLS when forwarding to this backend server.<br>
        sslserververify (bool | Unset): Enables or disables verifying the SSL/TLS certificate when forwarding to this
            backend server.<br>
        serverid (int | None | Unset): The unique ID for this backend server. This value is set by the system for
            internal use and cannot be changed.<br>
        advanced (str | Unset): Allows adding custom HAProxy server settings to the server.<br>
    """

    name: str | Unset = UNSET
    status: HAProxyBackendServerStatus | Unset = HAProxyBackendServerStatus.ACTIVE
    address: str | Unset = UNSET
    port: str | Unset = UNSET
    weight: int | Unset = 1
    ssl: bool | Unset = UNSET
    sslserververify: bool | Unset = UNSET
    serverid: int | None | Unset = UNSET
    advanced: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        address = self.address

        port = self.port

        weight = self.weight

        ssl = self.ssl

        sslserververify = self.sslserververify

        serverid: int | None | Unset
        if isinstance(self.serverid, Unset):
            serverid = UNSET
        else:
            serverid = self.serverid

        advanced = self.advanced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if weight is not UNSET:
            field_dict["weight"] = weight
        if ssl is not UNSET:
            field_dict["ssl"] = ssl
        if sslserververify is not UNSET:
            field_dict["sslserververify"] = sslserververify
        if serverid is not UNSET:
            field_dict["serverid"] = serverid
        if advanced is not UNSET:
            field_dict["advanced"] = advanced

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: HAProxyBackendServerStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HAProxyBackendServerStatus(_status)

        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        weight = d.pop("weight", UNSET)

        ssl = d.pop("ssl", UNSET)

        sslserververify = d.pop("sslserververify", UNSET)

        def _parse_serverid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        serverid = _parse_serverid(d.pop("serverid", UNSET))

        advanced = d.pop("advanced", UNSET)

        ha_proxy_backend_server = cls(
            name=name,
            status=status,
            address=address,
            port=port,
            weight=weight,
            ssl=ssl,
            sslserververify=sslserververify,
            serverid=serverid,
            advanced=advanced,
        )

        ha_proxy_backend_server.additional_properties = d
        return ha_proxy_backend_server

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
