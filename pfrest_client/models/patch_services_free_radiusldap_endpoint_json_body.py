from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.free_radiusldap_failover_mode import FreeRADIUSLDAPFailoverMode
from ..models.free_radiusldap_server_1_access_attr_used_for_allow import FreeRADIUSLDAPServer1AccessAttrUsedForAllow
from ..models.free_radiusldap_server_1_compare_check_items import FreeRADIUSLDAPServer1CompareCheckItems
from ..models.free_radiusldap_server_1_do_xlat import FreeRADIUSLDAPServer1DoXlat
from ..models.free_radiusldap_server_1_msad_compatibility_enable import FreeRADIUSLDAPServer1MsadCompatibilityEnable
from ..models.free_radiusldap_server_1_require_cert import FreeRADIUSLDAPServer1RequireCert
from ..models.free_radiusldap_server_2_access_attr_used_for_allow import FreeRADIUSLDAPServer2AccessAttrUsedForAllow
from ..models.free_radiusldap_server_2_compare_check_items import FreeRADIUSLDAPServer2CompareCheckItems
from ..models.free_radiusldap_server_2_do_xlat import FreeRADIUSLDAPServer2DoXlat
from ..models.free_radiusldap_server_2_msad_compatibility_enable import FreeRADIUSLDAPServer2MsadCompatibilityEnable
from ..models.free_radiusldap_server_2_require_cert import FreeRADIUSLDAPServer2RequireCert
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesFreeRADIUSLDAPEndpointJsonBody")


