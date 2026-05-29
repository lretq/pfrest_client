from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_server_ldap_protver import AuthServerLdapProtver
from ..models.auth_server_ldap_scope import AuthServerLdapScope
from ..models.auth_server_ldap_urltype import AuthServerLdapUrltype
from ..models.auth_server_radius_protocol import AuthServerRadiusProtocol
from ..models.auth_server_type import AuthServerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutUserAuthServersEndpointDataBodyItem")


@_attrs_define
class PutUserAuthServersEndpointDataBodyItem:
    """
    Attributes:
        type_ (AuthServerType): The type of this authentication server.<br>
        name (str): The descriptive name for this authentication server.<br>
        host (str): The remote IP address or hostname of the authentication server.<br>
        ldap_port (str): The LDAP port to connect to on this LDAP authentication server. Valid options are: a TCP/UDP
            port number<br><br>This field is only available when the following conditions are met:<br>- `type` must be equal
            to `'ldap'`<br>
        ldap_urltype (AuthServerLdapUrltype): The encryption mode to use when connecting to this authentication server.
            Use `Standard TCP` for unencrypted LDAP connections, use `STARTTLS Encrypt` to start an encrypted connection via
            STARTTLS if it's available, or `SSL/TLS Encrypted` to only use LDAPS encrypted connections.<br><br>This field is
            only available when the following conditions are met:<br>- `type` must be equal to `'ldap'`<br>
        ldap_scope (AuthServerLdapScope): The LDAP search scope. Use `one` to limit the scope to a single level, or
            `subtree` to allow the entire subtree to be searched.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be equal to `'ldap'`<br>
        ldap_bindpw (str): The password to use when binding to this authentication server.<br><br>This field is only
            available when the following conditions are met:<br>- `type` must be equal to `'ldap'`<br>- `ldap_binddn` must
            not be equal to `NULL`<br>
        radius_secret (str): The shared secret to use when authenticating to this RADIUS server.<br><br>This field is
            only available when the following conditions are met:<br>- `type` must be equal to `'radius'`<br>
        radius_nasip_attribute (str): The interface whose IP will be used as the 'NAS-IP-Address' attribute during
            RADIUS Access-Requests. This choice will not change the interface used for contacting the RADIUS
            server.<br><br>This field is only available when the following conditions are met:<br>- `type` must be equal to
            `'radius'`<br>
        refid (None | str | Unset): The unique reference ID for this authentication server. This value is only used
            internally and cannot be manually set or changed.<br>
        ldap_protver (AuthServerLdapProtver | Unset): The LDAP protocol version to use for connections to this LDAP
            authentication server.<br><br>This field is only available when the following conditions are met:<br>- `type`
            must be equal to `'ldap'`<br> Default: AuthServerLdapProtver.VALUE_3.
        ldap_timeout (int | Unset): The timeout (in seconds) for connections to the LDAP authentication
            server.<br><br>This field is only available when the following conditions are met:<br>- `type` must be equal to
            `'ldap'`<br> Default: 25.
        ldap_caref (str | Unset): The certificate authority used to validate the LDAP server certificate.<br><br>This
            field is only available when the following conditions are met:<br>- `ldap_urltype` must be one of [ starttls,
            encrypted ]<br> Default: 'global'.
        ldap_basedn (str | Unset): The root for LDAP searches on this authentication server.<br><br>This field is only
            available when the following conditions are met:<br>- `type` must be equal to `'ldap'`<br>
        ldap_authcn (str | Unset): The LDAP authentication container.<br><br>This field is only available when the
            following conditions are met:<br>- `type` must be equal to `'ldap'`<br>
        ldap_extended_enabled (bool | Unset): Enable LDAP extended queries.<br><br>This field is only available when the
            following conditions are met:<br>- `type` must be equal to `'ldap'`<br>
        ldap_extended_query (str | Unset): The extended LDAP query to make during LDAP searches.<br><br>This field is
            only available when the following conditions are met:<br>- `type` must be equal to `'ldap'`<br>-
            `ldap_extended_enabled` must be equal to `true`<br>
        ldap_binddn (None | str | Unset): The DN to use when binding to this authentication server. Set to `null` to
            bind anonymously.<br><br>This field is only available when the following conditions are met:<br>- `type` must be
            equal to `'ldap'`<br>
        ldap_attr_user (str | Unset): The LDAP user attribute.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be equal to `'ldap'`<br> Default: 'cn'.
        ldap_attr_group (str | Unset): The LDAP group attribute.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be equal to `'ldap'`<br> Default: 'cn'.
        ldap_attr_member (str | Unset): The LDAP member attribute.<br><br>This field is only available when the
            following conditions are met:<br>- `type` must be equal to `'ldap'`<br> Default: 'member'.
        ldap_rfc2307 (bool | Unset): Enables or disable RFC2307 LDAP options.<br><br>This field is only available when
            the following conditions are met:<br>- `type` must be equal to `'ldap'`<br>
        ldap_rfc2307_userdn (bool | Unset): Enables or disable the use of DNs for username searches.<br><br>This field
            is only available when the following conditions are met:<br>- `type` must be equal to `'ldap'`<br>-
            `ldap_rfc2307` must be equal to `true`<br>
        ldap_attr_groupobj (str | Unset): The group object class for groups in RFC2307 mode.<br><br>This field is only
            available when the following conditions are met:<br>- `type` must be equal to `'ldap'`<br>- `ldap_rfc2307` must
            be equal to `true`<br> Default: 'posixGroup'.
        ldap_pam_groupdn (str | Unset): The group DN to use for shell authentication. Users must be a member of this
            group and have valid posixAccount attributes to sign in.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be equal to `'ldap'`<br>
        ldap_utf8 (bool | Unset): Enables or disables UTF-8 encoding LDAP parameters before sending them to this
            authentication server<br><br>This field is only available when the following conditions are met:<br>- `type`
            must be equal to `'ldap'`<br>
        ldap_nostrip_at (bool | Unset): Do not strip away parts of the username after the @ symbol.<br><br>This field is
            only available when the following conditions are met:<br>- `type` must be equal to `'ldap'`<br>
        ldap_allow_unauthenticated (bool | Unset): Enables or disables unauthenticated binding. Unauthenticated binds
            are bind with an existing login but with an empty password. Some LDAP servers (Microsoft AD) allow this type of
            bind without any possibility to disable it.<br><br>This field is only available when the following conditions
            are met:<br>- `type` must be equal to `'ldap'`<br> Default: True.
        radius_auth_port (None | str | Unset): The port used by RADIUS for authentication. Set to `null` to disable use
            of authentication services. Valid options are: a TCP/UDP port number<br><br>This field is only available when
            the following conditions are met:<br>- `type` must be equal to `'radius'`<br> Default: '1812'.
        radius_acct_port (None | str | Unset): The port used by RADIUS for accounting. Set to `null` to disable use of
            accounting services. Valid options are: a TCP/UDP port number<br><br>This field is only available when the
            following conditions are met:<br>- `type` must be equal to `'radius'`<br> Default: '1813'.
        radius_protocol (AuthServerRadiusProtocol | Unset): The RADIUS protocol to use when authenticating.<br><br>This
            field is only available when the following conditions are met:<br>- `type` must be equal to `'radius'`<br>
            Default: AuthServerRadiusProtocol.MSCHAPV2.
        radius_timeout (int | Unset): The timeout (in seconds) for connections to this RADIUS authentication
            server.<br><br>This field is only available when the following conditions are met:<br>- `type` must be equal to
            `'radius'`<br> Default: 5.
    """

    type_: AuthServerType
    name: str
    host: str
    ldap_port: str
    ldap_urltype: AuthServerLdapUrltype
    ldap_scope: AuthServerLdapScope
    ldap_bindpw: str
    radius_secret: str
    radius_nasip_attribute: str
    refid: None | str | Unset = UNSET
    ldap_protver: AuthServerLdapProtver | Unset = AuthServerLdapProtver.VALUE_3
    ldap_timeout: int | Unset = 25
    ldap_caref: str | Unset = "global"
    ldap_basedn: str | Unset = UNSET
    ldap_authcn: str | Unset = UNSET
    ldap_extended_enabled: bool | Unset = UNSET
    ldap_extended_query: str | Unset = UNSET
    ldap_binddn: None | str | Unset = UNSET
    ldap_attr_user: str | Unset = "cn"
    ldap_attr_group: str | Unset = "cn"
    ldap_attr_member: str | Unset = "member"
    ldap_rfc2307: bool | Unset = UNSET
    ldap_rfc2307_userdn: bool | Unset = UNSET
    ldap_attr_groupobj: str | Unset = "posixGroup"
    ldap_pam_groupdn: str | Unset = UNSET
    ldap_utf8: bool | Unset = UNSET
    ldap_nostrip_at: bool | Unset = UNSET
    ldap_allow_unauthenticated: bool | Unset = True
    radius_auth_port: None | str | Unset = "1812"
    radius_acct_port: None | str | Unset = "1813"
    radius_protocol: AuthServerRadiusProtocol | Unset = AuthServerRadiusProtocol.MSCHAPV2
    radius_timeout: int | Unset = 5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        name = self.name

        host = self.host

        ldap_port = self.ldap_port

        ldap_urltype = self.ldap_urltype.value

        ldap_scope = self.ldap_scope.value

        ldap_bindpw = self.ldap_bindpw

        radius_secret = self.radius_secret

        radius_nasip_attribute = self.radius_nasip_attribute

        refid: None | str | Unset
        if isinstance(self.refid, Unset):
            refid = UNSET
        else:
            refid = self.refid

        ldap_protver: int | Unset = UNSET
        if not isinstance(self.ldap_protver, Unset):
            ldap_protver = self.ldap_protver.value

        ldap_timeout = self.ldap_timeout

        ldap_caref = self.ldap_caref

        ldap_basedn = self.ldap_basedn

        ldap_authcn = self.ldap_authcn

        ldap_extended_enabled = self.ldap_extended_enabled

        ldap_extended_query = self.ldap_extended_query

        ldap_binddn: None | str | Unset
        if isinstance(self.ldap_binddn, Unset):
            ldap_binddn = UNSET
        else:
            ldap_binddn = self.ldap_binddn

        ldap_attr_user = self.ldap_attr_user

        ldap_attr_group = self.ldap_attr_group

        ldap_attr_member = self.ldap_attr_member

        ldap_rfc2307 = self.ldap_rfc2307

        ldap_rfc2307_userdn = self.ldap_rfc2307_userdn

        ldap_attr_groupobj = self.ldap_attr_groupobj

        ldap_pam_groupdn = self.ldap_pam_groupdn

        ldap_utf8 = self.ldap_utf8

        ldap_nostrip_at = self.ldap_nostrip_at

        ldap_allow_unauthenticated = self.ldap_allow_unauthenticated

        radius_auth_port: None | str | Unset
        if isinstance(self.radius_auth_port, Unset):
            radius_auth_port = UNSET
        else:
            radius_auth_port = self.radius_auth_port

        radius_acct_port: None | str | Unset
        if isinstance(self.radius_acct_port, Unset):
            radius_acct_port = UNSET
        else:
            radius_acct_port = self.radius_acct_port

        radius_protocol: str | Unset = UNSET
        if not isinstance(self.radius_protocol, Unset):
            radius_protocol = self.radius_protocol.value

        radius_timeout = self.radius_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "host": host,
                "ldap_port": ldap_port,
                "ldap_urltype": ldap_urltype,
                "ldap_scope": ldap_scope,
                "ldap_bindpw": ldap_bindpw,
                "radius_secret": radius_secret,
                "radius_nasip_attribute": radius_nasip_attribute,
            }
        )
        if refid is not UNSET:
            field_dict["refid"] = refid
        if ldap_protver is not UNSET:
            field_dict["ldap_protver"] = ldap_protver
        if ldap_timeout is not UNSET:
            field_dict["ldap_timeout"] = ldap_timeout
        if ldap_caref is not UNSET:
            field_dict["ldap_caref"] = ldap_caref
        if ldap_basedn is not UNSET:
            field_dict["ldap_basedn"] = ldap_basedn
        if ldap_authcn is not UNSET:
            field_dict["ldap_authcn"] = ldap_authcn
        if ldap_extended_enabled is not UNSET:
            field_dict["ldap_extended_enabled"] = ldap_extended_enabled
        if ldap_extended_query is not UNSET:
            field_dict["ldap_extended_query"] = ldap_extended_query
        if ldap_binddn is not UNSET:
            field_dict["ldap_binddn"] = ldap_binddn
        if ldap_attr_user is not UNSET:
            field_dict["ldap_attr_user"] = ldap_attr_user
        if ldap_attr_group is not UNSET:
            field_dict["ldap_attr_group"] = ldap_attr_group
        if ldap_attr_member is not UNSET:
            field_dict["ldap_attr_member"] = ldap_attr_member
        if ldap_rfc2307 is not UNSET:
            field_dict["ldap_rfc2307"] = ldap_rfc2307
        if ldap_rfc2307_userdn is not UNSET:
            field_dict["ldap_rfc2307_userdn"] = ldap_rfc2307_userdn
        if ldap_attr_groupobj is not UNSET:
            field_dict["ldap_attr_groupobj"] = ldap_attr_groupobj
        if ldap_pam_groupdn is not UNSET:
            field_dict["ldap_pam_groupdn"] = ldap_pam_groupdn
        if ldap_utf8 is not UNSET:
            field_dict["ldap_utf8"] = ldap_utf8
        if ldap_nostrip_at is not UNSET:
            field_dict["ldap_nostrip_at"] = ldap_nostrip_at
        if ldap_allow_unauthenticated is not UNSET:
            field_dict["ldap_allow_unauthenticated"] = ldap_allow_unauthenticated
        if radius_auth_port is not UNSET:
            field_dict["radius_auth_port"] = radius_auth_port
        if radius_acct_port is not UNSET:
            field_dict["radius_acct_port"] = radius_acct_port
        if radius_protocol is not UNSET:
            field_dict["radius_protocol"] = radius_protocol
        if radius_timeout is not UNSET:
            field_dict["radius_timeout"] = radius_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = AuthServerType(d.pop("type"))

        name = d.pop("name")

        host = d.pop("host")

        ldap_port = d.pop("ldap_port")

        ldap_urltype = AuthServerLdapUrltype(d.pop("ldap_urltype"))

        ldap_scope = AuthServerLdapScope(d.pop("ldap_scope"))

        ldap_bindpw = d.pop("ldap_bindpw")

        radius_secret = d.pop("radius_secret")

        radius_nasip_attribute = d.pop("radius_nasip_attribute")

        def _parse_refid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refid = _parse_refid(d.pop("refid", UNSET))

        _ldap_protver = d.pop("ldap_protver", UNSET)
        ldap_protver: AuthServerLdapProtver | Unset
        if isinstance(_ldap_protver, Unset):
            ldap_protver = UNSET
        else:
            ldap_protver = AuthServerLdapProtver(_ldap_protver)

        ldap_timeout = d.pop("ldap_timeout", UNSET)

        ldap_caref = d.pop("ldap_caref", UNSET)

        ldap_basedn = d.pop("ldap_basedn", UNSET)

        ldap_authcn = d.pop("ldap_authcn", UNSET)

        ldap_extended_enabled = d.pop("ldap_extended_enabled", UNSET)

        ldap_extended_query = d.pop("ldap_extended_query", UNSET)

        def _parse_ldap_binddn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ldap_binddn = _parse_ldap_binddn(d.pop("ldap_binddn", UNSET))

        ldap_attr_user = d.pop("ldap_attr_user", UNSET)

        ldap_attr_group = d.pop("ldap_attr_group", UNSET)

        ldap_attr_member = d.pop("ldap_attr_member", UNSET)

        ldap_rfc2307 = d.pop("ldap_rfc2307", UNSET)

        ldap_rfc2307_userdn = d.pop("ldap_rfc2307_userdn", UNSET)

        ldap_attr_groupobj = d.pop("ldap_attr_groupobj", UNSET)

        ldap_pam_groupdn = d.pop("ldap_pam_groupdn", UNSET)

        ldap_utf8 = d.pop("ldap_utf8", UNSET)

        ldap_nostrip_at = d.pop("ldap_nostrip_at", UNSET)

        ldap_allow_unauthenticated = d.pop("ldap_allow_unauthenticated", UNSET)

        def _parse_radius_auth_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        radius_auth_port = _parse_radius_auth_port(d.pop("radius_auth_port", UNSET))

        def _parse_radius_acct_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        radius_acct_port = _parse_radius_acct_port(d.pop("radius_acct_port", UNSET))

        _radius_protocol = d.pop("radius_protocol", UNSET)
        radius_protocol: AuthServerRadiusProtocol | Unset
        if isinstance(_radius_protocol, Unset):
            radius_protocol = UNSET
        else:
            radius_protocol = AuthServerRadiusProtocol(_radius_protocol)

        radius_timeout = d.pop("radius_timeout", UNSET)

        put_user_auth_servers_endpoint_data_body_item = cls(
            type_=type_,
            name=name,
            host=host,
            ldap_port=ldap_port,
            ldap_urltype=ldap_urltype,
            ldap_scope=ldap_scope,
            ldap_bindpw=ldap_bindpw,
            radius_secret=radius_secret,
            radius_nasip_attribute=radius_nasip_attribute,
            refid=refid,
            ldap_protver=ldap_protver,
            ldap_timeout=ldap_timeout,
            ldap_caref=ldap_caref,
            ldap_basedn=ldap_basedn,
            ldap_authcn=ldap_authcn,
            ldap_extended_enabled=ldap_extended_enabled,
            ldap_extended_query=ldap_extended_query,
            ldap_binddn=ldap_binddn,
            ldap_attr_user=ldap_attr_user,
            ldap_attr_group=ldap_attr_group,
            ldap_attr_member=ldap_attr_member,
            ldap_rfc2307=ldap_rfc2307,
            ldap_rfc2307_userdn=ldap_rfc2307_userdn,
            ldap_attr_groupobj=ldap_attr_groupobj,
            ldap_pam_groupdn=ldap_pam_groupdn,
            ldap_utf8=ldap_utf8,
            ldap_nostrip_at=ldap_nostrip_at,
            ldap_allow_unauthenticated=ldap_allow_unauthenticated,
            radius_auth_port=radius_auth_port,
            radius_acct_port=radius_acct_port,
            radius_protocol=radius_protocol,
            radius_timeout=radius_timeout,
        )

        put_user_auth_servers_endpoint_data_body_item.additional_properties = d
        return put_user_auth_servers_endpoint_data_body_item

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
