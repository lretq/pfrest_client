from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.restapi_settings_log_level import RESTAPISettingsLogLevel
from ..models.restapi_settings_represent_interfaces_as import RESTAPISettingsRepresentInterfacesAs
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchSystemRESTAPISettingsEndpointJsonBody")


@_attrs_define
class PatchSystemRESTAPISettingsEndpointJsonBody:
    """
    Attributes:
        enabled (bool | Unset): Enables or disables the API. If set to `false`, the API will no longer respond to API
            requests
                        and can only be re-enabled via webConfigurator.<br> Default: True.
        read_only (bool | Unset): Enables or disables read-only API access. If enabled, the API will only respond to GET
            requests
                        and can only be disabled via webConfigurator.<br>
        keep_backup (bool | Unset): Enables or disables keeping a persistent backup of the API configuration that can be
            used
                        to restore the API configuration after package and systems updates.<br> Default: True.
        login_protection (bool | Unset): Enables or disables Login Protection for API authentication. When enabled,
            Login Protection will
                        monitor API attempts and temporarily block clients who fail API authentication too many times within
            a
                        period of time. When disabled, Login Protection will not monitor API authentication but will
            continue to
                        monitor webConfigurator and SSH logins (if configured). Login Protection can be configured globally
            in
                        System > Advanced.<br> Default: True.
        log_successful_auth (bool | Unset): Enables or disables logging of API authentication attempts that are
            successful. By default, only
                        failed API authentication attempts are logged to prevent flooding the authentication logs. This
            field is
                        only applicable when the API `login_protection` setting is enabled.<br>
        log_level (RESTAPISettingsLogLevel | Unset): Sets the log level for API logging. The log level determines the
            minimum severity of messages
                        that should be logged.<br> Default: RESTAPISettingsLogLevel.LOG_WARNING.
        allow_pre_releases (bool | Unset): Enables or disables displaying pre-releases in available API updates. Pre-
            releases contain fixes
                        and features that are currently under development and may not be fully stable. Use of pre-release
            versions
                        is at your own risk.<br>
        allow_development_packages (bool | Unset): Enables or disables allowing the use of development (-devel) variants
            of pfSense packages when a package is required by specific API endpoints. Use of development packages is at your
            own risk.<br>
        hateoas (bool | Unset): Enables or disables HATEOAS. Enabling HATEOAS will allow the API to include links to
            related resources in API responses. This is primarily useful for frontend web applications and self-navigating
            client scripts that integrate with HAL standards. Enabling HATEOAS may increase API response times, especially
            on systems with large configurations.<br>
        expose_sensitive_fields (bool | Unset): Enables or disables exposing sensitive fields in API responses. When
            enabled, sensitive fields such as passwords, private keys, and other sensitive data will be included in API
            responses.<br>
        override_sensitive_fields (list[str] | Unset): Specifies a list of fields (formatted as ModelName:FieldName)
            that should have their sensitive attribute overridden. Fields selected here will not be considered sensitive and
            will be included in API responses regardless of the `expose_sensitive_fields` setting.<br><br>This field is only
            available when the following conditions are met:<br>- `expose_sensitive_fields` must be equal to `false`<br>
        allowed_interfaces (list[str] | Unset): Sets the interfaces allowed to accept incoming API calls.<br>
        represent_interfaces_as (RESTAPISettingsRepresentInterfacesAs | Unset): Specifies how the API should represent
            interface names. Use `descr` to represent
                        interface objects by their description name, use `id` to represent interface objects by their
                        internal pfSense ID (e.g. wan, lan, opt1), or use `if` to represent interface objects by their
                        real interface name (e.g. em0, igb1, bxe3).<br> Default: RESTAPISettingsRepresentInterfacesAs.DESCR.
        auth_methods (list[str] | Unset): Sets the API authentication methods allowed to authenticate API calls.<br>
        jwt_exp (int | Unset): Sets the amount of time (in seconds) JWTs are valid for.<br> Default: 3600.
        ha_sync (bool | Unset): Enables or disables syncing API settings to HA peers. When enabled, API settings from
            this
                        host will automatically be synced to any hosts defined in `ha_sync_hosts`.<br>
        ha_sync_validate_certs (bool | Unset): Enables or disables certificate validation when syncing API
            configurations to HA sync peers. If
                        enabled, all hosts defined in `ha_sync_hosts` must have their webConfigurator configured with a
            certificate
                        trusted by this system. It is strongly recommended this be enabled at all times to help mitigate
                        Man-in-the-Middle attacks.<br> Default: True.
        ha_sync_hosts (list[str] | Unset): Set a list of IP addresses or hostnames to sync API settings to.<br>
        ha_sync_username (str | Unset): Sets the username to use when authenticating for HA sync processes. This user
            must be the present
                        on all hosts defined in `ha_sync_hosts`.<br>
        ha_sync_password (str | Unset): Sets the password to use when authenticating for HA sync processes. This must be
            the password
                        for the user defined in `ha_sync_username` and must be the same on all hosts defined in
            `ha_sync_hosts`.<br>
    """

    enabled: bool | Unset = True
    read_only: bool | Unset = UNSET
    keep_backup: bool | Unset = True
    login_protection: bool | Unset = True
    log_successful_auth: bool | Unset = UNSET
    log_level: RESTAPISettingsLogLevel | Unset = RESTAPISettingsLogLevel.LOG_WARNING
    allow_pre_releases: bool | Unset = UNSET
    allow_development_packages: bool | Unset = UNSET
    hateoas: bool | Unset = UNSET
    expose_sensitive_fields: bool | Unset = UNSET
    override_sensitive_fields: list[str] | Unset = UNSET
    allowed_interfaces: list[str] | Unset = UNSET
    represent_interfaces_as: RESTAPISettingsRepresentInterfacesAs | Unset = RESTAPISettingsRepresentInterfacesAs.DESCR
    auth_methods: list[str] | Unset = UNSET
    jwt_exp: int | Unset = 3600
    ha_sync: bool | Unset = UNSET
    ha_sync_validate_certs: bool | Unset = True
    ha_sync_hosts: list[str] | Unset = UNSET
    ha_sync_username: str | Unset = UNSET
    ha_sync_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        read_only = self.read_only

        keep_backup = self.keep_backup

        login_protection = self.login_protection

        log_successful_auth = self.log_successful_auth

        log_level: str | Unset = UNSET
        if not isinstance(self.log_level, Unset):
            log_level = self.log_level.value

        allow_pre_releases = self.allow_pre_releases

        allow_development_packages = self.allow_development_packages

        hateoas = self.hateoas

        expose_sensitive_fields = self.expose_sensitive_fields

        override_sensitive_fields: list[str] | Unset = UNSET
        if not isinstance(self.override_sensitive_fields, Unset):
            override_sensitive_fields = self.override_sensitive_fields

        allowed_interfaces: list[str] | Unset = UNSET
        if not isinstance(self.allowed_interfaces, Unset):
            allowed_interfaces = self.allowed_interfaces

        represent_interfaces_as: str | Unset = UNSET
        if not isinstance(self.represent_interfaces_as, Unset):
            represent_interfaces_as = self.represent_interfaces_as.value

        auth_methods: list[str] | Unset = UNSET
        if not isinstance(self.auth_methods, Unset):
            auth_methods = self.auth_methods

        jwt_exp = self.jwt_exp

        ha_sync = self.ha_sync

        ha_sync_validate_certs = self.ha_sync_validate_certs

        ha_sync_hosts: list[str] | Unset = UNSET
        if not isinstance(self.ha_sync_hosts, Unset):
            ha_sync_hosts = self.ha_sync_hosts

        ha_sync_username = self.ha_sync_username

        ha_sync_password = self.ha_sync_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if read_only is not UNSET:
            field_dict["read_only"] = read_only
        if keep_backup is not UNSET:
            field_dict["keep_backup"] = keep_backup
        if login_protection is not UNSET:
            field_dict["login_protection"] = login_protection
        if log_successful_auth is not UNSET:
            field_dict["log_successful_auth"] = log_successful_auth
        if log_level is not UNSET:
            field_dict["log_level"] = log_level
        if allow_pre_releases is not UNSET:
            field_dict["allow_pre_releases"] = allow_pre_releases
        if allow_development_packages is not UNSET:
            field_dict["allow_development_packages"] = allow_development_packages
        if hateoas is not UNSET:
            field_dict["hateoas"] = hateoas
        if expose_sensitive_fields is not UNSET:
            field_dict["expose_sensitive_fields"] = expose_sensitive_fields
        if override_sensitive_fields is not UNSET:
            field_dict["override_sensitive_fields"] = override_sensitive_fields
        if allowed_interfaces is not UNSET:
            field_dict["allowed_interfaces"] = allowed_interfaces
        if represent_interfaces_as is not UNSET:
            field_dict["represent_interfaces_as"] = represent_interfaces_as
        if auth_methods is not UNSET:
            field_dict["auth_methods"] = auth_methods
        if jwt_exp is not UNSET:
            field_dict["jwt_exp"] = jwt_exp
        if ha_sync is not UNSET:
            field_dict["ha_sync"] = ha_sync
        if ha_sync_validate_certs is not UNSET:
            field_dict["ha_sync_validate_certs"] = ha_sync_validate_certs
        if ha_sync_hosts is not UNSET:
            field_dict["ha_sync_hosts"] = ha_sync_hosts
        if ha_sync_username is not UNSET:
            field_dict["ha_sync_username"] = ha_sync_username
        if ha_sync_password is not UNSET:
            field_dict["ha_sync_password"] = ha_sync_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        read_only = d.pop("read_only", UNSET)

        keep_backup = d.pop("keep_backup", UNSET)

        login_protection = d.pop("login_protection", UNSET)

        log_successful_auth = d.pop("log_successful_auth", UNSET)

        _log_level = d.pop("log_level", UNSET)
        log_level: RESTAPISettingsLogLevel | Unset
        if isinstance(_log_level, Unset):
            log_level = UNSET
        else:
            log_level = RESTAPISettingsLogLevel(_log_level)

        allow_pre_releases = d.pop("allow_pre_releases", UNSET)

        allow_development_packages = d.pop("allow_development_packages", UNSET)

        hateoas = d.pop("hateoas", UNSET)

        expose_sensitive_fields = d.pop("expose_sensitive_fields", UNSET)

        override_sensitive_fields = cast(list[str], d.pop("override_sensitive_fields", UNSET))

        allowed_interfaces = cast(list[str], d.pop("allowed_interfaces", UNSET))

        _represent_interfaces_as = d.pop("represent_interfaces_as", UNSET)
        represent_interfaces_as: RESTAPISettingsRepresentInterfacesAs | Unset
        if isinstance(_represent_interfaces_as, Unset):
            represent_interfaces_as = UNSET
        else:
            represent_interfaces_as = RESTAPISettingsRepresentInterfacesAs(_represent_interfaces_as)

        auth_methods = cast(list[str], d.pop("auth_methods", UNSET))

        jwt_exp = d.pop("jwt_exp", UNSET)

        ha_sync = d.pop("ha_sync", UNSET)

        ha_sync_validate_certs = d.pop("ha_sync_validate_certs", UNSET)

        ha_sync_hosts = cast(list[str], d.pop("ha_sync_hosts", UNSET))

        ha_sync_username = d.pop("ha_sync_username", UNSET)

        ha_sync_password = d.pop("ha_sync_password", UNSET)

        patch_system_restapi_settings_endpoint_json_body = cls(
            enabled=enabled,
            read_only=read_only,
            keep_backup=keep_backup,
            login_protection=login_protection,
            log_successful_auth=log_successful_auth,
            log_level=log_level,
            allow_pre_releases=allow_pre_releases,
            allow_development_packages=allow_development_packages,
            hateoas=hateoas,
            expose_sensitive_fields=expose_sensitive_fields,
            override_sensitive_fields=override_sensitive_fields,
            allowed_interfaces=allowed_interfaces,
            represent_interfaces_as=represent_interfaces_as,
            auth_methods=auth_methods,
            jwt_exp=jwt_exp,
            ha_sync=ha_sync,
            ha_sync_validate_certs=ha_sync_validate_certs,
            ha_sync_hosts=ha_sync_hosts,
            ha_sync_username=ha_sync_username,
            ha_sync_password=ha_sync_password,
        )

        patch_system_restapi_settings_endpoint_json_body.additional_properties = d
        return patch_system_restapi_settings_endpoint_json_body

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
