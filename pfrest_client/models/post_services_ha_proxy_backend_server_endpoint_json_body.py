from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_backend_server_status import HAProxyBackendServerStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesHAProxyBackendServerEndpointJsonBody")


@_attrs_define
class PostServicesHAProxyBackendServerEndpointJsonBody:
    """
    Attributes:
        name (str): The unique name for this backend server.<br>
        address (str): The hostname or IP address of this backend server. Hostname values are only resolved at service
            startup.<br>
        port (str): The port to forward to for this backend server. Valid options are: a TCP/UDP port number<br>
        parent_id (int): The ID of the parent this object is nested under.
        status (HAProxyBackendServerStatus | Unset): The eligibility status for this backend server.<br> Default:
            HAProxyBackendServerStatus.ACTIVE.
        weight (int | Unset): The weight of this backend server when load balancing.<br> Default: 1.
        ssl (bool | Unset): Enables or disables using SSL/TLS when forwarding to this backend server.<br>
        sslserververify (bool | Unset): Enables or disables verifying the SSL/TLS certificate when forwarding to this
            backend server.<br>
        serverid (int | None | Unset): The unique ID for this backend server. This value is set by the system for
            internal use and cannot be changed.<br>
        advanced (str | Unset): Allows adding custom HAProxy server settings to the server.<br>
    """

    name: str
    address: str
    port: str
    parent_id: int
    status: HAProxyBackendServerStatus | Unset = HAProxyBackendServerStatus.ACTIVE
    weight: int | Unset = 1
    ssl: bool | Unset = UNSET
    sslserververify: bool | Unset = UNSET
    serverid: int | None | Unset = UNSET
    advanced: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address

        port = self.port

        parent_id = self.parent_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        field_dict.update(
            {
                "name": name,
                "address": address,
                "port": port,
                "parent_id": parent_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
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
        name = d.pop("name")

        address = d.pop("address")

        port = d.pop("port")

        parent_id = d.pop("parent_id")

        _status = d.pop("status", UNSET)
        status: HAProxyBackendServerStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HAProxyBackendServerStatus(_status)

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

        post_services_ha_proxy_backend_server_endpoint_json_body = cls(
            name=name,
            address=address,
            port=port,
            parent_id=parent_id,
            status=status,
            weight=weight,
            ssl=ssl,
            sslserververify=sslserververify,
            serverid=serverid,
            advanced=advanced,
        )

        post_services_ha_proxy_backend_server_endpoint_json_body.additional_properties = d
        return post_services_ha_proxy_backend_server_endpoint_json_body

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
