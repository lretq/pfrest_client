from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bind_settings_bind_dnssec_validation import BINDSettingsBindDnssecValidation
from ..models.bind_settings_bind_ip_version import BINDSettingsBindIpVersion
from ..models.bind_settings_log_options_item import BINDSettingsLogOptionsItem
from ..models.bind_settings_log_severity import BINDSettingsLogSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesBINDSettingsEndpointJsonBody")


@_attrs_define
class PatchServicesBINDSettingsEndpointJsonBody:
    """
    Attributes:
        bind_forwarder_ips (list[str]): The IP addresses of the DNS servers to forward queries to.<br><br>This field is
            only available when the following conditions are met:<br>- `bind_forwarder` must be equal to `true`<br>
        enable_bind (bool | Unset): Enables the BIND service.<br>
        bind_ip_version (BINDSettingsBindIpVersion | Unset): The IP version to use for the BIND service. Leave empty to
            use both IPv4 and IPv6.<br>
        listenon (list[str] | Unset): The interfaces to listen on for DNS requests.<br>
        bind_notify (bool | Unset): Notify slave server after any update on master.<br>
        bind_hide_version (bool | Unset): Hide the BIND version in responses.<br>
        bind_ram_limit (str | Unset): The maximum amount of RAM to use for the BIND service.<br> Default: '256M'.
        bind_logging (bool | Unset): Enable logging for the BIND service.<br>
        log_severity (BINDSettingsLogSeverity | Unset): The minimum severity of events to log.<br> Default:
            BINDSettingsLogSeverity.CRITICAL.
        log_options (list[BINDSettingsLogOptionsItem] | Unset): The categories to log.<br>
        rate_enabled (bool | Unset): Enable rate limiting for the BIND service.<br>
        rate_limit (int | Unset): The maximum number of queries per second to allow.<br><br>This field is only available
            when the following conditions are met:<br>- `rate_enabled` must be equal to `true`<br> Default: 15.
        log_only (bool | Unset): When rate limiting, only log that the query limit has been exceeded. If disabled, the
            query will be dropped instead.<br>
        bind_forwarder (bool | Unset): Enable forwarding queries to other DNS servers listed below rather than this
            server performing its own recursion.<br>
        bind_dnssec_validation (BINDSettingsBindDnssecValidation | Unset): Enable DNSSEC validation when BIND is acting
            as a recursive resolver.<br> Default: BINDSettingsBindDnssecValidation.AUTO.
        listenport (str | Unset): The TCP and UDP port to listen on for DNS requests. Valid options are: a TCP/UDP port
            number<br> Default: '53'.
        controlport (str | Unset): The TCP port to listen on for control requests (localhost only). Valid options are: a
            TCP/UDP port number<br> Default: '953'.
        bind_custom_options (str | Unset): Custom BIND options to include in the configuration file.<br>
        bind_global_settings (str | Unset): Global BIND settings to include in the configuration file.<br>
    """

    bind_forwarder_ips: list[str]
    enable_bind: bool | Unset = UNSET
    bind_ip_version: BINDSettingsBindIpVersion | Unset = UNSET
    listenon: list[str] | Unset = UNSET
    bind_notify: bool | Unset = UNSET
    bind_hide_version: bool | Unset = UNSET
    bind_ram_limit: str | Unset = "256M"
    bind_logging: bool | Unset = UNSET
    log_severity: BINDSettingsLogSeverity | Unset = BINDSettingsLogSeverity.CRITICAL
    log_options: list[BINDSettingsLogOptionsItem] | Unset = UNSET
    rate_enabled: bool | Unset = UNSET
    rate_limit: int | Unset = 15
    log_only: bool | Unset = UNSET
    bind_forwarder: bool | Unset = UNSET
    bind_dnssec_validation: BINDSettingsBindDnssecValidation | Unset = BINDSettingsBindDnssecValidation.AUTO
    listenport: str | Unset = "53"
    controlport: str | Unset = "953"
    bind_custom_options: str | Unset = UNSET
    bind_global_settings: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bind_forwarder_ips = self.bind_forwarder_ips

        enable_bind = self.enable_bind

        bind_ip_version: str | Unset = UNSET
        if not isinstance(self.bind_ip_version, Unset):
            bind_ip_version = self.bind_ip_version.value

        listenon: list[str] | Unset = UNSET
        if not isinstance(self.listenon, Unset):
            listenon = self.listenon

        bind_notify = self.bind_notify

        bind_hide_version = self.bind_hide_version

        bind_ram_limit = self.bind_ram_limit

        bind_logging = self.bind_logging

        log_severity: str | Unset = UNSET
        if not isinstance(self.log_severity, Unset):
            log_severity = self.log_severity.value

        log_options: list[str] | Unset = UNSET
        if not isinstance(self.log_options, Unset):
            log_options = []
            for log_options_item_data in self.log_options:
                log_options_item = log_options_item_data.value
                log_options.append(log_options_item)

        rate_enabled = self.rate_enabled

        rate_limit = self.rate_limit

        log_only = self.log_only

        bind_forwarder = self.bind_forwarder

        bind_dnssec_validation: str | Unset = UNSET
        if not isinstance(self.bind_dnssec_validation, Unset):
            bind_dnssec_validation = self.bind_dnssec_validation.value

        listenport = self.listenport

        controlport = self.controlport

        bind_custom_options = self.bind_custom_options

        bind_global_settings = self.bind_global_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bind_forwarder_ips": bind_forwarder_ips,
            }
        )
        if enable_bind is not UNSET:
            field_dict["enable_bind"] = enable_bind
        if bind_ip_version is not UNSET:
            field_dict["bind_ip_version"] = bind_ip_version
        if listenon is not UNSET:
            field_dict["listenon"] = listenon
        if bind_notify is not UNSET:
            field_dict["bind_notify"] = bind_notify
        if bind_hide_version is not UNSET:
            field_dict["bind_hide_version"] = bind_hide_version
        if bind_ram_limit is not UNSET:
            field_dict["bind_ram_limit"] = bind_ram_limit
        if bind_logging is not UNSET:
            field_dict["bind_logging"] = bind_logging
        if log_severity is not UNSET:
            field_dict["log_severity"] = log_severity
        if log_options is not UNSET:
            field_dict["log_options"] = log_options
        if rate_enabled is not UNSET:
            field_dict["rate_enabled"] = rate_enabled
        if rate_limit is not UNSET:
            field_dict["rate_limit"] = rate_limit
        if log_only is not UNSET:
            field_dict["log_only"] = log_only
        if bind_forwarder is not UNSET:
            field_dict["bind_forwarder"] = bind_forwarder
        if bind_dnssec_validation is not UNSET:
            field_dict["bind_dnssec_validation"] = bind_dnssec_validation
        if listenport is not UNSET:
            field_dict["listenport"] = listenport
        if controlport is not UNSET:
            field_dict["controlport"] = controlport
        if bind_custom_options is not UNSET:
            field_dict["bind_custom_options"] = bind_custom_options
        if bind_global_settings is not UNSET:
            field_dict["bind_global_settings"] = bind_global_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bind_forwarder_ips = cast(list[str], d.pop("bind_forwarder_ips"))

        enable_bind = d.pop("enable_bind", UNSET)

        _bind_ip_version = d.pop("bind_ip_version", UNSET)
        bind_ip_version: BINDSettingsBindIpVersion | Unset
        if isinstance(_bind_ip_version, Unset):
            bind_ip_version = UNSET
        else:
            bind_ip_version = BINDSettingsBindIpVersion(_bind_ip_version)

        listenon = cast(list[str], d.pop("listenon", UNSET))

        bind_notify = d.pop("bind_notify", UNSET)

        bind_hide_version = d.pop("bind_hide_version", UNSET)

        bind_ram_limit = d.pop("bind_ram_limit", UNSET)

        bind_logging = d.pop("bind_logging", UNSET)

        _log_severity = d.pop("log_severity", UNSET)
        log_severity: BINDSettingsLogSeverity | Unset
        if isinstance(_log_severity, Unset):
            log_severity = UNSET
        else:
            log_severity = BINDSettingsLogSeverity(_log_severity)

        _log_options = d.pop("log_options", UNSET)
        log_options: list[BINDSettingsLogOptionsItem] | Unset = UNSET
        if _log_options is not UNSET:
            log_options = []
            for log_options_item_data in _log_options:
                log_options_item = BINDSettingsLogOptionsItem(log_options_item_data)

                log_options.append(log_options_item)

        rate_enabled = d.pop("rate_enabled", UNSET)

        rate_limit = d.pop("rate_limit", UNSET)

        log_only = d.pop("log_only", UNSET)

        bind_forwarder = d.pop("bind_forwarder", UNSET)

        _bind_dnssec_validation = d.pop("bind_dnssec_validation", UNSET)
        bind_dnssec_validation: BINDSettingsBindDnssecValidation | Unset
        if isinstance(_bind_dnssec_validation, Unset):
            bind_dnssec_validation = UNSET
        else:
            bind_dnssec_validation = BINDSettingsBindDnssecValidation(_bind_dnssec_validation)

        listenport = d.pop("listenport", UNSET)

        controlport = d.pop("controlport", UNSET)

        bind_custom_options = d.pop("bind_custom_options", UNSET)

        bind_global_settings = d.pop("bind_global_settings", UNSET)

        patch_services_bind_settings_endpoint_json_body = cls(
            bind_forwarder_ips=bind_forwarder_ips,
            enable_bind=enable_bind,
            bind_ip_version=bind_ip_version,
            listenon=listenon,
            bind_notify=bind_notify,
            bind_hide_version=bind_hide_version,
            bind_ram_limit=bind_ram_limit,
            bind_logging=bind_logging,
            log_severity=log_severity,
            log_options=log_options,
            rate_enabled=rate_enabled,
            rate_limit=rate_limit,
            log_only=log_only,
            bind_forwarder=bind_forwarder,
            bind_dnssec_validation=bind_dnssec_validation,
            listenport=listenport,
            controlport=controlport,
            bind_custom_options=bind_custom_options,
            bind_global_settings=bind_global_settings,
        )

        patch_services_bind_settings_endpoint_json_body.additional_properties = d
        return patch_services_bind_settings_endpoint_json_body

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
