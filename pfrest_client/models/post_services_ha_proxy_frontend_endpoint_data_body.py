from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_frontend_httpclose import HAProxyFrontendHttpclose
from ..models.ha_proxy_frontend_status import HAProxyFrontendStatus
from ..models.ha_proxy_frontend_type import HAProxyFrontendType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ha_proxy_frontend_a_actionitems_item import HAProxyFrontendAActionitemsItem
    from ..models.ha_proxy_frontend_a_errorfiles_item import HAProxyFrontendAErrorfilesItem
    from ..models.ha_proxy_frontend_a_extaddr_item import HAProxyFrontendAExtaddrItem
    from ..models.ha_proxy_frontend_ha_acls_item import HAProxyFrontendHaAclsItem
    from ..models.ha_proxy_frontend_ha_certificates_item import HAProxyFrontendHaCertificatesItem


T = TypeVar("T", bound="PostServicesHAProxyFrontendEndpointDataBody")


@_attrs_define
class PostServicesHAProxyFrontendEndpointDataBody:
    """
    Attributes:
        name (str): The unique name for this HAProxy frontend.<br>
        type_ (HAProxyFrontendType): The processing type for this frontend.<br>
        descr (str | Unset): The description for this HAProxy frontend.<br>
        status (HAProxyFrontendStatus | Unset): The activation status for this HAProxy frontend.<br> Default:
            HAProxyFrontendStatus.ACTIVE.
        a_extaddr (list[HAProxyFrontendAExtaddrItem] | Unset): The external addresses assigned to this frontend.<br>
        max_connections (int | None | Unset): The maximum number of connections allowed by this frontend.<br>
        ha_acls (list[HAProxyFrontendHaAclsItem] | Unset): The ACLs to apply to this frontend.<br>
        a_actionitems (list[HAProxyFrontendAActionitemsItem] | Unset): The actions to take when an ACL match is
            found.<br>
        backend_serverpool (None | str | Unset): The default backend to use for this frontend.<br>
        socket_stats (bool | Unset): Enables or disables collecting and providing separate statistics for each
            socket.<br>
        dontlognull (bool | Unset): Enables or disables logging connections with no data transferred.<br>
        dontlog_normal (bool | Unset): Enables or disables only logging anomalous (not normal) connection.<br>
        log_separate_errors (bool | Unset): Enables or disables changing the log level from info to err on potentially
            interesting info.<br>
        log_detailed (bool | Unset): Enables or disables more detailed logging.<br>
        a_errorfiles (list[HAProxyFrontendAErrorfilesItem] | Unset): The custom error files to use for this
            frontend.<br>
        client_timeout (int | None | Unset): The amount of time (in milliseconds) to wait for data from the client.<br>
            Default: 30000.
        forwardfor (bool | Unset): Enables or disables the HTTP X-Forwarded-For header which contains the client's IP
            address.<br><br>This field is only available when the following conditions are met:<br>- `type` must be equal to
            `'http'`<br>
        httpclose (HAProxyFrontendHttpclose | Unset): The `httpclose` option this frontend will operate.<br> Default:
            HAProxyFrontendHttpclose.HTTP_KEEP_ALIVE.
        advanced_bind (None | str | Unset): Custom value to pass behind each bind option.<br>
        advanced (None | str | Unset): Custom configuration to pass to this frontend.<br>
        ssloffloadcert (None | str | Unset): The default SSL/TLS certificate refid to use for this frontend.<br>
        ha_certificates (list[HAProxyFrontendHaCertificatesItem] | Unset): The additional SSL/TLS certificates to use on
            this frontend.<br>
    """

    name: str
    type_: HAProxyFrontendType
    descr: str | Unset = UNSET
    status: HAProxyFrontendStatus | Unset = HAProxyFrontendStatus.ACTIVE
    a_extaddr: list[HAProxyFrontendAExtaddrItem] | Unset = UNSET
    max_connections: int | None | Unset = UNSET
    ha_acls: list[HAProxyFrontendHaAclsItem] | Unset = UNSET
    a_actionitems: list[HAProxyFrontendAActionitemsItem] | Unset = UNSET
    backend_serverpool: None | str | Unset = UNSET
    socket_stats: bool | Unset = UNSET
    dontlognull: bool | Unset = UNSET
    dontlog_normal: bool | Unset = UNSET
    log_separate_errors: bool | Unset = UNSET
    log_detailed: bool | Unset = UNSET
    a_errorfiles: list[HAProxyFrontendAErrorfilesItem] | Unset = UNSET
    client_timeout: int | None | Unset = 30000
    forwardfor: bool | Unset = UNSET
    httpclose: HAProxyFrontendHttpclose | Unset = HAProxyFrontendHttpclose.HTTP_KEEP_ALIVE
    advanced_bind: None | str | Unset = UNSET
    advanced: None | str | Unset = UNSET
    ssloffloadcert: None | str | Unset = UNSET
    ha_certificates: list[HAProxyFrontendHaCertificatesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_.value

        descr = self.descr

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        a_extaddr: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.a_extaddr, Unset):
            a_extaddr = []
            for a_extaddr_item_data in self.a_extaddr:
                a_extaddr_item = a_extaddr_item_data.to_dict()
                a_extaddr.append(a_extaddr_item)

        max_connections: int | None | Unset
        if isinstance(self.max_connections, Unset):
            max_connections = UNSET
        else:
            max_connections = self.max_connections

        ha_acls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ha_acls, Unset):
            ha_acls = []
            for ha_acls_item_data in self.ha_acls:
                ha_acls_item = ha_acls_item_data.to_dict()
                ha_acls.append(ha_acls_item)

        a_actionitems: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.a_actionitems, Unset):
            a_actionitems = []
            for a_actionitems_item_data in self.a_actionitems:
                a_actionitems_item = a_actionitems_item_data.to_dict()
                a_actionitems.append(a_actionitems_item)

        backend_serverpool: None | str | Unset
        if isinstance(self.backend_serverpool, Unset):
            backend_serverpool = UNSET
        else:
            backend_serverpool = self.backend_serverpool

        socket_stats = self.socket_stats

        dontlognull = self.dontlognull

        dontlog_normal = self.dontlog_normal

        log_separate_errors = self.log_separate_errors

        log_detailed = self.log_detailed

        a_errorfiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.a_errorfiles, Unset):
            a_errorfiles = []
            for a_errorfiles_item_data in self.a_errorfiles:
                a_errorfiles_item = a_errorfiles_item_data.to_dict()
                a_errorfiles.append(a_errorfiles_item)

        client_timeout: int | None | Unset
        if isinstance(self.client_timeout, Unset):
            client_timeout = UNSET
        else:
            client_timeout = self.client_timeout

        forwardfor = self.forwardfor

        httpclose: str | Unset = UNSET
        if not isinstance(self.httpclose, Unset):
            httpclose = self.httpclose.value

        advanced_bind: None | str | Unset
        if isinstance(self.advanced_bind, Unset):
            advanced_bind = UNSET
        else:
            advanced_bind = self.advanced_bind

        advanced: None | str | Unset
        if isinstance(self.advanced, Unset):
            advanced = UNSET
        else:
            advanced = self.advanced

        ssloffloadcert: None | str | Unset
        if isinstance(self.ssloffloadcert, Unset):
            ssloffloadcert = UNSET
        else:
            ssloffloadcert = self.ssloffloadcert

        ha_certificates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ha_certificates, Unset):
            ha_certificates = []
            for ha_certificates_item_data in self.ha_certificates:
                ha_certificates_item = ha_certificates_item_data.to_dict()
                ha_certificates.append(ha_certificates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if status is not UNSET:
            field_dict["status"] = status
        if a_extaddr is not UNSET:
            field_dict["a_extaddr"] = a_extaddr
        if max_connections is not UNSET:
            field_dict["max_connections"] = max_connections
        if ha_acls is not UNSET:
            field_dict["ha_acls"] = ha_acls
        if a_actionitems is not UNSET:
            field_dict["a_actionitems"] = a_actionitems
        if backend_serverpool is not UNSET:
            field_dict["backend_serverpool"] = backend_serverpool
        if socket_stats is not UNSET:
            field_dict["socket_stats"] = socket_stats
        if dontlognull is not UNSET:
            field_dict["dontlognull"] = dontlognull
        if dontlog_normal is not UNSET:
            field_dict["dontlog_normal"] = dontlog_normal
        if log_separate_errors is not UNSET:
            field_dict["log_separate_errors"] = log_separate_errors
        if log_detailed is not UNSET:
            field_dict["log_detailed"] = log_detailed
        if a_errorfiles is not UNSET:
            field_dict["a_errorfiles"] = a_errorfiles
        if client_timeout is not UNSET:
            field_dict["client_timeout"] = client_timeout
        if forwardfor is not UNSET:
            field_dict["forwardfor"] = forwardfor
        if httpclose is not UNSET:
            field_dict["httpclose"] = httpclose
        if advanced_bind is not UNSET:
            field_dict["advanced_bind"] = advanced_bind
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if ssloffloadcert is not UNSET:
            field_dict["ssloffloadcert"] = ssloffloadcert
        if ha_certificates is not UNSET:
            field_dict["ha_certificates"] = ha_certificates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ha_proxy_frontend_a_actionitems_item import HAProxyFrontendAActionitemsItem
        from ..models.ha_proxy_frontend_a_errorfiles_item import HAProxyFrontendAErrorfilesItem
        from ..models.ha_proxy_frontend_a_extaddr_item import HAProxyFrontendAExtaddrItem
        from ..models.ha_proxy_frontend_ha_acls_item import HAProxyFrontendHaAclsItem
        from ..models.ha_proxy_frontend_ha_certificates_item import HAProxyFrontendHaCertificatesItem

        d = dict(src_dict)
        name = d.pop("name")

        type_ = HAProxyFrontendType(d.pop("type"))

        descr = d.pop("descr", UNSET)

        _status = d.pop("status", UNSET)
        status: HAProxyFrontendStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = HAProxyFrontendStatus(_status)

        _a_extaddr = d.pop("a_extaddr", UNSET)
        a_extaddr: list[HAProxyFrontendAExtaddrItem] | Unset = UNSET
        if _a_extaddr is not UNSET:
            a_extaddr = []
            for a_extaddr_item_data in _a_extaddr:
                a_extaddr_item = HAProxyFrontendAExtaddrItem.from_dict(a_extaddr_item_data)

                a_extaddr.append(a_extaddr_item)

        def _parse_max_connections(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_connections = _parse_max_connections(d.pop("max_connections", UNSET))

        _ha_acls = d.pop("ha_acls", UNSET)
        ha_acls: list[HAProxyFrontendHaAclsItem] | Unset = UNSET
        if _ha_acls is not UNSET:
            ha_acls = []
            for ha_acls_item_data in _ha_acls:
                ha_acls_item = HAProxyFrontendHaAclsItem.from_dict(ha_acls_item_data)

                ha_acls.append(ha_acls_item)

        _a_actionitems = d.pop("a_actionitems", UNSET)
        a_actionitems: list[HAProxyFrontendAActionitemsItem] | Unset = UNSET
        if _a_actionitems is not UNSET:
            a_actionitems = []
            for a_actionitems_item_data in _a_actionitems:
                a_actionitems_item = HAProxyFrontendAActionitemsItem.from_dict(a_actionitems_item_data)

                a_actionitems.append(a_actionitems_item)

        def _parse_backend_serverpool(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backend_serverpool = _parse_backend_serverpool(d.pop("backend_serverpool", UNSET))

        socket_stats = d.pop("socket_stats", UNSET)

        dontlognull = d.pop("dontlognull", UNSET)

        dontlog_normal = d.pop("dontlog_normal", UNSET)

        log_separate_errors = d.pop("log_separate_errors", UNSET)

        log_detailed = d.pop("log_detailed", UNSET)

        _a_errorfiles = d.pop("a_errorfiles", UNSET)
        a_errorfiles: list[HAProxyFrontendAErrorfilesItem] | Unset = UNSET
        if _a_errorfiles is not UNSET:
            a_errorfiles = []
            for a_errorfiles_item_data in _a_errorfiles:
                a_errorfiles_item = HAProxyFrontendAErrorfilesItem.from_dict(a_errorfiles_item_data)

                a_errorfiles.append(a_errorfiles_item)

        def _parse_client_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        client_timeout = _parse_client_timeout(d.pop("client_timeout", UNSET))

        forwardfor = d.pop("forwardfor", UNSET)

        _httpclose = d.pop("httpclose", UNSET)
        httpclose: HAProxyFrontendHttpclose | Unset
        if isinstance(_httpclose, Unset):
            httpclose = UNSET
        else:
            httpclose = HAProxyFrontendHttpclose(_httpclose)

        def _parse_advanced_bind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        advanced_bind = _parse_advanced_bind(d.pop("advanced_bind", UNSET))

        def _parse_advanced(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        advanced = _parse_advanced(d.pop("advanced", UNSET))

        def _parse_ssloffloadcert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssloffloadcert = _parse_ssloffloadcert(d.pop("ssloffloadcert", UNSET))

        _ha_certificates = d.pop("ha_certificates", UNSET)
        ha_certificates: list[HAProxyFrontendHaCertificatesItem] | Unset = UNSET
        if _ha_certificates is not UNSET:
            ha_certificates = []
            for ha_certificates_item_data in _ha_certificates:
                ha_certificates_item = HAProxyFrontendHaCertificatesItem.from_dict(ha_certificates_item_data)

                ha_certificates.append(ha_certificates_item)

        post_services_ha_proxy_frontend_endpoint_data_body = cls(
            name=name,
            type_=type_,
            descr=descr,
            status=status,
            a_extaddr=a_extaddr,
            max_connections=max_connections,
            ha_acls=ha_acls,
            a_actionitems=a_actionitems,
            backend_serverpool=backend_serverpool,
            socket_stats=socket_stats,
            dontlognull=dontlognull,
            dontlog_normal=dontlog_normal,
            log_separate_errors=log_separate_errors,
            log_detailed=log_detailed,
            a_errorfiles=a_errorfiles,
            client_timeout=client_timeout,
            forwardfor=forwardfor,
            httpclose=httpclose,
            advanced_bind=advanced_bind,
            advanced=advanced,
            ssloffloadcert=ssloffloadcert,
            ha_certificates=ha_certificates,
        )

        post_services_ha_proxy_frontend_endpoint_data_body.additional_properties = d
        return post_services_ha_proxy_frontend_endpoint_data_body

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
