from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_settings_email_level import HAProxySettingsEmailLevel
from ..models.ha_proxy_settings_logfacility import HAProxySettingsLogfacility
from ..models.ha_proxy_settings_loglevel import HAProxySettingsLoglevel
from ..models.ha_proxy_settings_sslcompatibilitymode import HAProxySettingsSslcompatibilitymode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ha_proxy_settings_dns_resolvers_item import HAProxySettingsDnsResolversItem
    from ..models.ha_proxy_settings_email_mailers_item import HAProxySettingsEmailMailersItem


T = TypeVar("T", bound="PatchServicesHAProxySettingsEndpointJsonBody")


@_attrs_define
class PatchServicesHAProxySettingsEndpointJsonBody:
    """
    Attributes:
        enable (bool | Unset): Enables or disable HAProxy on the system.<br>
        maxconn (int | None | Unset): The maximum per-process number of concurrent connections<br>
        nbthread (int | Unset): The number of threads to start per process. This setting is experimental.<br> Default:
            1.
        terminate_on_reload (bool | Unset): Enables or disables an immediate stop of old process on reload. (closes
            existing connections)<br>
        hard_stop_after (str | Unset): The maximum time allowed to perform a clean soft-stop. This can be represented as
            different time values such as 30s, 15m, 3h or 1d.<br> Default: '15m'.
        carpdev (None | str | Unset): The CARP interface IP to monitor. HAProxy will only run on the firewall whose
            interface is MASTER.<br>
        localstatsport (None | str | Unset): The internal port to be used for the stats tab. Set to null to disable
            local stats. Valid options are: a TCP/UDP port number<br>
        localstats_refreshtime (int | None | Unset): The internal (in seconds) in which local stats will be
            refreshed.<br>
        localstats_sticktable_refreshtime (int | None | Unset): The internal (in seconds) in which the sticktable stats
            will be refreshed.<br>
        remotesyslog (None | str | Unset): The IP address or hostname of the remote syslog server to send logs to. Use
            `/var/run/log` to to log to the local pfSense system log.<br>
        logfacility (HAProxySettingsLogfacility | Unset): The logging facility to log to.<br> Default:
            HAProxySettingsLogfacility.SYSLOG.
        loglevel (HAProxySettingsLoglevel | Unset): The log level to begin logging events. Only events of this level or
            higher will be logged.<br> Default: HAProxySettingsLoglevel.WARNING.
        log_send_hostname (str | Unset): The hostname field to include in the syslog header. Leave empty to use the
            system hostname.<br>
        dns_resolvers (list[HAProxySettingsDnsResolversItem] | Unset): The DNS resolvers HAProxy will use for DNS
            queries.<br>
        resolver_retries (int | Unset): The number of queries to send to resolve a server name before giving up.<br>
            Default: 3.
        resolver_timeoutretry (str | Unset): The time between two DNS queries, when no response have been received.<br>
            Default: '1s'.
        resolver_holdvalid (str | Unset): The interval between two successive name resolution when the last answer was
            valid.<br> Default: '1s'.
        email_mailers (list[HAProxySettingsEmailMailersItem] | Unset): The email servers HAProxy will use to send SMTP
            alerts.<br>
        email_level (HAProxySettingsEmailLevel | Unset): The maximum log level to send emails for. Leave empty to
            disable sending email alerts.<br>
        email_myhostname (str | Unset): The hostname to use as the origin of the email.<br>
        email_from (str | Unset): The email address to be used as the sender of the emails.<br>
        email_to (str | Unset): The email address to send emails to.<br>
        sslcompatibilitymode (HAProxySettingsSslcompatibilitymode | Unset): The SSL/TLS compatibility mode which
            determines the cipher suites and TLS versions supported.<br> Default: HAProxySettingsSslcompatibilitymode.AUTO.
        ssldefaultdhparam (int | Unset): The maximum size of the Diffie-Hellman parameters used for generating the
            ephemeral/temporary Diffie-Hellman key in case of DHE key exchange<br> Default: 1024.
        advanced (str | Unset): Additional HAProxy options to include in the global settings area.<br>
        enablesync (bool | Unset): Enables or disables including HAProxy configurations in HA sync if configured.<br>
    """

    enable: bool | Unset = UNSET
    maxconn: int | None | Unset = UNSET
    nbthread: int | Unset = 1
    terminate_on_reload: bool | Unset = UNSET
    hard_stop_after: str | Unset = "15m"
    carpdev: None | str | Unset = UNSET
    localstatsport: None | str | Unset = UNSET
    localstats_refreshtime: int | None | Unset = UNSET
    localstats_sticktable_refreshtime: int | None | Unset = UNSET
    remotesyslog: None | str | Unset = UNSET
    logfacility: HAProxySettingsLogfacility | Unset = HAProxySettingsLogfacility.SYSLOG
    loglevel: HAProxySettingsLoglevel | Unset = HAProxySettingsLoglevel.WARNING
    log_send_hostname: str | Unset = UNSET
    dns_resolvers: list[HAProxySettingsDnsResolversItem] | Unset = UNSET
    resolver_retries: int | Unset = 3
    resolver_timeoutretry: str | Unset = "1s"
    resolver_holdvalid: str | Unset = "1s"
    email_mailers: list[HAProxySettingsEmailMailersItem] | Unset = UNSET
    email_level: HAProxySettingsEmailLevel | Unset = UNSET
    email_myhostname: str | Unset = UNSET
    email_from: str | Unset = UNSET
    email_to: str | Unset = UNSET
    sslcompatibilitymode: HAProxySettingsSslcompatibilitymode | Unset = HAProxySettingsSslcompatibilitymode.AUTO
    ssldefaultdhparam: int | Unset = 1024
    advanced: str | Unset = UNSET
    enablesync: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        maxconn: int | None | Unset
        if isinstance(self.maxconn, Unset):
            maxconn = UNSET
        else:
            maxconn = self.maxconn

        nbthread = self.nbthread

        terminate_on_reload = self.terminate_on_reload

        hard_stop_after = self.hard_stop_after

        carpdev: None | str | Unset
        if isinstance(self.carpdev, Unset):
            carpdev = UNSET
        else:
            carpdev = self.carpdev

        localstatsport: None | str | Unset
        if isinstance(self.localstatsport, Unset):
            localstatsport = UNSET
        else:
            localstatsport = self.localstatsport

        localstats_refreshtime: int | None | Unset
        if isinstance(self.localstats_refreshtime, Unset):
            localstats_refreshtime = UNSET
        else:
            localstats_refreshtime = self.localstats_refreshtime

        localstats_sticktable_refreshtime: int | None | Unset
        if isinstance(self.localstats_sticktable_refreshtime, Unset):
            localstats_sticktable_refreshtime = UNSET
        else:
            localstats_sticktable_refreshtime = self.localstats_sticktable_refreshtime

        remotesyslog: None | str | Unset
        if isinstance(self.remotesyslog, Unset):
            remotesyslog = UNSET
        else:
            remotesyslog = self.remotesyslog

        logfacility: str | Unset = UNSET
        if not isinstance(self.logfacility, Unset):
            logfacility = self.logfacility.value

        loglevel: str | Unset = UNSET
        if not isinstance(self.loglevel, Unset):
            loglevel = self.loglevel.value

        log_send_hostname = self.log_send_hostname

        dns_resolvers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dns_resolvers, Unset):
            dns_resolvers = []
            for dns_resolvers_item_data in self.dns_resolvers:
                dns_resolvers_item = dns_resolvers_item_data.to_dict()
                dns_resolvers.append(dns_resolvers_item)

        resolver_retries = self.resolver_retries

        resolver_timeoutretry = self.resolver_timeoutretry

        resolver_holdvalid = self.resolver_holdvalid

        email_mailers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.email_mailers, Unset):
            email_mailers = []
            for email_mailers_item_data in self.email_mailers:
                email_mailers_item = email_mailers_item_data.to_dict()
                email_mailers.append(email_mailers_item)

        email_level: str | Unset = UNSET
        if not isinstance(self.email_level, Unset):
            email_level = self.email_level.value

        email_myhostname = self.email_myhostname

        email_from = self.email_from

        email_to = self.email_to

        sslcompatibilitymode: str | Unset = UNSET
        if not isinstance(self.sslcompatibilitymode, Unset):
            sslcompatibilitymode = self.sslcompatibilitymode.value

        ssldefaultdhparam = self.ssldefaultdhparam

        advanced = self.advanced

        enablesync = self.enablesync

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if maxconn is not UNSET:
            field_dict["maxconn"] = maxconn
        if nbthread is not UNSET:
            field_dict["nbthread"] = nbthread
        if terminate_on_reload is not UNSET:
            field_dict["terminate_on_reload"] = terminate_on_reload
        if hard_stop_after is not UNSET:
            field_dict["hard_stop_after"] = hard_stop_after
        if carpdev is not UNSET:
            field_dict["carpdev"] = carpdev
        if localstatsport is not UNSET:
            field_dict["localstatsport"] = localstatsport
        if localstats_refreshtime is not UNSET:
            field_dict["localstats_refreshtime"] = localstats_refreshtime
        if localstats_sticktable_refreshtime is not UNSET:
            field_dict["localstats_sticktable_refreshtime"] = localstats_sticktable_refreshtime
        if remotesyslog is not UNSET:
            field_dict["remotesyslog"] = remotesyslog
        if logfacility is not UNSET:
            field_dict["logfacility"] = logfacility
        if loglevel is not UNSET:
            field_dict["loglevel"] = loglevel
        if log_send_hostname is not UNSET:
            field_dict["log_send_hostname"] = log_send_hostname
        if dns_resolvers is not UNSET:
            field_dict["dns_resolvers"] = dns_resolvers
        if resolver_retries is not UNSET:
            field_dict["resolver_retries"] = resolver_retries
        if resolver_timeoutretry is not UNSET:
            field_dict["resolver_timeoutretry"] = resolver_timeoutretry
        if resolver_holdvalid is not UNSET:
            field_dict["resolver_holdvalid"] = resolver_holdvalid
        if email_mailers is not UNSET:
            field_dict["email_mailers"] = email_mailers
        if email_level is not UNSET:
            field_dict["email_level"] = email_level
        if email_myhostname is not UNSET:
            field_dict["email_myhostname"] = email_myhostname
        if email_from is not UNSET:
            field_dict["email_from"] = email_from
        if email_to is not UNSET:
            field_dict["email_to"] = email_to
        if sslcompatibilitymode is not UNSET:
            field_dict["sslcompatibilitymode"] = sslcompatibilitymode
        if ssldefaultdhparam is not UNSET:
            field_dict["ssldefaultdhparam"] = ssldefaultdhparam
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if enablesync is not UNSET:
            field_dict["enablesync"] = enablesync

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ha_proxy_settings_dns_resolvers_item import HAProxySettingsDnsResolversItem
        from ..models.ha_proxy_settings_email_mailers_item import HAProxySettingsEmailMailersItem

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        def _parse_maxconn(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        maxconn = _parse_maxconn(d.pop("maxconn", UNSET))

        nbthread = d.pop("nbthread", UNSET)

        terminate_on_reload = d.pop("terminate_on_reload", UNSET)

        hard_stop_after = d.pop("hard_stop_after", UNSET)

        def _parse_carpdev(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carpdev = _parse_carpdev(d.pop("carpdev", UNSET))

        def _parse_localstatsport(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        localstatsport = _parse_localstatsport(d.pop("localstatsport", UNSET))

        def _parse_localstats_refreshtime(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        localstats_refreshtime = _parse_localstats_refreshtime(d.pop("localstats_refreshtime", UNSET))

        def _parse_localstats_sticktable_refreshtime(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        localstats_sticktable_refreshtime = _parse_localstats_sticktable_refreshtime(
            d.pop("localstats_sticktable_refreshtime", UNSET)
        )

        def _parse_remotesyslog(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remotesyslog = _parse_remotesyslog(d.pop("remotesyslog", UNSET))

        _logfacility = d.pop("logfacility", UNSET)
        logfacility: HAProxySettingsLogfacility | Unset
        if isinstance(_logfacility, Unset):
            logfacility = UNSET
        else:
            logfacility = HAProxySettingsLogfacility(_logfacility)

        _loglevel = d.pop("loglevel", UNSET)
        loglevel: HAProxySettingsLoglevel | Unset
        if isinstance(_loglevel, Unset):
            loglevel = UNSET
        else:
            loglevel = HAProxySettingsLoglevel(_loglevel)

        log_send_hostname = d.pop("log_send_hostname", UNSET)

        _dns_resolvers = d.pop("dns_resolvers", UNSET)
        dns_resolvers: list[HAProxySettingsDnsResolversItem] | Unset = UNSET
        if _dns_resolvers is not UNSET:
            dns_resolvers = []
            for dns_resolvers_item_data in _dns_resolvers:
                dns_resolvers_item = HAProxySettingsDnsResolversItem.from_dict(dns_resolvers_item_data)

                dns_resolvers.append(dns_resolvers_item)

        resolver_retries = d.pop("resolver_retries", UNSET)

        resolver_timeoutretry = d.pop("resolver_timeoutretry", UNSET)

        resolver_holdvalid = d.pop("resolver_holdvalid", UNSET)

        _email_mailers = d.pop("email_mailers", UNSET)
        email_mailers: list[HAProxySettingsEmailMailersItem] | Unset = UNSET
        if _email_mailers is not UNSET:
            email_mailers = []
            for email_mailers_item_data in _email_mailers:
                email_mailers_item = HAProxySettingsEmailMailersItem.from_dict(email_mailers_item_data)

                email_mailers.append(email_mailers_item)

        _email_level = d.pop("email_level", UNSET)
        email_level: HAProxySettingsEmailLevel | Unset
        if isinstance(_email_level, Unset):
            email_level = UNSET
        else:
            email_level = HAProxySettingsEmailLevel(_email_level)

        email_myhostname = d.pop("email_myhostname", UNSET)

        email_from = d.pop("email_from", UNSET)

        email_to = d.pop("email_to", UNSET)

        _sslcompatibilitymode = d.pop("sslcompatibilitymode", UNSET)
        sslcompatibilitymode: HAProxySettingsSslcompatibilitymode | Unset
        if isinstance(_sslcompatibilitymode, Unset):
            sslcompatibilitymode = UNSET
        else:
            sslcompatibilitymode = HAProxySettingsSslcompatibilitymode(_sslcompatibilitymode)

        ssldefaultdhparam = d.pop("ssldefaultdhparam", UNSET)

        advanced = d.pop("advanced", UNSET)

        enablesync = d.pop("enablesync", UNSET)

        patch_services_ha_proxy_settings_endpoint_json_body = cls(
            enable=enable,
            maxconn=maxconn,
            nbthread=nbthread,
            terminate_on_reload=terminate_on_reload,
            hard_stop_after=hard_stop_after,
            carpdev=carpdev,
            localstatsport=localstatsport,
            localstats_refreshtime=localstats_refreshtime,
            localstats_sticktable_refreshtime=localstats_sticktable_refreshtime,
            remotesyslog=remotesyslog,
            logfacility=logfacility,
            loglevel=loglevel,
            log_send_hostname=log_send_hostname,
            dns_resolvers=dns_resolvers,
            resolver_retries=resolver_retries,
            resolver_timeoutretry=resolver_timeoutretry,
            resolver_holdvalid=resolver_holdvalid,
            email_mailers=email_mailers,
            email_level=email_level,
            email_myhostname=email_myhostname,
            email_from=email_from,
            email_to=email_to,
            sslcompatibilitymode=sslcompatibilitymode,
            ssldefaultdhparam=ssldefaultdhparam,
            advanced=advanced,
            enablesync=enablesync,
        )

        patch_services_ha_proxy_settings_endpoint_json_body.additional_properties = d
        return patch_services_ha_proxy_settings_endpoint_json_body

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
