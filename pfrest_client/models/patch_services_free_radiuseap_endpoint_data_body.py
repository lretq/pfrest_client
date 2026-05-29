from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.free_radiuseap_default_eap_type import FreeRADIUSEAPDefaultEapType
from ..models.free_radiuseap_peap_default_eap_type import FreeRADIUSEAPPeapDefaultEapType
from ..models.free_radiuseap_peap_soh_enable import FreeRADIUSEAPPeapSohEnable
from ..models.free_radiuseap_tls_min_version import FreeRADIUSEAPTlsMinVersion
from ..models.free_radiuseap_ttls_default_eap_type import FreeRADIUSEAPTtlsDefaultEapType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesFreeRADIUSEAPEndpointDataBody")


@_attrs_define
class PatchServicesFreeRADIUSEAPEndpointDataBody:
    """
    Attributes:
        disable_weak_eap_types (bool | Unset): Disables weak EAP types (MD5 and GTC). When enabled, only stronger EAP
            types like TLS, TTLS, PEAP, and MSCHAPv2 are allowed.<br>
        default_eap_type (FreeRADIUSEAPDefaultEapType | Unset): The default EAP type invoked when an EAP-Identity
            response is received.<br> Default: FreeRADIUSEAPDefaultEapType.MD5.
        timer_expire (int | Unset): The expiration time (in seconds) of the EAP-Response / EAP-Request correlation
            list.<br> Default: 60.
        ignore_unknown_eap_types (bool | Unset): If enabled, unknown EAP types are ignored instead of rejected. A proxy
            module must be configured to forward such requests to another RADIUS server.<br>
        cisco_accounting_username_bug (bool | Unset): Enables the workaround for the CISCO AP1230B firmware 12.2(13)JA1
            accounting username bug.<br>
        max_sessions (int | Unset): Helps prevent DoS attacks by limiting the number of EAP sessions the server
            tracks.<br> Default: 4096.
        tls_min_version (FreeRADIUSEAPTlsMinVersion | Unset): The minimum TLS version that will be accepted for EAP-TLS-
            derived methods.<br> Default: FreeRADIUSEAPTlsMinVersion.VALUE_0.
        ssl_ca_cert (None | str | Unset): The Certificate Authority (refid) used by the FreeRADIUS EAP module. Leave
            unset to have the FreeRADIUS package auto-generate a temporary CA on apply.<br>
        ssl_ca_crl (None | str | Unset): The Certificate Revocation List (refid) checked when verifying EAP client
            certificates. Leave unset to disable CRL checking.<br>
        ssl_server_cert (None | str | Unset): The server Certificate (refid) presented by the FreeRADIUS EAP module.
            Leave unset to have the FreeRADIUS package auto-generate a temporary server certificate on apply.<br>
        tls_include_length (bool | Unset): When enabled, the total length of the EAP-TLS message is included in every
            packet, instead of only the first packet of a fragment series.<br> Default: True.
        tls_fragment_size (int | Unset): The EAP-TLS fragment size (in bytes). Cannot exceed 4096.<br> Default: 1024.
        tls_check_cert_issuer (bool | Unset): When enabled, the server/client certificate must match the configured CA
            issuer.<br>
        tls_ca_subject (str | Unset): The expected CA subject string for issuer validation. Leave blank to use the
            subject of the configured SSL CA Certificate.<br>
        tls_check_cert_cn (bool | Unset): When enabled, the Common Name of the client certificate must match the User-
            Name attribute.<br>
        cache_enable (bool | Unset): Enables the EAP-TLS session resumption / fast reauthentication cache.<br>
        cache_lifetime (int | Unset): Lifetime of cached entries (in hours).<br> Default: 24.
        cache_max_entries (int | Unset): The maximum number of entries in the EAP-TLS cache. Set to 0 for infinite.<br>
            Default: 255.
        ocsp_enable (bool | Unset): Enables OCSP support for EAP-TLS client certificate verification.<br>
        ocsp_override_cert_url (bool | Unset): When enabled, the configured OCSP responder URL overrides the URL
            extracted from the client certificate.<br>
        ocsp_url (str | Unset): The OCSP responder URL used to verify EAP-TLS client certificates when OCSP is
            enabled.<br> Default: 'http://127.0.0.1/ocsp/'.
        ttls_default_eap_type (FreeRADIUSEAPTtlsDefaultEapType | Unset): The default EAP type used inside the EAP-TTLS
            tunnel.<br> Default: FreeRADIUSEAPTtlsDefaultEapType.MD5.
        ttls_copy_request_to_tunnel (bool | Unset): When enabled, attributes available outside of the EAP-TTLS tunnel
            are copied into the tunneled authentication request.<br>
        ttls_use_tunneled_reply (bool | Unset): When enabled, reply attributes from the tunneled authentication are
            returned to the NAS.<br>
        ttls_include_length (bool | Unset): When enabled, the total length of the EAP-TTLS message is included in every
            packet, instead of only the first packet of a fragment series.<br> Default: True.
        peap_default_eap_type (FreeRADIUSEAPPeapDefaultEapType | Unset): The default EAP type used inside the EAP-PEAP
            tunnel.<br> Default: FreeRADIUSEAPPeapDefaultEapType.MSCHAPV2.
        peap_copy_request_to_tunnel (bool | Unset): When enabled, attributes available outside of the EAP-PEAP tunnel
            are copied into the tunneled authentication request.<br>
        peap_use_tunneled_reply (bool | Unset): When enabled, reply attributes from the tunneled authentication are
            returned to the NAS.<br>
        peap_soh_enable (FreeRADIUSEAPPeapSohEnable | Unset): Enable or disable Microsoft Statement of Health (SoH)
            support inside EAP-PEAP. The SoH site configuration must be edited at /usr/local/etc/raddb/sites-available/soh
            outside of this API.<br> Default: FreeRADIUSEAPPeapSohEnable.DISABLE.
    """

    disable_weak_eap_types: bool | Unset = UNSET
    default_eap_type: FreeRADIUSEAPDefaultEapType | Unset = FreeRADIUSEAPDefaultEapType.MD5
    timer_expire: int | Unset = 60
    ignore_unknown_eap_types: bool | Unset = UNSET
    cisco_accounting_username_bug: bool | Unset = UNSET
    max_sessions: int | Unset = 4096
    tls_min_version: FreeRADIUSEAPTlsMinVersion | Unset = FreeRADIUSEAPTlsMinVersion.VALUE_0
    ssl_ca_cert: None | str | Unset = UNSET
    ssl_ca_crl: None | str | Unset = UNSET
    ssl_server_cert: None | str | Unset = UNSET
    tls_include_length: bool | Unset = True
    tls_fragment_size: int | Unset = 1024
    tls_check_cert_issuer: bool | Unset = UNSET
    tls_ca_subject: str | Unset = UNSET
    tls_check_cert_cn: bool | Unset = UNSET
    cache_enable: bool | Unset = UNSET
    cache_lifetime: int | Unset = 24
    cache_max_entries: int | Unset = 255
    ocsp_enable: bool | Unset = UNSET
    ocsp_override_cert_url: bool | Unset = UNSET
    ocsp_url: str | Unset = "http://127.0.0.1/ocsp/"
    ttls_default_eap_type: FreeRADIUSEAPTtlsDefaultEapType | Unset = FreeRADIUSEAPTtlsDefaultEapType.MD5
    ttls_copy_request_to_tunnel: bool | Unset = UNSET
    ttls_use_tunneled_reply: bool | Unset = UNSET
    ttls_include_length: bool | Unset = True
    peap_default_eap_type: FreeRADIUSEAPPeapDefaultEapType | Unset = FreeRADIUSEAPPeapDefaultEapType.MSCHAPV2
    peap_copy_request_to_tunnel: bool | Unset = UNSET
    peap_use_tunneled_reply: bool | Unset = UNSET
    peap_soh_enable: FreeRADIUSEAPPeapSohEnable | Unset = FreeRADIUSEAPPeapSohEnable.DISABLE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disable_weak_eap_types = self.disable_weak_eap_types

        default_eap_type: str | Unset = UNSET
        if not isinstance(self.default_eap_type, Unset):
            default_eap_type = self.default_eap_type.value

        timer_expire = self.timer_expire

        ignore_unknown_eap_types = self.ignore_unknown_eap_types

        cisco_accounting_username_bug = self.cisco_accounting_username_bug

        max_sessions = self.max_sessions

        tls_min_version: str | Unset = UNSET
        if not isinstance(self.tls_min_version, Unset):
            tls_min_version = self.tls_min_version.value

        ssl_ca_cert: None | str | Unset
        if isinstance(self.ssl_ca_cert, Unset):
            ssl_ca_cert = UNSET
        else:
            ssl_ca_cert = self.ssl_ca_cert

        ssl_ca_crl: None | str | Unset
        if isinstance(self.ssl_ca_crl, Unset):
            ssl_ca_crl = UNSET
        else:
            ssl_ca_crl = self.ssl_ca_crl

        ssl_server_cert: None | str | Unset
        if isinstance(self.ssl_server_cert, Unset):
            ssl_server_cert = UNSET
        else:
            ssl_server_cert = self.ssl_server_cert

        tls_include_length = self.tls_include_length

        tls_fragment_size = self.tls_fragment_size

        tls_check_cert_issuer = self.tls_check_cert_issuer

        tls_ca_subject = self.tls_ca_subject

        tls_check_cert_cn = self.tls_check_cert_cn

        cache_enable = self.cache_enable

        cache_lifetime = self.cache_lifetime

        cache_max_entries = self.cache_max_entries

        ocsp_enable = self.ocsp_enable

        ocsp_override_cert_url = self.ocsp_override_cert_url

        ocsp_url = self.ocsp_url

        ttls_default_eap_type: str | Unset = UNSET
        if not isinstance(self.ttls_default_eap_type, Unset):
            ttls_default_eap_type = self.ttls_default_eap_type.value

        ttls_copy_request_to_tunnel = self.ttls_copy_request_to_tunnel

        ttls_use_tunneled_reply = self.ttls_use_tunneled_reply

        ttls_include_length = self.ttls_include_length

        peap_default_eap_type: str | Unset = UNSET
        if not isinstance(self.peap_default_eap_type, Unset):
            peap_default_eap_type = self.peap_default_eap_type.value

        peap_copy_request_to_tunnel = self.peap_copy_request_to_tunnel

        peap_use_tunneled_reply = self.peap_use_tunneled_reply

        peap_soh_enable: str | Unset = UNSET
        if not isinstance(self.peap_soh_enable, Unset):
            peap_soh_enable = self.peap_soh_enable.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable_weak_eap_types is not UNSET:
            field_dict["disable_weak_eap_types"] = disable_weak_eap_types
        if default_eap_type is not UNSET:
            field_dict["default_eap_type"] = default_eap_type
        if timer_expire is not UNSET:
            field_dict["timer_expire"] = timer_expire
        if ignore_unknown_eap_types is not UNSET:
            field_dict["ignore_unknown_eap_types"] = ignore_unknown_eap_types
        if cisco_accounting_username_bug is not UNSET:
            field_dict["cisco_accounting_username_bug"] = cisco_accounting_username_bug
        if max_sessions is not UNSET:
            field_dict["max_sessions"] = max_sessions
        if tls_min_version is not UNSET:
            field_dict["tls_min_version"] = tls_min_version
        if ssl_ca_cert is not UNSET:
            field_dict["ssl_ca_cert"] = ssl_ca_cert
        if ssl_ca_crl is not UNSET:
            field_dict["ssl_ca_crl"] = ssl_ca_crl
        if ssl_server_cert is not UNSET:
            field_dict["ssl_server_cert"] = ssl_server_cert
        if tls_include_length is not UNSET:
            field_dict["tls_include_length"] = tls_include_length
        if tls_fragment_size is not UNSET:
            field_dict["tls_fragment_size"] = tls_fragment_size
        if tls_check_cert_issuer is not UNSET:
            field_dict["tls_check_cert_issuer"] = tls_check_cert_issuer
        if tls_ca_subject is not UNSET:
            field_dict["tls_ca_subject"] = tls_ca_subject
        if tls_check_cert_cn is not UNSET:
            field_dict["tls_check_cert_cn"] = tls_check_cert_cn
        if cache_enable is not UNSET:
            field_dict["cache_enable"] = cache_enable
        if cache_lifetime is not UNSET:
            field_dict["cache_lifetime"] = cache_lifetime
        if cache_max_entries is not UNSET:
            field_dict["cache_max_entries"] = cache_max_entries
        if ocsp_enable is not UNSET:
            field_dict["ocsp_enable"] = ocsp_enable
        if ocsp_override_cert_url is not UNSET:
            field_dict["ocsp_override_cert_url"] = ocsp_override_cert_url
        if ocsp_url is not UNSET:
            field_dict["ocsp_url"] = ocsp_url
        if ttls_default_eap_type is not UNSET:
            field_dict["ttls_default_eap_type"] = ttls_default_eap_type
        if ttls_copy_request_to_tunnel is not UNSET:
            field_dict["ttls_copy_request_to_tunnel"] = ttls_copy_request_to_tunnel
        if ttls_use_tunneled_reply is not UNSET:
            field_dict["ttls_use_tunneled_reply"] = ttls_use_tunneled_reply
        if ttls_include_length is not UNSET:
            field_dict["ttls_include_length"] = ttls_include_length
        if peap_default_eap_type is not UNSET:
            field_dict["peap_default_eap_type"] = peap_default_eap_type
        if peap_copy_request_to_tunnel is not UNSET:
            field_dict["peap_copy_request_to_tunnel"] = peap_copy_request_to_tunnel
        if peap_use_tunneled_reply is not UNSET:
            field_dict["peap_use_tunneled_reply"] = peap_use_tunneled_reply
        if peap_soh_enable is not UNSET:
            field_dict["peap_soh_enable"] = peap_soh_enable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disable_weak_eap_types = d.pop("disable_weak_eap_types", UNSET)

        _default_eap_type = d.pop("default_eap_type", UNSET)
        default_eap_type: FreeRADIUSEAPDefaultEapType | Unset
        if isinstance(_default_eap_type, Unset):
            default_eap_type = UNSET
        else:
            default_eap_type = FreeRADIUSEAPDefaultEapType(_default_eap_type)

        timer_expire = d.pop("timer_expire", UNSET)

        ignore_unknown_eap_types = d.pop("ignore_unknown_eap_types", UNSET)

        cisco_accounting_username_bug = d.pop("cisco_accounting_username_bug", UNSET)

        max_sessions = d.pop("max_sessions", UNSET)

        _tls_min_version = d.pop("tls_min_version", UNSET)
        tls_min_version: FreeRADIUSEAPTlsMinVersion | Unset
        if isinstance(_tls_min_version, Unset):
            tls_min_version = UNSET
        else:
            tls_min_version = FreeRADIUSEAPTlsMinVersion(_tls_min_version)

        def _parse_ssl_ca_cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssl_ca_cert = _parse_ssl_ca_cert(d.pop("ssl_ca_cert", UNSET))

        def _parse_ssl_ca_crl(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssl_ca_crl = _parse_ssl_ca_crl(d.pop("ssl_ca_crl", UNSET))

        def _parse_ssl_server_cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssl_server_cert = _parse_ssl_server_cert(d.pop("ssl_server_cert", UNSET))

        tls_include_length = d.pop("tls_include_length", UNSET)

        tls_fragment_size = d.pop("tls_fragment_size", UNSET)

        tls_check_cert_issuer = d.pop("tls_check_cert_issuer", UNSET)

        tls_ca_subject = d.pop("tls_ca_subject", UNSET)

        tls_check_cert_cn = d.pop("tls_check_cert_cn", UNSET)

        cache_enable = d.pop("cache_enable", UNSET)

        cache_lifetime = d.pop("cache_lifetime", UNSET)

        cache_max_entries = d.pop("cache_max_entries", UNSET)

        ocsp_enable = d.pop("ocsp_enable", UNSET)

        ocsp_override_cert_url = d.pop("ocsp_override_cert_url", UNSET)

        ocsp_url = d.pop("ocsp_url", UNSET)

        _ttls_default_eap_type = d.pop("ttls_default_eap_type", UNSET)
        ttls_default_eap_type: FreeRADIUSEAPTtlsDefaultEapType | Unset
        if isinstance(_ttls_default_eap_type, Unset):
            ttls_default_eap_type = UNSET
        else:
            ttls_default_eap_type = FreeRADIUSEAPTtlsDefaultEapType(_ttls_default_eap_type)

        ttls_copy_request_to_tunnel = d.pop("ttls_copy_request_to_tunnel", UNSET)

        ttls_use_tunneled_reply = d.pop("ttls_use_tunneled_reply", UNSET)

        ttls_include_length = d.pop("ttls_include_length", UNSET)

        _peap_default_eap_type = d.pop("peap_default_eap_type", UNSET)
        peap_default_eap_type: FreeRADIUSEAPPeapDefaultEapType | Unset
        if isinstance(_peap_default_eap_type, Unset):
            peap_default_eap_type = UNSET
        else:
            peap_default_eap_type = FreeRADIUSEAPPeapDefaultEapType(_peap_default_eap_type)

        peap_copy_request_to_tunnel = d.pop("peap_copy_request_to_tunnel", UNSET)

        peap_use_tunneled_reply = d.pop("peap_use_tunneled_reply", UNSET)

        _peap_soh_enable = d.pop("peap_soh_enable", UNSET)
        peap_soh_enable: FreeRADIUSEAPPeapSohEnable | Unset
        if isinstance(_peap_soh_enable, Unset):
            peap_soh_enable = UNSET
        else:
            peap_soh_enable = FreeRADIUSEAPPeapSohEnable(_peap_soh_enable)

        patch_services_free_radiuseap_endpoint_data_body = cls(
            disable_weak_eap_types=disable_weak_eap_types,
            default_eap_type=default_eap_type,
            timer_expire=timer_expire,
            ignore_unknown_eap_types=ignore_unknown_eap_types,
            cisco_accounting_username_bug=cisco_accounting_username_bug,
            max_sessions=max_sessions,
            tls_min_version=tls_min_version,
            ssl_ca_cert=ssl_ca_cert,
            ssl_ca_crl=ssl_ca_crl,
            ssl_server_cert=ssl_server_cert,
            tls_include_length=tls_include_length,
            tls_fragment_size=tls_fragment_size,
            tls_check_cert_issuer=tls_check_cert_issuer,
            tls_ca_subject=tls_ca_subject,
            tls_check_cert_cn=tls_check_cert_cn,
            cache_enable=cache_enable,
            cache_lifetime=cache_lifetime,
            cache_max_entries=cache_max_entries,
            ocsp_enable=ocsp_enable,
            ocsp_override_cert_url=ocsp_override_cert_url,
            ocsp_url=ocsp_url,
            ttls_default_eap_type=ttls_default_eap_type,
            ttls_copy_request_to_tunnel=ttls_copy_request_to_tunnel,
            ttls_use_tunneled_reply=ttls_use_tunneled_reply,
            ttls_include_length=ttls_include_length,
            peap_default_eap_type=peap_default_eap_type,
            peap_copy_request_to_tunnel=peap_copy_request_to_tunnel,
            peap_use_tunneled_reply=peap_use_tunneled_reply,
            peap_soh_enable=peap_soh_enable,
        )

        patch_services_free_radiuseap_endpoint_data_body.additional_properties = d
        return patch_services_free_radiuseap_endpoint_data_body

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
