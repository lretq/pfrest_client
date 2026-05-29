from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ha_proxy_backend_balance import HAProxyBackendBalance
from ..models.ha_proxy_backend_check_type import HAProxyBackendCheckType
from ..models.ha_proxy_backend_email_level import HAProxyBackendEmailLevel
from ..models.ha_proxy_backend_httpcheck_method import HAProxyBackendHttpcheckMethod
from ..models.ha_proxy_backend_persist_cookie_mode import HAProxyBackendPersistCookieMode
from ..models.ha_proxy_backend_persist_sticky_type import HAProxyBackendPersistStickyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ha_proxy_backend_acls_item import HAProxyBackendAclsItem
    from ..models.ha_proxy_backend_actions_item import HAProxyBackendActionsItem
    from ..models.ha_proxy_backend_errorfiles_item import HAProxyBackendErrorfilesItem
    from ..models.ha_proxy_backend_servers_item import HAProxyBackendServersItem


T = TypeVar("T", bound="HAProxyBackend")


@_attrs_define
class HAProxyBackend:
    """
    Attributes:
        name (str | Unset): The unique name for this backend.<br>
        servers (list[HAProxyBackendServersItem] | Unset): The pool of servers this backend will use.<br>
        balance (HAProxyBackendBalance | Unset): The load balancing option to use for servers assigned to this
            backend.<br>
        balance_urilen (int | None | Unset): The number of URI characters the algorithm should consider when
            hashing.<br><br>This field is only available when the following conditions are met:<br>- `balance` must be equal
            to `'uri'`<br>
        balance_uridepth (int | None | Unset): The maximum directory depth to be used to compute the hash. One level is
            counted for each slash in the request.<br><br>This field is only available when the following conditions are
            met:<br>- `balance` must be equal to `'uri'`<br>
        balance_uriwhole (bool | Unset): Enables or disables allowing the use of whole URIs, including URL
            parameters.<br><br>This field is only available when the following conditions are met:<br>- `balance` must be
            equal to `'uri'`<br>
        acls (list[HAProxyBackendAclsItem] | Unset): The ACLs to apply to this backend.<br>
        actions (list[HAProxyBackendActionsItem] | Unset): The actions to apply to this backend.<br>
        connection_timeout (int | None | Unset): The amount of time (in milliseconds) to wait before giving up on
            connections.<br> Default: 30000.
        server_timeout (int | None | Unset): The amount of time (in milliseconds) to wait for data transferred to or
            from the server.<br> Default: 30000.
        retries (int | None | Unset): The number of retry attempts to allow after a connection failure to the
            server.<br>
        check_type (HAProxyBackendCheckType | Unset): The health check method to use when checking the health of backend
            servers.<br> Default: HAProxyBackendCheckType.NONE.
        checkinter (int | None | Unset): The interval (in milliseconds) in which health checks will be
            performed.<br><br>This field is only available when the following conditions are met:<br>- `check_type` must not
            be equal to `'none'`<br>
        log_health_checks (bool | Unset): Enables or disables logging changes to the health check status<br><br>This
            field is only available when the following conditions are met:<br>- `check_type` must not be equal to
            `'none'`<br>
        httpcheck_method (HAProxyBackendHttpcheckMethod | Unset): The HTTP method to use for HTTP health
            checks.<br><br>This field is only available when the following conditions are met:<br>- `check_type` must be
            equal to `'HTTP'`<br> Default: HAProxyBackendHttpcheckMethod.OPTIONS.
        monitor_uri (str | Unset): The URL to use for HTTP health checks.<br><br>This field is only available when the
            following conditions are met:<br>- `check_type` must be equal to `'HTTP'`<br> Default: '/'.
        monitor_httpversion (str | Unset): The HTTP version to use for HTTP health checks.<br><br>This field is only
            available when the following conditions are met:<br>- `check_type` must be equal to `'HTTP'`<br> Default:
            'HTTP/1.0'.
        monitor_username (str | Unset): The username to use for MySQL or PostgreSQL health checks.<br><br>This field is
            only available when the following conditions are met:<br>- `check_type` must be one of [ MySQL, PostgreSQL ]<br>
        monitor_domain (str | Unset): The domain to use for SMTP or ESMTP health checks.<br><br>This field is only
            available when the following conditions are met:<br>- `check_type` must be one of [ SMTP, ESMTP ]<br>
        agent_checks (bool | Unset): Enables or disables using a TCP connection to read an ASCII string of the form.<br>
        agent_port (str | Unset):  Valid options are: a TCP/UDP port number<br><br>This field is only available when the
            following conditions are met:<br>- `agent_checks` must be equal to `true`<br>
        agent_inter (int | None | Unset): The interval (in milliseconds) between agent checks.<br><br>This field is only
            available when the following conditions are met:<br>- `agent_checks` must be equal to `true`<br> Default: 2000.
        persist_cookie_enabled (bool | Unset): Enables or disables cookie based persistence.<br>
        persist_cookie_name (str | Unset): The string name to track in Set-Cookie and Cookie HTTP headers.<br><br>This
            field is only available when the following conditions are met:<br>- `persist_cookie_enabled` must be equal to
            `true`<br>
        persist_cookie_mode (HAProxyBackendPersistCookieMode | Unset): The mode HAProxy uses to insert/prefix/replace or
            examine cookie and set-cookie headers.<br><br>This field is only available when the following conditions are
            met:<br>- `persist_cookie_enabled` must be equal to `true`<br> Default: HAProxyBackendPersistCookieMode.PASSIVE.
        persist_cookie_cachable (bool | Unset): Enables or disables allowing shared caches to cache the server
            response.<br><br>This field is only available when the following conditions are met:<br>-
            `persist_cookie_enabled` must be equal to `true`<br>
        persist_cookie_postonly (bool | Unset): Enables or disables only inserting cookies on POST requests.<br><br>This
            field is only available when the following conditions are met:<br>- `persist_cookie_enabled` must be equal to
            `true`<br>
        persist_cookie_httponly (bool | Unset): Enables or disables preventing the use of cookies with non-HTTP
            components.<br><br>This field is only available when the following conditions are met:<br>-
            `persist_cookie_enabled` must be equal to `true`<br>
        persist_cookie_secure (bool | Unset): Enables or disables prevention of cookie usage over non-secure
            channels.<br><br>This field is only available when the following conditions are met:<br>-
            `persist_cookie_enabled` must be equal to `true`<br>
        haproxy_cookie_maxidle (int | None | Unset): The max-idle time to allow. This option only applies to insert mode
            cookies.<br><br>This field is only available when the following conditions are met:<br>-
            `persist_cookie_enabled` must be equal to `true`<br>
        haproxy_cookie_maxlife (int | None | Unset): The max-life time to allow. This option only applies to insert mode
            cookies.<br><br>This field is only available when the following conditions are met:<br>-
            `persist_cookie_enabled` must be equal to `true`<br>
        haproxy_cookie_domains (list[str] | Unset): The domains to set the cookies for.<br><br>This field is only
            available when the following conditions are met:<br>- `persist_cookie_enabled` must be equal to `true`<br>
        haproxy_cookie_dynamic_cookie_key (str | Unset): The dynamic cookie secret key. This is will be used to generate
            dynamic cookies for this backend.<br><br>This field is only available when the following conditions are
            met:<br>- `persist_cookie_enabled` must be equal to `true`<br>
        persist_sticky_type (HAProxyBackendPersistStickyType | Unset): The sticky table mode to use for this backend.
            These options are used to make sure subsequent requests from a single client go to the same backend.<br>
            Default: HAProxyBackendPersistStickyType.NONE.
        persist_stick_expire (str | Unset): The maximum duration of an entry in the stick-table since it was last
            created, refreshed or matched.<br><br>This field is only available when the following conditions are met:<br>-
            `persist_sticky_type` must not be equal to `'none'`<br>
        persist_stick_tablesize (str | Unset): The maximum number of entries allowed in the table. This value directly
            impacts memory usage.<br><br>This field is only available when the following conditions are met:<br>-
            `persist_sticky_type` must not be equal to `'none'`<br>
        persist_stick_cookiename (str | Unset): The cookie name to use for stick table.<br><br>This field is only
            available when the following conditions are met:<br>- `persist_sticky_type` must be one of [ stick_cookie_value,
            stick_rdp_cookie ]<br>
        persist_stick_length (int | None | Unset): The maximum number of characters allowed in a string type stick
            table<br><br>This field is only available when the following conditions are met:<br>- `persist_sticky_type` must
            be one of [ stick_cookie_value, stick_rdp_cookie ]<br>
        email_level (HAProxyBackendEmailLevel | Unset): The maximum log level to send emails for. Leave empty to disable
            sending email alerts. If left empty, the value set in the global settings will be used.<br>
        email_to (str | Unset): The email address to send emails to. If left empty, the value set in the global settings
            will be used.<br>
        stats_enabled (bool | Unset): Enables or disables the HAProxy statistics page for this backend.<br>
        stats_uri (str | Unset): The statistics URL for this backend.<br><br>This field is only available when the
            following conditions are met:<br>- `stats_enabled` must be equal to `true`<br>
        stats_scope (list[str] | Unset): The frontends and backends stats to be shown, leave empty to show
            all.<br><br>This field is only available when the following conditions are met:<br>- `stats_enabled` must be
            equal to `true`<br>
        stats_realm (str | Unset): The realm that is shown when authentication is requested by HAProxy.<br><br>This
            field is only available when the following conditions are met:<br>- `stats_enabled` must be equal to `true`<br>
        stats_username (str | Unset): The stats page username<br><br>This field is only available when the following
            conditions are met:<br>- `stats_enabled` must be equal to `true`<br>
        stats_password (str | Unset): The stats page password.<br><br>This field is only available when the following
            conditions are met:<br>- `stats_enabled` must be equal to `true`<br>
        stats_admin (str | Unset): The admin to make use of the options disable/enable/softstop/softstart/killsessions
            from the stats page.<br><br>This field is only available when the following conditions are met:<br>-
            `stats_enabled` must be equal to `true`<br>
        stats_node (str | Unset): The short name displayed in stats and helps differentiate which server in the cluster
            is actually serving clients.<br><br>This field is only available when the following conditions are met:<br>-
            `stats_enabled` must be equal to `true`<br>
        stats_desc (str | Unset): The verbose description for this node.<br><br>This field is only available when the
            following conditions are met:<br>- `stats_enabled` must be equal to `true`<br>
        stats_refresh (int | Unset): The interval (in seconds) in which the stats page is refreshed.<br><br>This field
            is only available when the following conditions are met:<br>- `stats_enabled` must be equal to `true`<br>
            Default: 10.
        strict_transport_security (int | None | Unset): The HSTS validity period for this backend. Leave empty to
            disable HSTS.<br>
        errorfiles (list[HAProxyBackendErrorfilesItem] | Unset): The HAProxy error file mappings to use for this
            backend.<br>
        cookie_attribute_secure (bool | Unset): Enables or disables assigning the secure attributes on cookies for this
            backend.<br>
        advanced (str | Unset): The per server pass thru to apply to each server line.<br>
        advanced_backend (str | Unset): The backend pass thru to apply to the backend section.<br>
        transparent_clientip (bool | Unset): Enables or disables using the client-IP to connect to backend servers.<br>
        transparent_interface (None | str | Unset): The interface that will connect to the backend server.<br><br>This
            field is only available when the following conditions are met:<br>- `transparent_clientip` must be equal to
            `true`<br>
    """

    name: str | Unset = UNSET
    servers: list[HAProxyBackendServersItem] | Unset = UNSET
    balance: HAProxyBackendBalance | Unset = UNSET
    balance_urilen: int | None | Unset = UNSET
    balance_uridepth: int | None | Unset = UNSET
    balance_uriwhole: bool | Unset = UNSET
    acls: list[HAProxyBackendAclsItem] | Unset = UNSET
    actions: list[HAProxyBackendActionsItem] | Unset = UNSET
    connection_timeout: int | None | Unset = 30000
    server_timeout: int | None | Unset = 30000
    retries: int | None | Unset = UNSET
    check_type: HAProxyBackendCheckType | Unset = HAProxyBackendCheckType.NONE
    checkinter: int | None | Unset = UNSET
    log_health_checks: bool | Unset = UNSET
    httpcheck_method: HAProxyBackendHttpcheckMethod | Unset = HAProxyBackendHttpcheckMethod.OPTIONS
    monitor_uri: str | Unset = "/"
    monitor_httpversion: str | Unset = "HTTP/1.0"
    monitor_username: str | Unset = UNSET
    monitor_domain: str | Unset = UNSET
    agent_checks: bool | Unset = UNSET
    agent_port: str | Unset = UNSET
    agent_inter: int | None | Unset = 2000
    persist_cookie_enabled: bool | Unset = UNSET
    persist_cookie_name: str | Unset = UNSET
    persist_cookie_mode: HAProxyBackendPersistCookieMode | Unset = HAProxyBackendPersistCookieMode.PASSIVE
    persist_cookie_cachable: bool | Unset = UNSET
    persist_cookie_postonly: bool | Unset = UNSET
    persist_cookie_httponly: bool | Unset = UNSET
    persist_cookie_secure: bool | Unset = UNSET
    haproxy_cookie_maxidle: int | None | Unset = UNSET
    haproxy_cookie_maxlife: int | None | Unset = UNSET
    haproxy_cookie_domains: list[str] | Unset = UNSET
    haproxy_cookie_dynamic_cookie_key: str | Unset = UNSET
    persist_sticky_type: HAProxyBackendPersistStickyType | Unset = HAProxyBackendPersistStickyType.NONE
    persist_stick_expire: str | Unset = UNSET
    persist_stick_tablesize: str | Unset = UNSET
    persist_stick_cookiename: str | Unset = UNSET
    persist_stick_length: int | None | Unset = UNSET
    email_level: HAProxyBackendEmailLevel | Unset = UNSET
    email_to: str | Unset = UNSET
    stats_enabled: bool | Unset = UNSET
    stats_uri: str | Unset = UNSET
    stats_scope: list[str] | Unset = UNSET
    stats_realm: str | Unset = UNSET
    stats_username: str | Unset = UNSET
    stats_password: str | Unset = UNSET
    stats_admin: str | Unset = UNSET
    stats_node: str | Unset = UNSET
    stats_desc: str | Unset = UNSET
    stats_refresh: int | Unset = 10
    strict_transport_security: int | None | Unset = UNSET
    errorfiles: list[HAProxyBackendErrorfilesItem] | Unset = UNSET
    cookie_attribute_secure: bool | Unset = UNSET
    advanced: str | Unset = UNSET
    advanced_backend: str | Unset = UNSET
    transparent_clientip: bool | Unset = UNSET
    transparent_interface: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        servers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = []
            for servers_item_data in self.servers:
                servers_item = servers_item_data.to_dict()
                servers.append(servers_item)

        balance: str | Unset = UNSET
        if not isinstance(self.balance, Unset):
            balance = self.balance.value

        balance_urilen: int | None | Unset
        if isinstance(self.balance_urilen, Unset):
            balance_urilen = UNSET
        else:
            balance_urilen = self.balance_urilen

        balance_uridepth: int | None | Unset
        if isinstance(self.balance_uridepth, Unset):
            balance_uridepth = UNSET
        else:
            balance_uridepth = self.balance_uridepth

        balance_uriwhole = self.balance_uriwhole

        acls: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acls, Unset):
            acls = []
            for acls_item_data in self.acls:
                acls_item = acls_item_data.to_dict()
                acls.append(acls_item)

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        connection_timeout: int | None | Unset
        if isinstance(self.connection_timeout, Unset):
            connection_timeout = UNSET
        else:
            connection_timeout = self.connection_timeout

        server_timeout: int | None | Unset
        if isinstance(self.server_timeout, Unset):
            server_timeout = UNSET
        else:
            server_timeout = self.server_timeout

        retries: int | None | Unset
        if isinstance(self.retries, Unset):
            retries = UNSET
        else:
            retries = self.retries

        check_type: str | Unset = UNSET
        if not isinstance(self.check_type, Unset):
            check_type = self.check_type.value

        checkinter: int | None | Unset
        if isinstance(self.checkinter, Unset):
            checkinter = UNSET
        else:
            checkinter = self.checkinter

        log_health_checks = self.log_health_checks

        httpcheck_method: str | Unset = UNSET
        if not isinstance(self.httpcheck_method, Unset):
            httpcheck_method = self.httpcheck_method.value

        monitor_uri = self.monitor_uri

        monitor_httpversion = self.monitor_httpversion

        monitor_username = self.monitor_username

        monitor_domain = self.monitor_domain

        agent_checks = self.agent_checks

        agent_port = self.agent_port

        agent_inter: int | None | Unset
        if isinstance(self.agent_inter, Unset):
            agent_inter = UNSET
        else:
            agent_inter = self.agent_inter

        persist_cookie_enabled = self.persist_cookie_enabled

        persist_cookie_name = self.persist_cookie_name

        persist_cookie_mode: str | Unset = UNSET
        if not isinstance(self.persist_cookie_mode, Unset):
            persist_cookie_mode = self.persist_cookie_mode.value

        persist_cookie_cachable = self.persist_cookie_cachable

        persist_cookie_postonly = self.persist_cookie_postonly

        persist_cookie_httponly = self.persist_cookie_httponly

        persist_cookie_secure = self.persist_cookie_secure

        haproxy_cookie_maxidle: int | None | Unset
        if isinstance(self.haproxy_cookie_maxidle, Unset):
            haproxy_cookie_maxidle = UNSET
        else:
            haproxy_cookie_maxidle = self.haproxy_cookie_maxidle

        haproxy_cookie_maxlife: int | None | Unset
        if isinstance(self.haproxy_cookie_maxlife, Unset):
            haproxy_cookie_maxlife = UNSET
        else:
            haproxy_cookie_maxlife = self.haproxy_cookie_maxlife

        haproxy_cookie_domains: list[str] | Unset = UNSET
        if not isinstance(self.haproxy_cookie_domains, Unset):
            haproxy_cookie_domains = self.haproxy_cookie_domains

        haproxy_cookie_dynamic_cookie_key = self.haproxy_cookie_dynamic_cookie_key

        persist_sticky_type: str | Unset = UNSET
        if not isinstance(self.persist_sticky_type, Unset):
            persist_sticky_type = self.persist_sticky_type.value

        persist_stick_expire = self.persist_stick_expire

        persist_stick_tablesize = self.persist_stick_tablesize

        persist_stick_cookiename = self.persist_stick_cookiename

        persist_stick_length: int | None | Unset
        if isinstance(self.persist_stick_length, Unset):
            persist_stick_length = UNSET
        else:
            persist_stick_length = self.persist_stick_length

        email_level: str | Unset = UNSET
        if not isinstance(self.email_level, Unset):
            email_level = self.email_level.value

        email_to = self.email_to

        stats_enabled = self.stats_enabled

        stats_uri = self.stats_uri

        stats_scope: list[str] | Unset = UNSET
        if not isinstance(self.stats_scope, Unset):
            stats_scope = self.stats_scope

        stats_realm = self.stats_realm

        stats_username = self.stats_username

        stats_password = self.stats_password

        stats_admin = self.stats_admin

        stats_node = self.stats_node

        stats_desc = self.stats_desc

        stats_refresh = self.stats_refresh

        strict_transport_security: int | None | Unset
        if isinstance(self.strict_transport_security, Unset):
            strict_transport_security = UNSET
        else:
            strict_transport_security = self.strict_transport_security

        errorfiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errorfiles, Unset):
            errorfiles = []
            for errorfiles_item_data in self.errorfiles:
                errorfiles_item = errorfiles_item_data.to_dict()
                errorfiles.append(errorfiles_item)

        cookie_attribute_secure = self.cookie_attribute_secure

        advanced = self.advanced

        advanced_backend = self.advanced_backend

        transparent_clientip = self.transparent_clientip

        transparent_interface: None | str | Unset
        if isinstance(self.transparent_interface, Unset):
            transparent_interface = UNSET
        else:
            transparent_interface = self.transparent_interface

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if servers is not UNSET:
            field_dict["servers"] = servers
        if balance is not UNSET:
            field_dict["balance"] = balance
        if balance_urilen is not UNSET:
            field_dict["balance_urilen"] = balance_urilen
        if balance_uridepth is not UNSET:
            field_dict["balance_uridepth"] = balance_uridepth
        if balance_uriwhole is not UNSET:
            field_dict["balance_uriwhole"] = balance_uriwhole
        if acls is not UNSET:
            field_dict["acls"] = acls
        if actions is not UNSET:
            field_dict["actions"] = actions
        if connection_timeout is not UNSET:
            field_dict["connection_timeout"] = connection_timeout
        if server_timeout is not UNSET:
            field_dict["server_timeout"] = server_timeout
        if retries is not UNSET:
            field_dict["retries"] = retries
        if check_type is not UNSET:
            field_dict["check_type"] = check_type
        if checkinter is not UNSET:
            field_dict["checkinter"] = checkinter
        if log_health_checks is not UNSET:
            field_dict["log_health_checks"] = log_health_checks
        if httpcheck_method is not UNSET:
            field_dict["httpcheck_method"] = httpcheck_method
        if monitor_uri is not UNSET:
            field_dict["monitor_uri"] = monitor_uri
        if monitor_httpversion is not UNSET:
            field_dict["monitor_httpversion"] = monitor_httpversion
        if monitor_username is not UNSET:
            field_dict["monitor_username"] = monitor_username
        if monitor_domain is not UNSET:
            field_dict["monitor_domain"] = monitor_domain
        if agent_checks is not UNSET:
            field_dict["agent_checks"] = agent_checks
        if agent_port is not UNSET:
            field_dict["agent_port"] = agent_port
        if agent_inter is not UNSET:
            field_dict["agent_inter"] = agent_inter
        if persist_cookie_enabled is not UNSET:
            field_dict["persist_cookie_enabled"] = persist_cookie_enabled
        if persist_cookie_name is not UNSET:
            field_dict["persist_cookie_name"] = persist_cookie_name
        if persist_cookie_mode is not UNSET:
            field_dict["persist_cookie_mode"] = persist_cookie_mode
        if persist_cookie_cachable is not UNSET:
            field_dict["persist_cookie_cachable"] = persist_cookie_cachable
        if persist_cookie_postonly is not UNSET:
            field_dict["persist_cookie_postonly"] = persist_cookie_postonly
        if persist_cookie_httponly is not UNSET:
            field_dict["persist_cookie_httponly"] = persist_cookie_httponly
        if persist_cookie_secure is not UNSET:
            field_dict["persist_cookie_secure"] = persist_cookie_secure
        if haproxy_cookie_maxidle is not UNSET:
            field_dict["haproxy_cookie_maxidle"] = haproxy_cookie_maxidle
        if haproxy_cookie_maxlife is not UNSET:
            field_dict["haproxy_cookie_maxlife"] = haproxy_cookie_maxlife
        if haproxy_cookie_domains is not UNSET:
            field_dict["haproxy_cookie_domains"] = haproxy_cookie_domains
        if haproxy_cookie_dynamic_cookie_key is not UNSET:
            field_dict["haproxy_cookie_dynamic_cookie_key"] = haproxy_cookie_dynamic_cookie_key
        if persist_sticky_type is not UNSET:
            field_dict["persist_sticky_type"] = persist_sticky_type
        if persist_stick_expire is not UNSET:
            field_dict["persist_stick_expire"] = persist_stick_expire
        if persist_stick_tablesize is not UNSET:
            field_dict["persist_stick_tablesize"] = persist_stick_tablesize
        if persist_stick_cookiename is not UNSET:
            field_dict["persist_stick_cookiename"] = persist_stick_cookiename
        if persist_stick_length is not UNSET:
            field_dict["persist_stick_length"] = persist_stick_length
        if email_level is not UNSET:
            field_dict["email_level"] = email_level
        if email_to is not UNSET:
            field_dict["email_to"] = email_to
        if stats_enabled is not UNSET:
            field_dict["stats_enabled"] = stats_enabled
        if stats_uri is not UNSET:
            field_dict["stats_uri"] = stats_uri
        if stats_scope is not UNSET:
            field_dict["stats_scope"] = stats_scope
        if stats_realm is not UNSET:
            field_dict["stats_realm"] = stats_realm
        if stats_username is not UNSET:
            field_dict["stats_username"] = stats_username
        if stats_password is not UNSET:
            field_dict["stats_password"] = stats_password
        if stats_admin is not UNSET:
            field_dict["stats_admin"] = stats_admin
        if stats_node is not UNSET:
            field_dict["stats_node"] = stats_node
        if stats_desc is not UNSET:
            field_dict["stats_desc"] = stats_desc
        if stats_refresh is not UNSET:
            field_dict["stats_refresh"] = stats_refresh
        if strict_transport_security is not UNSET:
            field_dict["strict_transport_security"] = strict_transport_security
        if errorfiles is not UNSET:
            field_dict["errorfiles"] = errorfiles
        if cookie_attribute_secure is not UNSET:
            field_dict["cookie_attribute_secure"] = cookie_attribute_secure
        if advanced is not UNSET:
            field_dict["advanced"] = advanced
        if advanced_backend is not UNSET:
            field_dict["advanced_backend"] = advanced_backend
        if transparent_clientip is not UNSET:
            field_dict["transparent_clientip"] = transparent_clientip
        if transparent_interface is not UNSET:
            field_dict["transparent_interface"] = transparent_interface

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ha_proxy_backend_acls_item import HAProxyBackendAclsItem
        from ..models.ha_proxy_backend_actions_item import HAProxyBackendActionsItem
        from ..models.ha_proxy_backend_errorfiles_item import HAProxyBackendErrorfilesItem
        from ..models.ha_proxy_backend_servers_item import HAProxyBackendServersItem

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _servers = d.pop("servers", UNSET)
        servers: list[HAProxyBackendServersItem] | Unset = UNSET
        if _servers is not UNSET:
            servers = []
            for servers_item_data in _servers:
                servers_item = HAProxyBackendServersItem.from_dict(servers_item_data)

                servers.append(servers_item)

        _balance = d.pop("balance", UNSET)
        balance: HAProxyBackendBalance | Unset
        if isinstance(_balance, Unset):
            balance = UNSET
        else:
            balance = HAProxyBackendBalance(_balance)

        def _parse_balance_urilen(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        balance_urilen = _parse_balance_urilen(d.pop("balance_urilen", UNSET))

        def _parse_balance_uridepth(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        balance_uridepth = _parse_balance_uridepth(d.pop("balance_uridepth", UNSET))

        balance_uriwhole = d.pop("balance_uriwhole", UNSET)

        _acls = d.pop("acls", UNSET)
        acls: list[HAProxyBackendAclsItem] | Unset = UNSET
        if _acls is not UNSET:
            acls = []
            for acls_item_data in _acls:
                acls_item = HAProxyBackendAclsItem.from_dict(acls_item_data)

                acls.append(acls_item)

        _actions = d.pop("actions", UNSET)
        actions: list[HAProxyBackendActionsItem] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = HAProxyBackendActionsItem.from_dict(actions_item_data)

                actions.append(actions_item)

        def _parse_connection_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        connection_timeout = _parse_connection_timeout(d.pop("connection_timeout", UNSET))

        def _parse_server_timeout(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        server_timeout = _parse_server_timeout(d.pop("server_timeout", UNSET))

        def _parse_retries(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retries = _parse_retries(d.pop("retries", UNSET))

        _check_type = d.pop("check_type", UNSET)
        check_type: HAProxyBackendCheckType | Unset
        if isinstance(_check_type, Unset):
            check_type = UNSET
        else:
            check_type = HAProxyBackendCheckType(_check_type)

        def _parse_checkinter(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        checkinter = _parse_checkinter(d.pop("checkinter", UNSET))

        log_health_checks = d.pop("log_health_checks", UNSET)

        _httpcheck_method = d.pop("httpcheck_method", UNSET)
        httpcheck_method: HAProxyBackendHttpcheckMethod | Unset
        if isinstance(_httpcheck_method, Unset):
            httpcheck_method = UNSET
        else:
            httpcheck_method = HAProxyBackendHttpcheckMethod(_httpcheck_method)

        monitor_uri = d.pop("monitor_uri", UNSET)

        monitor_httpversion = d.pop("monitor_httpversion", UNSET)

        monitor_username = d.pop("monitor_username", UNSET)

        monitor_domain = d.pop("monitor_domain", UNSET)

        agent_checks = d.pop("agent_checks", UNSET)

        agent_port = d.pop("agent_port", UNSET)

        def _parse_agent_inter(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agent_inter = _parse_agent_inter(d.pop("agent_inter", UNSET))

        persist_cookie_enabled = d.pop("persist_cookie_enabled", UNSET)

        persist_cookie_name = d.pop("persist_cookie_name", UNSET)

        _persist_cookie_mode = d.pop("persist_cookie_mode", UNSET)
        persist_cookie_mode: HAProxyBackendPersistCookieMode | Unset
        if isinstance(_persist_cookie_mode, Unset):
            persist_cookie_mode = UNSET
        else:
            persist_cookie_mode = HAProxyBackendPersistCookieMode(_persist_cookie_mode)

        persist_cookie_cachable = d.pop("persist_cookie_cachable", UNSET)

        persist_cookie_postonly = d.pop("persist_cookie_postonly", UNSET)

        persist_cookie_httponly = d.pop("persist_cookie_httponly", UNSET)

        persist_cookie_secure = d.pop("persist_cookie_secure", UNSET)

        def _parse_haproxy_cookie_maxidle(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        haproxy_cookie_maxidle = _parse_haproxy_cookie_maxidle(d.pop("haproxy_cookie_maxidle", UNSET))

        def _parse_haproxy_cookie_maxlife(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        haproxy_cookie_maxlife = _parse_haproxy_cookie_maxlife(d.pop("haproxy_cookie_maxlife", UNSET))

        haproxy_cookie_domains = cast(list[str], d.pop("haproxy_cookie_domains", UNSET))

        haproxy_cookie_dynamic_cookie_key = d.pop("haproxy_cookie_dynamic_cookie_key", UNSET)

        _persist_sticky_type = d.pop("persist_sticky_type", UNSET)
        persist_sticky_type: HAProxyBackendPersistStickyType | Unset
        if isinstance(_persist_sticky_type, Unset):
            persist_sticky_type = UNSET
        else:
            persist_sticky_type = HAProxyBackendPersistStickyType(_persist_sticky_type)

        persist_stick_expire = d.pop("persist_stick_expire", UNSET)

        persist_stick_tablesize = d.pop("persist_stick_tablesize", UNSET)

        persist_stick_cookiename = d.pop("persist_stick_cookiename", UNSET)

        def _parse_persist_stick_length(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        persist_stick_length = _parse_persist_stick_length(d.pop("persist_stick_length", UNSET))

        _email_level = d.pop("email_level", UNSET)
        email_level: HAProxyBackendEmailLevel | Unset
        if isinstance(_email_level, Unset):
            email_level = UNSET
        else:
            email_level = HAProxyBackendEmailLevel(_email_level)

        email_to = d.pop("email_to", UNSET)

        stats_enabled = d.pop("stats_enabled", UNSET)

        stats_uri = d.pop("stats_uri", UNSET)

        stats_scope = cast(list[str], d.pop("stats_scope", UNSET))

        stats_realm = d.pop("stats_realm", UNSET)

        stats_username = d.pop("stats_username", UNSET)

        stats_password = d.pop("stats_password", UNSET)

        stats_admin = d.pop("stats_admin", UNSET)

        stats_node = d.pop("stats_node", UNSET)

        stats_desc = d.pop("stats_desc", UNSET)

        stats_refresh = d.pop("stats_refresh", UNSET)

        def _parse_strict_transport_security(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        strict_transport_security = _parse_strict_transport_security(d.pop("strict_transport_security", UNSET))

        _errorfiles = d.pop("errorfiles", UNSET)
        errorfiles: list[HAProxyBackendErrorfilesItem] | Unset = UNSET
        if _errorfiles is not UNSET:
            errorfiles = []
            for errorfiles_item_data in _errorfiles:
                errorfiles_item = HAProxyBackendErrorfilesItem.from_dict(errorfiles_item_data)

                errorfiles.append(errorfiles_item)

        cookie_attribute_secure = d.pop("cookie_attribute_secure", UNSET)

        advanced = d.pop("advanced", UNSET)

        advanced_backend = d.pop("advanced_backend", UNSET)

        transparent_clientip = d.pop("transparent_clientip", UNSET)

        def _parse_transparent_interface(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transparent_interface = _parse_transparent_interface(d.pop("transparent_interface", UNSET))

        ha_proxy_backend = cls(
            name=name,
            servers=servers,
            balance=balance,
            balance_urilen=balance_urilen,
            balance_uridepth=balance_uridepth,
            balance_uriwhole=balance_uriwhole,
            acls=acls,
            actions=actions,
            connection_timeout=connection_timeout,
            server_timeout=server_timeout,
            retries=retries,
            check_type=check_type,
            checkinter=checkinter,
            log_health_checks=log_health_checks,
            httpcheck_method=httpcheck_method,
            monitor_uri=monitor_uri,
            monitor_httpversion=monitor_httpversion,
            monitor_username=monitor_username,
            monitor_domain=monitor_domain,
            agent_checks=agent_checks,
            agent_port=agent_port,
            agent_inter=agent_inter,
            persist_cookie_enabled=persist_cookie_enabled,
            persist_cookie_name=persist_cookie_name,
            persist_cookie_mode=persist_cookie_mode,
            persist_cookie_cachable=persist_cookie_cachable,
            persist_cookie_postonly=persist_cookie_postonly,
            persist_cookie_httponly=persist_cookie_httponly,
            persist_cookie_secure=persist_cookie_secure,
            haproxy_cookie_maxidle=haproxy_cookie_maxidle,
            haproxy_cookie_maxlife=haproxy_cookie_maxlife,
            haproxy_cookie_domains=haproxy_cookie_domains,
            haproxy_cookie_dynamic_cookie_key=haproxy_cookie_dynamic_cookie_key,
            persist_sticky_type=persist_sticky_type,
            persist_stick_expire=persist_stick_expire,
            persist_stick_tablesize=persist_stick_tablesize,
            persist_stick_cookiename=persist_stick_cookiename,
            persist_stick_length=persist_stick_length,
            email_level=email_level,
            email_to=email_to,
            stats_enabled=stats_enabled,
            stats_uri=stats_uri,
            stats_scope=stats_scope,
            stats_realm=stats_realm,
            stats_username=stats_username,
            stats_password=stats_password,
            stats_admin=stats_admin,
            stats_node=stats_node,
            stats_desc=stats_desc,
            stats_refresh=stats_refresh,
            strict_transport_security=strict_transport_security,
            errorfiles=errorfiles,
            cookie_attribute_secure=cookie_attribute_secure,
            advanced=advanced,
            advanced_backend=advanced_backend,
            transparent_clientip=transparent_clientip,
            transparent_interface=transparent_interface,
        )

        ha_proxy_backend.additional_properties = d
        return ha_proxy_backend

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