@_attrs_define
class PatchServicesFreeRADIUSLDAPEndpointJsonBody:
    """
    Attributes:
        failover_mode (FreeRADIUSLDAPFailoverMode | Unset): The failover/load-balancing mode used between the two LDAP
            servers.<br> Default: FreeRADIUSLDAPFailoverMode.REDUNDANT.
        server1_enable_authorize (bool | Unset): Enables LDAP authorization support for Server 1.<br>
        server1_enable_authenticate (bool | Unset): Enables LDAP authentication support for Server 1.<br>
        server1_server (str | Unset): The FQDN or IP address of Server 1.<br> Default: 'ldap.example.com'.
        server1_server_port (str | Unset): The TCP port used to connect to Server 1. Valid options are: a TCP/UDP port
            number<br> Default: '389'.
        server1_identity (str | Unset): The bind DN used to connect to Server 1.<br> Default: 'cn=admin,o=My Company
            Ltd,c=US'.
        server1_password (str | Unset): The password used to bind to Server 1.<br>
        server1_base_dn (str | Unset): The base DN used when searching Server 1.<br> Default: 'o=My Company Ltd,c=US'.
        server1_filter (str | Unset): The LDAP search filter used by Server 1.<br> Default: '(uid=%{%{Stripped-User-
            Name}:-%{User-Name}})'.
        server1_base_filter (str | Unset): The base LDAP filter used by Server 1.<br> Default:
            '(objectclass=radiusprofile)'.
        server1_ldap_connections_number (int | Unset): The maximum number of LDAP connections opened to Server 1.<br>
            Default: 5.
        server1_timeout (int | Unset): The bind/operation timeout (in seconds) used with Server 1.<br> Default: 4.
        server1_time_limit (int | Unset): The LDAP search time limit (in seconds) used with Server 1.<br> Default: 3.
        server1_net_timeout (int | Unset): The TCP network timeout (in seconds) used with Server 1.<br> Default: 1.
        server1_msad_compatibility_enable (FreeRADIUSLDAPServer1MsadCompatibilityEnable | Unset): Enables Microsoft
            Active Directory compatibility mode for Server 1.<br> Default:
            FreeRADIUSLDAPServer1MsadCompatibilityEnable.DISABLE.
        server1_misc_enable (bool | Unset): Enables the miscellaneous (Default Profile / Profile Attribute / Access
            Attribute) block for Server 1.<br>
        server1_default_profile (str | Unset): The default profile DN used by Server 1.<br> Default:
            'cn=radprofile,ou=dialup,o=My Company Ltd,c=US'.
        server1_profile_attribute (str | Unset): The LDAP profile attribute used by Server 1.<br> Default:
            'radiusProfileDn'.
        server1_access_attribute (str | Unset): The LDAP access attribute used by Server 1.<br> Default: 'dialupAccess'.
        server1_group_enable (bool | Unset): Enables LDAP group membership lookups for Server 1.<br>
        server1_groupname_attribute (str | Unset): The LDAP group name attribute used by Server 1.<br> Default: 'cn'.
        server1_group_membership_filter (str | Unset): The LDAP group membership filter used by Server 1.<br> Default:
            '(|(&(objectClass=GroupOfNames)(member=%{control:Ldap-
            UserDn}))(&(objectClass=GroupOfUniqueNames)(uniquemember=%{control:Ldap-UserDn})))'.
        server1_group_membership_attribute (str | Unset): The LDAP group membership attribute used by Server 1.<br>
            Default: 'radiusGroupName'.
        server1_compare_check_items (FreeRADIUSLDAPServer1CompareCheckItems | Unset): Whether Server 1 should compare
            check items.<br> Default: FreeRADIUSLDAPServer1CompareCheckItems.YES.
        server1_do_xlat (FreeRADIUSLDAPServer1DoXlat | Unset): Whether Server 1 should perform attribute translation
            (xlat).<br> Default: FreeRADIUSLDAPServer1DoXlat.YES.
        server1_access_attr_used_for_allow (FreeRADIUSLDAPServer1AccessAttrUsedForAllow | Unset): Whether the access
            attribute is used to allow (Server 1).<br> Default: FreeRADIUSLDAPServer1AccessAttrUsedForAllow.YES.
        server1_keepalive_idle (int | Unset): The TCP KeepAlive idle interval (in seconds) used with Server 1.<br>
            Default: 60.
        server1_keepalive_probes (int | Unset): The number of TCP KeepAlive probes used with Server 1.<br> Default: 3.
        server1_keepalive_interval (int | Unset): The TCP KeepAlive interval (in seconds) used with Server 1.<br>
            Default: 3.
        server1_enable_tls_support (bool | Unset): Enables TLS support when connecting to Server 1.<br>
        server1_enable_starttls (bool | Unset): Use STARTTLS when establishing a TLS-protected connection to Server
            1.<br>
        server1_ssl_ca_cert (None | str | Unset): The Certificate Authority (refid) used to verify the Server 1 server
            certificate when TLS support is enabled.<br>
        server1_ssl_server_cert (None | str | Unset): The client Certificate (refid) presented when establishing a TLS
            connection to Server 1.<br>
        server1_require_cert (FreeRADIUSLDAPServer1RequireCert | Unset): The certificate verification mode used when
            connecting to Server 1 with TLS support.<br> Default: FreeRADIUSLDAPServer1RequireCert.NEVER.
        server2_enable_authorize (bool | Unset): Enables LDAP authorization support for Server 2.<br>
        server2_enable_authenticate (bool | Unset): Enables LDAP authentication support for Server 2.<br>
        server2_server (str | Unset): The FQDN or IP address of Server 2.<br> Default: 'ldap.example.com'.
        server2_server_port (str | Unset): The TCP port used to connect to Server 2. Valid options are: a TCP/UDP port
            number<br> Default: '389'.
        server2_identity (str | Unset): The bind DN used to connect to Server 2.<br> Default: 'cn=admin,o=My Company
            Ltd,c=US'.
        server2_password (str | Unset): The password used to bind to Server 2.<br>
        server2_base_dn (str | Unset): The base DN used when searching Server 2.<br> Default: 'o=My Company Ltd,c=US'.
        server2_filter (str | Unset): The LDAP search filter used by Server 2.<br> Default: '(uid=%{%{Stripped-User-
            Name}:-%{User-Name}})'.
        server2_base_filter (str | Unset): The base LDAP filter used by Server 2.<br> Default:
            '(objectclass=radiusprofile)'.
        server2_ldap_connections_number (int | Unset): The maximum number of LDAP connections opened to Server 2.<br>
            Default: 5.
        server2_timeout (int | Unset): The bind/operation timeout (in seconds) used with Server 2.<br> Default: 4.
        server2_time_limit (int | Unset): The LDAP search time limit (in seconds) used with Server 2.<br> Default: 3.
        server2_net_timeout (int | Unset): The TCP network timeout (in seconds) used with Server 2.<br> Default: 1.
        server2_msad_compatibility_enable (FreeRADIUSLDAPServer2MsadCompatibilityEnable | Unset): Enables Microsoft
            Active Directory compatibility mode for Server 2.<br> Default:
            FreeRADIUSLDAPServer2MsadCompatibilityEnable.DISABLE.
        server2_misc_enable (bool | Unset): Enables the miscellaneous (Default Profile / Profile Attribute / Access
            Attribute) block for Server 2.<br>
        server2_default_profile (str | Unset): The default profile DN used by Server 2.<br> Default:
            'cn=radprofile,ou=dialup,o=My Company Ltd,c=US'.
        server2_profile_attribute (str | Unset): The LDAP profile attribute used by Server 2.<br> Default:
            'radiusProfileDn'.
        server2_access_attribute (str | Unset): The LDAP access attribute used by Server 2.<br> Default: 'dialupAccess'.
        server2_group_enable (bool | Unset): Enables LDAP group membership lookups for Server 2.<br>
        server2_groupname_attribute (str | Unset): The LDAP group name attribute used by Server 2.<br> Default: 'cn'.
        server2_group_membership_filter (str | Unset): The LDAP group membership filter used by Server 2.<br> Default:
            '(|(&(objectClass=GroupOfNames)(member=%{control:Ldap-
            UserDn}))(&(objectClass=GroupOfUniqueNames)(uniquemember=%{control:Ldap-UserDn})))'.
        server2_group_membership_attribute (str | Unset): The LDAP group membership attribute used by Server 2.<br>
            Default: 'radiusGroupName'.
        server2_compare_check_items (FreeRADIUSLDAPServer2CompareCheckItems | Unset): Whether Server 2 should compare
            check items.<br> Default: FreeRADIUSLDAPServer2CompareCheckItems.YES.
        server2_do_xlat (FreeRADIUSLDAPServer2DoXlat | Unset): Whether Server 2 should perform attribute translation
            (xlat).<br> Default: FreeRADIUSLDAPServer2DoXlat.YES.
        server2_access_attr_used_for_allow (FreeRADIUSLDAPServer2AccessAttrUsedForAllow | Unset): Whether the access
            attribute is used to allow (Server 2).<br> Default: FreeRADIUSLDAPServer2AccessAttrUsedForAllow.YES.
        server2_keepalive_idle (int | Unset): The TCP KeepAlive idle interval (in seconds) used with Server 2.<br>
            Default: 60.
        server2_keepalive_probes (int | Unset): The number of TCP KeepAlive probes used with Server 2.<br> Default: 3.
        server2_keepalive_interval (int | Unset): The TCP KeepAlive interval (in seconds) used with Server 2.<br>
            Default: 3.
        server2_enable_tls_support (bool | Unset): Enables TLS support when connecting to Server 2.<br>
        server2_enable_starttls (bool | Unset): Use STARTTLS when establishing a TLS-protected connection to Server
            2.<br>
        server2_ssl_ca_cert (None | str | Unset): The Certificate Authority (refid) used to verify the Server 2 server
            certificate when TLS support is enabled.<br>
        server2_ssl_server_cert (None | str | Unset): The client Certificate (refid) presented when establishing a TLS
            connection to Server 2.<br>
        server2_require_cert (FreeRADIUSLDAPServer2RequireCert | Unset): The certificate verification mode used when
            connecting to Server 2 with TLS support.<br> Default: FreeRADIUSLDAPServer2RequireCert.NEVER.
    """

    failover_mode: FreeRADIUSLDAPFailoverMode | Unset = FreeRADIUSLDAPFailoverMode.REDUNDANT
    server1_enable_authorize: bool | Unset = UNSET
    server1_enable_authenticate: bool | Unset = UNSET
    server1_server: str | Unset = "ldap.example.com"
    server1_server_port: str | Unset = "389"
    server1_identity: str | Unset = "cn=admin,o=My Company Ltd,c=US"
    server1_password: str | Unset = UNSET
    server1_base_dn: str | Unset = "o=My Company Ltd,c=US"
    server1_filter: str | Unset = "(uid=%{%{Stripped-User-Name}:-%{User-Name}})"
    server1_base_filter: str | Unset = "(objectclass=radiusprofile)"
    server1_ldap_connections_number: int | Unset = 5
    server1_timeout: int | Unset = 4
    server1_time_limit: int | Unset = 3
    server1_net_timeout: int | Unset = 1
    server1_msad_compatibility_enable: FreeRADIUSLDAPServer1MsadCompatibilityEnable | Unset = (
        FreeRADIUSLDAPServer1MsadCompatibilityEnable.DISABLE
    )
    server1_misc_enable: bool | Unset = UNSET
    server1_default_profile: str | Unset = "cn=radprofile,ou=dialup,o=My Company Ltd,c=US"
    server1_profile_attribute: str | Unset = "radiusProfileDn"
    server1_access_attribute: str | Unset = "dialupAccess"
    server1_group_enable: bool | Unset = UNSET
    server1_groupname_attribute: str | Unset = "cn"
    server1_group_membership_filter: str | Unset = (
        "(|(&(objectClass=GroupOfNames)(member=%{control:Ldap-UserDn}))(&(objectClass=GroupOfUniqueNames)(uniquemember=%{control:Ldap-UserDn})))"
    )
    server1_group_membership_attribute: str | Unset = "radiusGroupName"
    server1_compare_check_items: FreeRADIUSLDAPServer1CompareCheckItems | Unset = (
        FreeRADIUSLDAPServer1CompareCheckItems.YES
    )
    server1_do_xlat: FreeRADIUSLDAPServer1DoXlat | Unset = FreeRADIUSLDAPServer1DoXlat.YES
    server1_access_attr_used_for_allow: FreeRADIUSLDAPServer1AccessAttrUsedForAllow | Unset = (
        FreeRADIUSLDAPServer1AccessAttrUsedForAllow.YES
    )
    server1_keepalive_idle: int | Unset = 60
    server1_keepalive_probes: int | Unset = 3
    server1_keepalive_interval: int | Unset = 3
    server1_enable_tls_support: bool | Unset = UNSET
    server1_enable_starttls: bool | Unset = UNSET
    server1_ssl_ca_cert: None | str | Unset = UNSET
    server1_ssl_server_cert: None | str | Unset = UNSET
    server1_require_cert: FreeRADIUSLDAPServer1RequireCert | Unset = FreeRADIUSLDAPServer1RequireCert.NEVER
    server2_enable_authorize: bool | Unset = UNSET
    server2_enable_authenticate: bool | Unset = UNSET
    server2_server: str | Unset = "ldap.example.com"
    server2_server_port: str | Unset = "389"
    server2_identity: str | Unset = "cn=admin,o=My Company Ltd,c=US"
    server2_password: str | Unset = UNSET
    server2_base_dn: str | Unset = "o=My Company Ltd,c=US"
    server2_filter: str | Unset = "(uid=%{%{Stripped-User-Name}:-%{User-Name}})"
    server2_base_filter: str | Unset = "(objectclass=radiusprofile)"
    server2_ldap_connections_number: int | Unset = 5
    server2_timeout: int | Unset = 4
    server2_time_limit: int | Unset = 3
    server2_net_timeout: int | Unset = 1
    server2_msad_compatibility_enable: FreeRADIUSLDAPServer2MsadCompatibilityEnable | Unset = (
        FreeRADIUSLDAPServer2MsadCompatibilityEnable.DISABLE
    )
    server2_misc_enable: bool | Unset = UNSET
    server2_default_profile: str | Unset = "cn=radprofile,ou=dialup,o=My Company Ltd,c=US"
    server2_profile_attribute: str | Unset = "radiusProfileDn"
    server2_access_attribute: str | Unset = "dialupAccess"
    server2_group_enable: bool | Unset = UNSET
    server2_groupname_attribute: str | Unset = "cn"
    server2_group_membership_filter: str | Unset = (
        "(|(&(objectClass=GroupOfNames)(member=%{control:Ldap-UserDn}))(&(objectClass=GroupOfUniqueNames)(uniquemember=%{control:Ldap-UserDn})))"
    )
    server2_group_membership_attribute: str | Unset = "radiusGroupName"
    server2_compare_check_items: FreeRADIUSLDAPServer2CompareCheckItems | Unset = (
        FreeRADIUSLDAPServer2CompareCheckItems.YES
    )
    server2_do_xlat: FreeRADIUSLDAPServer2DoXlat | Unset = FreeRADIUSLDAPServer2DoXlat.YES
    server2_access_attr_used_for_allow: FreeRADIUSLDAPServer2AccessAttrUsedForAllow | Unset = (
        FreeRADIUSLDAPServer2AccessAttrUsedForAllow.YES
    )
    server2_keepalive_idle: int | Unset = 60
    server2_keepalive_probes: int | Unset = 3
    server2_keepalive_interval: int | Unset = 3
    server2_enable_tls_support: bool | Unset = UNSET
    server2_enable_starttls: bool | Unset = UNSET
    server2_ssl_ca_cert: None | str | Unset = UNSET
    server2_ssl_server_cert: None | str | Unset = UNSET
    server2_require_cert: FreeRADIUSLDAPServer2RequireCert | Unset = FreeRADIUSLDAPServer2RequireCert.NEVER
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failover_mode: str | Unset = UNSET
        if not isinstance(self.failover_mode, Unset):
            failover_mode = self.failover_mode.value

        server1_enable_authorize = self.server1_enable_authorize

        server1_enable_authenticate = self.server1_enable_authenticate

        server1_server = self.server1_server

        server1_server_port = self.server1_server_port

        server1_identity = self.server1_identity

        server1_password = self.server1_password

        server1_base_dn = self.server1_base_dn

        server1_filter = self.server1_filter

        server1_base_filter = self.server1_base_filter

        server1_ldap_connections_number = self.server1_ldap_connections_number

        server1_timeout = self.server1_timeout

        server1_time_limit = self.server1_time_limit

        server1_net_timeout = self.server1_net_timeout

        server1_msad_compatibility_enable: str | Unset = UNSET
        if not isinstance(self.server1_msad_compatibility_enable, Unset):
            server1_msad_compatibility_enable = self.server1_msad_compatibility_enable.value

        server1_misc_enable = self.server1_misc_enable

        server1_default_profile = self.server1_default_profile

        server1_profile_attribute = self.server1_profile_attribute

        server1_access_attribute = self.server1_access_attribute

        server1_group_enable = self.server1_group_enable

        server1_groupname_attribute = self.server1_groupname_attribute

        server1_group_membership_filter = self.server1_group_membership_filter

        server1_group_membership_attribute = self.server1_group_membership_attribute

        server1_compare_check_items: str | Unset = UNSET
        if not isinstance(self.server1_compare_check_items, Unset):
            server1_compare_check_items = self.server1_compare_check_items.value

        server1_do_xlat: str | Unset = UNSET
        if not isinstance(self.server1_do_xlat, Unset):
            server1_do_xlat = self.server1_do_xlat.value

        server1_access_attr_used_for_allow: str | Unset = UNSET
        if not isinstance(self.server1_access_attr_used_for_allow, Unset):
            server1_access_attr_used_for_allow = self.server1_access_attr_used_for_allow.value

        server1_keepalive_idle = self.server1_keepalive_idle

        server1_keepalive_probes = self.server1_keepalive_probes

        server1_keepalive_interval = self.server1_keepalive_interval

        server1_enable_tls_support = self.server1_enable_tls_support

        server1_enable_starttls = self.server1_enable_starttls

        server1_ssl_ca_cert: None | str | Unset
        if isinstance(self.server1_ssl_ca_cert, Unset):
            server1_ssl_ca_cert = UNSET
        else:
            server1_ssl_ca_cert = self.server1_ssl_ca_cert

        server1_ssl_server_cert: None | str | Unset
        if isinstance(self.server1_ssl_server_cert, Unset):
            server1_ssl_server_cert = UNSET
        else:
            server1_ssl_server_cert = self.server1_ssl_server_cert

        server1_require_cert: str | Unset = UNSET
        if not isinstance(self.server1_require_cert, Unset):
            server1_require_cert = self.server1_require_cert.value

        server2_enable_authorize = self.server2_enable_authorize

        server2_enable_authenticate = self.server2_enable_authenticate

        server2_server = self.server2_server

        server2_server_port = self.server2_server_port

        server2_identity = self.server2_identity

        server2_password = self.server2_password

        server2_base_dn = self.server2_base_dn

        server2_filter = self.server2_filter

        server2_base_filter = self.server2_base_filter

        server2_ldap_connections_number = self.server2_ldap_connections_number

        server2_timeout = self.server2_timeout

        server2_time_limit = self.server2_time_limit

        server2_net_timeout = self.server2_net_timeout

        server2_msad_compatibility_enable: str | Unset = UNSET
        if not isinstance(self.server2_msad_compatibility_enable, Unset):
            server2_msad_compatibility_enable = self.server2_msad_compatibility_enable.value

        server2_misc_enable = self.server2_misc_enable

        server2_default_profile = self.server2_default_profile

        server2_profile_attribute = self.server2_profile_attribute

        server2_access_attribute = self.server2_access_attribute

        server2_group_enable = self.server2_group_enable

        server2_groupname_attribute = self.server2_groupname_attribute

        server2_group_membership_filter = self.server2_group_membership_filter

        server2_group_membership_attribute = self.server2_group_membership_attribute

        server2_compare_check_items: str | Unset = UNSET
        if not isinstance(self.server2_compare_check_items, Unset):
            server2_compare_check_items = self.server2_compare_check_items.value

        server2_do_xlat: str | Unset = UNSET
        if not isinstance(self.server2_do_xlat, Unset):
            server2_do_xlat = self.server2_do_xlat.value

        server2_access_attr_used_for_allow: str | Unset = UNSET
        if not isinstance(self.server2_access_attr_used_for_allow, Unset):
            server2_access_attr_used_for_allow = self.server2_access_attr_used_for_allow.value

        server2_keepalive_idle = self.server2_keepalive_idle

        server2_keepalive_probes = self.server2_keepalive_probes

        server2_keepalive_interval = self.server2_keepalive_interval

        server2_enable_tls_support = self.server2_enable_tls_support

        server2_enable_starttls = self.server2_enable_starttls

        server2_ssl_ca_cert: None | str | Unset
        if isinstance(self.server2_ssl_ca_cert, Unset):
            server2_ssl_ca_cert = UNSET
        else:
            server2_ssl_ca_cert = self.server2_ssl_ca_cert

        server2_ssl_server_cert: None | str | Unset
        if isinstance(self.server2_ssl_server_cert, Unset):
            server2_ssl_server_cert = UNSET
        else:
            server2_ssl_server_cert = self.server2_ssl_server_cert

        server2_require_cert: str | Unset = UNSET
        if not isinstance(self.server2_require_cert, Unset):
            server2_require_cert = self.server2_require_cert.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failover_mode is not UNSET:
            field_dict["failover_mode"] = failover_mode
        if server1_enable_authorize is not UNSET:
            field_dict["server1_enable_authorize"] = server1_enable_authorize
        if server1_enable_authenticate is not UNSET:
            field_dict["server1_enable_authenticate"] = server1_enable_authenticate
        if server1_server is not UNSET:
            field_dict["server1_server"] = server1_server
        if server1_server_port is not UNSET:
            field_dict["server1_server_port"] = server1_server_port
        if server1_identity is not UNSET:
            field_dict["server1_identity"] = server1_identity
        if server1_password is not UNSET:
            field_dict["server1_password"] = server1_password
        if server1_base_dn is not UNSET:
            field_dict["server1_base_dn"] = server1_base_dn
        if server1_filter is not UNSET:
            field_dict["server1_filter"] = server1_filter
        if server1_base_filter is not UNSET:
            field_dict["server1_base_filter"] = server1_base_filter
        if server1_ldap_connections_number is not UNSET:
            field_dict["server1_ldap_connections_number"] = server1_ldap_connections_number
        if server1_timeout is not UNSET:
            field_dict["server1_timeout"] = server1_timeout
        if server1_time_limit is not UNSET:
            field_dict["server1_time_limit"] = server1_time_limit
        if server1_net_timeout is not UNSET:
            field_dict["server1_net_timeout"] = server1_net_timeout
        if server1_msad_compatibility_enable is not UNSET:
            field_dict["server1_msad_compatibility_enable"] = server1_msad_compatibility_enable
        if server1_misc_enable is not UNSET:
            field_dict["server1_misc_enable"] = server1_misc_enable
        if server1_default_profile is not UNSET:
            field_dict["server1_default_profile"] = server1_default_profile
        if server1_profile_attribute is not UNSET:
            field_dict["server1_profile_attribute"] = server1_profile_attribute
        if server1_access_attribute is not UNSET:
            field_dict["server1_access_attribute"] = server1_access_attribute
        if server1_group_enable is not UNSET:
            field_dict["server1_group_enable"] = server1_group_enable
        if server1_groupname_attribute is not UNSET:
            field_dict["server1_groupname_attribute"] = server1_groupname_attribute
        if server1_group_membership_filter is not UNSET:
            field_dict["server1_group_membership_filter"] = server1_group_membership_filter
        if server1_group_membership_attribute is not UNSET:
            field_dict["server1_group_membership_attribute"] = server1_group_membership_attribute
        if server1_compare_check_items is not UNSET:
            field_dict["server1_compare_check_items"] = server1_compare_check_items
        if server1_do_xlat is not UNSET:
            field_dict["server1_do_xlat"] = server1_do_xlat
        if server1_access_attr_used_for_allow is not UNSET:
            field_dict["server1_access_attr_used_for_allow"] = server1_access_attr_used_for_allow
        if server1_keepalive_idle is not UNSET:
            field_dict["server1_keepalive_idle"] = server1_keepalive_idle
        if server1_keepalive_probes is not UNSET:
            field_dict["server1_keepalive_probes"] = server1_keepalive_probes
        if server1_keepalive_interval is not UNSET:
            field_dict["server1_keepalive_interval"] = server1_keepalive_interval
        if server1_enable_tls_support is not UNSET:
            field_dict["server1_enable_tls_support"] = server1_enable_tls_support
        if server1_enable_starttls is not UNSET:
            field_dict["server1_enable_starttls"] = server1_enable_starttls
        if server1_ssl_ca_cert is not UNSET:
            field_dict["server1_ssl_ca_cert"] = server1_ssl_ca_cert
        if server1_ssl_server_cert is not UNSET:
            field_dict["server1_ssl_server_cert"] = server1_ssl_server_cert
        if server1_require_cert is not UNSET:
            field_dict["server1_require_cert"] = server1_require_cert
        if server2_enable_authorize is not UNSET:
            field_dict["server2_enable_authorize"] = server2_enable_authorize
        if server2_enable_authenticate is not UNSET:
            field_dict["server2_enable_authenticate"] = server2_enable_authenticate
        if server2_server is not UNSET:
            field_dict["server2_server"] = server2_server
        if server2_server_port is not UNSET:
            field_dict["server2_server_port"] = server2_server_port
        if server2_identity is not UNSET:
            field_dict["server2_identity"] = server2_identity
        if server2_password is not UNSET:
            field_dict["server2_password"] = server2_password
        if server2_base_dn is not UNSET:
            field_dict["server2_base_dn"] = server2_base_dn
        if server2_filter is not UNSET:
            field_dict["server2_filter"] = server2_filter
        if server2_base_filter is not UNSET:
            field_dict["server2_base_filter"] = server2_base_filter
        if server2_ldap_connections_number is not UNSET:
            field_dict["server2_ldap_connections_number"] = server2_ldap_connections_number
        if server2_timeout is not UNSET:
            field_dict["server2_timeout"] = server2_timeout
        if server2_time_limit is not UNSET:
            field_dict["server2_time_limit"] = server2_time_limit
        if server2_net_timeout is not UNSET:
            field_dict["server2_net_timeout"] = server2_net_timeout
        if server2_msad_compatibility_enable is not UNSET:
            field_dict["server2_msad_compatibility_enable"] = server2_msad_compatibility_enable
        if server2_misc_enable is not UNSET:
            field_dict["server2_misc_enable"] = server2_misc_enable
        if server2_default_profile is not UNSET:
            field_dict["server2_default_profile"] = server2_default_profile
        if server2_profile_attribute is not UNSET:
            field_dict["server2_profile_attribute"] = server2_profile_attribute
        if server2_access_attribute is not UNSET:
            field_dict["server2_access_attribute"] = server2_access_attribute
        if server2_group_enable is not UNSET:
            field_dict["server2_group_enable"] = server2_group_enable
        if server2_groupname_attribute is not UNSET:
            field_dict["server2_groupname_attribute"] = server2_groupname_attribute
        if server2_group_membership_filter is not UNSET:
            field_dict["server2_group_membership_filter"] = server2_group_membership_filter
        if server2_group_membership_attribute is not UNSET:
            field_dict["server2_group_membership_attribute"] = server2_group_membership_attribute
        if server2_compare_check_items is not UNSET:
            field_dict["server2_compare_check_items"] = server2_compare_check_items
        if server2_do_xlat is not UNSET:
            field_dict["server2_do_xlat"] = server2_do_xlat
        if server2_access_attr_used_for_allow is not UNSET:
            field_dict["server2_access_attr_used_for_allow"] = server2_access_attr_used_for_allow
        if server2_keepalive_idle is not UNSET:
            field_dict["server2_keepalive_idle"] = server2_keepalive_idle
        if server2_keepalive_probes is not UNSET:
            field_dict["server2_keepalive_probes"] = server2_keepalive_probes
        if server2_keepalive_interval is not UNSET:
            field_dict["server2_keepalive_interval"] = server2_keepalive_interval
        if server2_enable_tls_support is not UNSET:
            field_dict["server2_enable_tls_support"] = server2_enable_tls_support
        if server2_enable_starttls is not UNSET:
            field_dict["server2_enable_starttls"] = server2_enable_starttls
        if server2_ssl_ca_cert is not UNSET:
            field_dict["server2_ssl_ca_cert"] = server2_ssl_ca_cert
        if server2_ssl_server_cert is not UNSET:
            field_dict["server2_ssl_server_cert"] = server2_ssl_server_cert
        if server2_require_cert is not UNSET:
            field_dict["server2_require_cert"] = server2_require_cert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _failover_mode = d.pop("failover_mode", UNSET)
        failover_mode: FreeRADIUSLDAPFailoverMode | Unset
        if isinstance(_failover_mode, Unset):
            failover_mode = UNSET
        else:
            failover_mode = FreeRADIUSLDAPFailoverMode(_failover_mode)

        server1_enable_authorize = d.pop("server1_enable_authorize", UNSET)

        server1_enable_authenticate = d.pop("server1_enable_authenticate", UNSET)

        server1_server = d.pop("server1_server", UNSET)

        server1_server_port = d.pop("server1_server_port", UNSET)

        server1_identity = d.pop("server1_identity", UNSET)

        server1_password = d.pop("server1_password", UNSET)

        server1_base_dn = d.pop("server1_base_dn", UNSET)

        server1_filter = d.pop("server1_filter", UNSET)

        server1_base_filter = d.pop("server1_base_filter", UNSET)

        server1_ldap_connections_number = d.pop("server1_ldap_connections_number", UNSET)

        server1_timeout = d.pop("server1_timeout", UNSET)

        server1_time_limit = d.pop("server1_time_limit", UNSET)

        server1_net_timeout = d.pop("server1_net_timeout", UNSET)

        _server1_msad_compatibility_enable = d.pop("server1_msad_compatibility_enable", UNSET)
        server1_msad_compatibility_enable: FreeRADIUSLDAPServer1MsadCompatibilityEnable | Unset
        if isinstance(_server1_msad_compatibility_enable, Unset):
            server1_msad_compatibility_enable = UNSET
        else:
            server1_msad_compatibility_enable = FreeRADIUSLDAPServer1MsadCompatibilityEnable(
                _server1_msad_compatibility_enable
            )

        server1_misc_enable = d.pop("server1_misc_enable", UNSET)

        server1_default_profile = d.pop("server1_default_profile", UNSET)

        server1_profile_attribute = d.pop("server1_profile_attribute", UNSET)

        server1_access_attribute = d.pop("server1_access_attribute", UNSET)

        server1_group_enable = d.pop("server1_group_enable", UNSET)

        server1_groupname_attribute = d.pop("server1_groupname_attribute", UNSET)

        server1_group_membership_filter = d.pop("server1_group_membership_filter", UNSET)

        server1_group_membership_attribute = d.pop("server1_group_membership_attribute", UNSET)

        _server1_compare_check_items = d.pop("server1_compare_check_items", UNSET)
        server1_compare_check_items: FreeRADIUSLDAPServer1CompareCheckItems | Unset
        if isinstance(_server1_compare_check_items, Unset):
            server1_compare_check_items = UNSET
        else:
            server1_compare_check_items = FreeRADIUSLDAPServer1CompareCheckItems(_server1_compare_check_items)

        _server1_do_xlat = d.pop("server1_do_xlat", UNSET)
        server1_do_xlat: FreeRADIUSLDAPServer1DoXlat | Unset
        if isinstance(_server1_do_xlat, Unset):
            server1_do_xlat = UNSET
        else:
            server1_do_xlat = FreeRADIUSLDAPServer1DoXlat(_server1_do_xlat)

        _server1_access_attr_used_for_allow = d.pop("server1_access_attr_used_for_allow", UNSET)
        server1_access_attr_used_for_allow: FreeRADIUSLDAPServer1AccessAttrUsedForAllow | Unset
        if isinstance(_server1_access_attr_used_for_allow, Unset):
            server1_access_attr_used_for_allow = UNSET
        else:
            server1_access_attr_used_for_allow = FreeRADIUSLDAPServer1AccessAttrUsedForAllow(
                _server1_access_attr_used_for_allow
            )

        server1_keepalive_idle = d.pop("server1_keepalive_idle", UNSET)

        server1_keepalive_probes = d.pop("server1_keepalive_probes", UNSET)

        server1_keepalive_interval = d.pop("server1_keepalive_interval", UNSET)

        server1_enable_tls_support = d.pop("server1_enable_tls_support", UNSET)

        server1_enable_starttls = d.pop("server1_enable_starttls", UNSET)

        def _parse_server1_ssl_ca_cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server1_ssl_ca_cert = _parse_server1_ssl_ca_cert(d.pop("server1_ssl_ca_cert", UNSET))

        def _parse_server1_ssl_server_cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server1_ssl_server_cert = _parse_server1_ssl_server_cert(d.pop("server1_ssl_server_cert", UNSET))

        _server1_require_cert = d.pop("server1_require_cert", UNSET)
        server1_require_cert: FreeRADIUSLDAPServer1RequireCert | Unset
        if isinstance(_server1_require_cert, Unset):
            server1_require_cert = UNSET
        else:
            server1_require_cert = FreeRADIUSLDAPServer1RequireCert(_server1_require_cert)

        server2_enable_authorize = d.pop("server2_enable_authorize", UNSET)

        server2_enable_authenticate = d.pop("server2_enable_authenticate", UNSET)

        server2_server = d.pop("server2_server", UNSET)

        server2_server_port = d.pop("server2_server_port", UNSET)

        server2_identity = d.pop("server2_identity", UNSET)

        server2_password = d.pop("server2_password", UNSET)

        server2_base_dn = d.pop("server2_base_dn", UNSET)

        server2_filter = d.pop("server2_filter", UNSET)

        server2_base_filter = d.pop("server2_base_filter", UNSET)

        server2_ldap_connections_number = d.pop("server2_ldap_connections_number", UNSET)

        server2_timeout = d.pop("server2_timeout", UNSET)

        server2_time_limit = d.pop("server2_time_limit", UNSET)

        server2_net_timeout = d.pop("server2_net_timeout", UNSET)

        _server2_msad_compatibility_enable = d.pop("server2_msad_compatibility_enable", UNSET)
        server2_msad_compatibility_enable: FreeRADIUSLDAPServer2MsadCompatibilityEnable | Unset
        if isinstance(_server2_msad_compatibility_enable, Unset):
            server2_msad_compatibility_enable = UNSET
        else:
            server2_msad_compatibility_enable = FreeRADIUSLDAPServer2MsadCompatibilityEnable(
                _server2_msad_compatibility_enable
            )

        server2_misc_enable = d.pop("server2_misc_enable", UNSET)

        server2_default_profile = d.pop("server2_default_profile", UNSET)

        server2_profile_attribute = d.pop("server2_profile_attribute", UNSET)

        server2_access_attribute = d.pop("server2_access_attribute", UNSET)

        server2_group_enable = d.pop("server2_group_enable", UNSET)

        server2_groupname_attribute = d.pop("server2_groupname_attribute", UNSET)

        server2_group_membership_filter = d.pop("server2_group_membership_filter", UNSET)

        server2_group_membership_attribute = d.pop("server2_group_membership_attribute", UNSET)

        _server2_compare_check_items = d.pop("server2_compare_check_items", UNSET)
        server2_compare_check_items: FreeRADIUSLDAPServer2CompareCheckItems | Unset
        if isinstance(_server2_compare_check_items, Unset):
            server2_compare_check_items = UNSET
        else:
            server2_compare_check_items = FreeRADIUSLDAPServer2CompareCheckItems(_server2_compare_check_items)

        _server2_do_xlat = d.pop("server2_do_xlat", UNSET)
        server2_do_xlat: FreeRADIUSLDAPServer2DoXlat | Unset
        if isinstance(_server2_do_xlat, Unset):
            server2_do_xlat = UNSET
        else:
            server2_do_xlat = FreeRADIUSLDAPServer2DoXlat(_server2_do_xlat)

        _server2_access_attr_used_for_allow = d.pop("server2_access_attr_used_for_allow", UNSET)
        server2_access_attr_used_for_allow: FreeRADIUSLDAPServer2AccessAttrUsedForAllow | Unset
        if isinstance(_server2_access_attr_used_for_allow, Unset):
            server2_access_attr_used_for_allow = UNSET
        else:
            server2_access_attr_used_for_allow = FreeRADIUSLDAPServer2AccessAttrUsedForAllow(
                _server2_access_attr_used_for_allow
            )

        server2_keepalive_idle = d.pop("server2_keepalive_idle", UNSET)

        server2_keepalive_probes = d.pop("server2_keepalive_probes", UNSET)

        server2_keepalive_interval = d.pop("server2_keepalive_interval", UNSET)

        server2_enable_tls_support = d.pop("server2_enable_tls_support", UNSET)

        server2_enable_starttls = d.pop("server2_enable_starttls", UNSET)

        def _parse_server2_ssl_ca_cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server2_ssl_ca_cert = _parse_server2_ssl_ca_cert(d.pop("server2_ssl_ca_cert", UNSET))

        def _parse_server2_ssl_server_cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server2_ssl_server_cert = _parse_server2_ssl_server_cert(d.pop("server2_ssl_server_cert", UNSET))

        _server2_require_cert = d.pop("server2_require_cert", UNSET)
        server2_require_cert: FreeRADIUSLDAPServer2RequireCert | Unset
        if isinstance(_server2_require_cert, Unset):
            server2_require_cert = UNSET
        else:
            server2_require_cert = FreeRADIUSLDAPServer2RequireCert(_server2_require_cert)

        patch_services_free_radiusldap_endpoint_json_body = cls(
            failover_mode=failover_mode,
            server1_enable_authorize=server1_enable_authorize,
            server1_enable_authenticate=server1_enable_authenticate,
            server1_server=server1_server,
            server1_server_port=server1_server_port,
            server1_identity=server1_identity,
            server1_password=server1_password,
            server1_base_dn=server1_base_dn,
            server1_filter=server1_filter,
            server1_base_filter=server1_base_filter,
            server1_ldap_connections_number=server1_ldap_connections_number,
            server1_timeout=server1_timeout,
            server1_time_limit=server1_time_limit,
            server1_net_timeout=server1_net_timeout,
            server1_msad_compatibility_enable=server1_msad_compatibility_enable,
            server1_misc_enable=server1_misc_enable,
            server1_default_profile=server1_default_profile,
            server1_profile_attribute=server1_profile_attribute,
            server1_access_attribute=server1_access_attribute,
            server1_group_enable=server1_group_enable,
            server1_groupname_attribute=server1_groupname_attribute,
            server1_group_membership_filter=server1_group_membership_filter,
            server1_group_membership_attribute=server1_group_membership_attribute,
            server1_compare_check_items=server1_compare_check_items,
            server1_do_xlat=server1_do_xlat,
            server1_access_attr_used_for_allow=server1_access_attr_used_for_allow,
            server1_keepalive_idle=server1_keepalive_idle,
            server1_keepalive_probes=server1_keepalive_probes,
            server1_keepalive_interval=server1_keepalive_interval,
            server1_enable_tls_support=server1_enable_tls_support,
            server1_enable_starttls=server1_enable_starttls,
            server1_ssl_ca_cert=server1_ssl_ca_cert,
            server1_ssl_server_cert=server1_ssl_server_cert,
            server1_require_cert=server1_require_cert,
            server2_enable_authorize=server2_enable_authorize,
            server2_enable_authenticate=server2_enable_authenticate,
            server2_server=server2_server,
            server2_server_port=server2_server_port,
            server2_identity=server2_identity,
            server2_password=server2_password,
            server2_base_dn=server2_base_dn,
            server2_filter=server2_filter,
            server2_base_filter=server2_base_filter,
            server2_ldap_connections_number=server2_ldap_connections_number,
            server2_timeout=server2_timeout,
            server2_time_limit=server2_time_limit,
            server2_net_timeout=server2_net_timeout,
            server2_msad_compatibility_enable=server2_msad_compatibility_enable,
            server2_misc_enable=server2_misc_enable,
            server2_default_profile=server2_default_profile,
            server2_profile_attribute=server2_profile_attribute,
            server2_access_attribute=server2_access_attribute,
            server2_group_enable=server2_group_enable,
            server2_groupname_attribute=server2_groupname_attribute,
            server2_group_membership_filter=server2_group_membership_filter,
            server2_group_membership_attribute=server2_group_membership_attribute,
            server2_compare_check_items=server2_compare_check_items,
            server2_do_xlat=server2_do_xlat,
            server2_access_attr_used_for_allow=server2_access_attr_used_for_allow,
            server2_keepalive_idle=server2_keepalive_idle,
            server2_keepalive_probes=server2_keepalive_probes,
            server2_keepalive_interval=server2_keepalive_interval,
            server2_enable_tls_support=server2_enable_tls_support,
            server2_enable_starttls=server2_enable_starttls,
            server2_ssl_ca_cert=server2_ssl_ca_cert,
            server2_ssl_server_cert=server2_ssl_server_cert,
            server2_require_cert=server2_require_cert,
        )

        patch_services_free_radiusldap_endpoint_json_body.additional_properties = d
        return patch_services_free_radiusldap_endpoint_json_body

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
