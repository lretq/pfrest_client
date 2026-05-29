from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.open_vpn_client_allow_compression import OpenVPNClientAllowCompression
from ..models.open_vpn_client_create_gw import OpenVPNClientCreateGw
from ..models.open_vpn_client_dev_mode import OpenVPNClientDevMode
from ..models.open_vpn_client_exit_notify import OpenVPNClientExitNotify
from ..models.open_vpn_client_mode import OpenVPNClientMode
from ..models.open_vpn_client_ping_action import OpenVPNClientPingAction
from ..models.open_vpn_client_ping_method import OpenVPNClientPingMethod
from ..models.open_vpn_client_protocol import OpenVPNClientProtocol
from ..models.open_vpn_client_proxy_authtype import OpenVPNClientProxyAuthtype
from ..models.open_vpn_client_sndrcvbuf import OpenVPNClientSndrcvbuf
from ..models.open_vpn_client_tls_type import OpenVPNClientTlsType
from ..models.open_vpn_client_tlsauth_keydir import OpenVPNClientTlsauthKeydir
from ..models.open_vpn_client_topology import OpenVPNClientTopology
from ..models.open_vpn_client_verbosity_level import OpenVPNClientVerbosityLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostVPNOpenVPNClientEndpointDataBody")


@_attrs_define
class PostVPNOpenVPNClientEndpointDataBody:
    """
    Attributes:
        mode (OpenVPNClientMode): The OpenVPN client mode.<br>
        dev_mode (OpenVPNClientDevMode): The carrier mode for this OpenVPN client. `tun` mode carries IPv4 and IPv6
            (layer 3) and is the most common and compatible mode across all platforms. `tap` mode is capable of carrying
            802.3 (layer 2).<br>
        protocol (OpenVPNClientProtocol): The protocol used by this OpenVPN client.<br>
        interface (str): The interface used by the firewall to originate this OpenVPN client connection.<br><br>This
            field is only available when the following conditions are met:<br>- `protocol` must not be one of [ UDP, TCP
            ]<br>
        server_addr (str): The IP address or hostname of the OpenVPN server this client will connect to.<br>
        server_port (str): The port used by the server to receive client connections. Valid options are: a TCP/UDP port
            number<br>
        proxy_user (str): The username to use for authentication to the remote proxy.<br><br>This field is only
            available when the following conditions are met:<br>- `proxy_authtype` must not be equal to `'none'`<br>
        proxy_passwd (str): The username to use for authentication to the remote proxy.<br><br>This field is only
            available when the following conditions are met:<br>- `proxy_authtype` must not be equal to `'none'`<br>
        tls_type (OpenVPNClientTlsType): The TLS key usage type. In `auth` mode, the TLS key is used only as HMAC
            authentication for the control channel, protecting the peers from unauthorized connections. The `crypt` mode
            encrypts the control channel communication in addition to providing authentication, providing more privacy and
            traffic control channel obfuscation.<br><br>This field is only available when the following conditions are
            met:<br>- `tls` must not be equal to `NULL`<br>
        caref (str): The `refid` of the CA object to assume as the peer CA.<br>
        data_ciphers (list[str]): The encryption algorithms/ciphers allowed by this OpenVPN client.<br>
        data_ciphers_fallback (str): The fallback encryption algorithm/cipher used for data channel packets when
            communicating with clients that do not support data encryption algorithm negotiation (e.g. Shared Key).<br>
        digest (str): The algorithm used to authenticate data channel packets, and control channel packets if a TLS Key
            is present.<br>
        vpnid (int | None | Unset): The unique ID for this OpenVPN client. This value is assigned by the system and
            cannot be changed.<br>
        vpnif (None | str | Unset): The VPN interface name for this OpenVPN client. This value is assigned by the system
            and cannot be changed.<br>
        description (str | Unset): The description for this OpenVPN client.<br>
        disable (bool | Unset): Disables this OpenVPN client.<br>
        local_port (None | str | Unset): The port binding used by OpenVPN for client connections. Valid options are: a
            TCP/UDP port number<br>
        proxy_addr (None | str | Unset): The address for an HTTP Proxy this client can use to connect to a remote
            server.<br>
        proxy_port (None | str | Unset): The port used by the HTTP Proxy. Valid options are: a TCP/UDP port number<br>
        proxy_authtype (OpenVPNClientProxyAuthtype | Unset): The type of authentication used by the proxy server.<br>
            Default: OpenVPNClientProxyAuthtype.NONE.
        auth_user (None | str | Unset): The username used to authenticate with the OpenVPN server.<br>
        auth_pass (None | str | Unset): The password used to authenticate with the OpenVPN server.<br><br>This field is
            only available when the following conditions are met:<br>- `auth_user` must not be equal to `NULL`<br>
        auth_retry_none (bool | Unset): Disables retrying authentication if an authentication failed error is received
            from the server<br>
        tls (None | str | Unset): The TLS key this OpenVPN client will use to sign control channel packets with an HMAC
            signature for authentication when establishing the tunnel.<br>
        tlsauth_keydir (OpenVPNClientTlsauthKeydir | Unset): The TLS key direction. This must be set to complementary
            values on the client and client. For example, if the client is set to 0, the client must be set to 1. Both may
            be set to omit the direction, in which case the TLS Key will be used bidirectionally.<br><br>This field is only
            available when the following conditions are met:<br>- `tls` must not be equal to `NULL`<br> Default:
            OpenVPNClientTlsauthKeydir.DEFAULT.
        certref (None | str | Unset): The `refid` of the certificate object to assume as the OpenVPN client
            certificate.<br>
        remote_cert_tls (bool | Unset): Enables or disables requiring hosts to have a client certificate to connect.<br>
            Default: True.
        tunnel_network (str | Unset): The IPv4 virtual network used for private communications between this client and
            client hosts.<br>
        tunnel_networkv6 (str | Unset): The IPv6 virtual network used for private communications between this client and
            client hosts.<br>
        remote_network (list[str] | Unset): IPv4 networks that will be routed through the tunnel, so that a site-to-site
            VPN can be established without manually changing the routing tables. Expressed as a list of one or more CIDR
            ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be left
            empty for non site-to-site VPN.<br>
        remote_networkv6 (list[str] | Unset): IPv6 networks that will be routed through the tunnel, so that a site-to-
            site VPN can be established without manually changing the routing tables. Expressed as a list of one or more
            CIDR ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be
            left empty for non site-to-site VPN.<br>
        use_shaper (int | None | Unset): Maximum outgoing bandwidth (in bytes per second) for this tunnel. Use `null` no
            limit.<br>
        allow_compression (OpenVPNClientAllowCompression | Unset): The compression mode allowed by this OpenVPN client.
            Compression can potentially increase throughput but may allow an attacker to extract secrets if they can control
            compressed plaintext traversing the VPN (e.g. HTTP)<br> Default: OpenVPNClientAllowCompression.NO.
        passtos (bool | Unset): Enables or disables setting the TOS IP header value of tunnel packets to match the
            encapsulated packet value.<br>
        route_no_pull (bool | Unset): Enables or disables the servers ability to add routes to the client's routing
            table.<br>
        route_no_exec (bool | Unset): Enables or disables adding/removing routes automatically.<br>
        dns_add (bool | Unset): Enables or disables using the DNS server(s) provided by the OpenVPN server.<br>
        topology (OpenVPNClientTopology | Unset): The method used to supply a virtual adapter IP address to clients when
            using TUN mode on IPv4.<br><br>This field is only available when the following conditions are met:<br>-
            `dev_mode` must be equal to `'tun'`<br> Default: OpenVPNClientTopology.SUBNET.
        inactive_seconds (int | Unset): The amount of time (in seconds) until a client connection is closed for
            inactivity.<br> Default: 300.
        ping_method (OpenVPNClientPingMethod | Unset): The method used to define ping configuration.<br> Default:
            OpenVPNClientPingMethod.KEEPALIVE.
        keepalive_interval (int | Unset): The keepalive interval parameter.<br><br>This field is only available when the
            following conditions are met:<br>- `ping_method` must be equal to `'keepalive'`<br> Default: 10.
        keepalive_timeout (int | Unset): The keepalive timeout parameter.<br><br>This field is only available when the
            following conditions are met:<br>- `ping_method` must be equal to `'keepalive'`<br> Default: 60.
        ping_seconds (int | Unset): The number of seconds to accept no packets before sending a ping to the remote peer
            over the TCP/UDP control channel.<br><br>This field is only available when the following conditions are
            met:<br>- `ping_method` must be equal to `'ping'`<br> Default: 10.
        ping_action (OpenVPNClientPingAction | Unset): The action to take after a ping to the remote peer times-
            out.<br><br>This field is only available when the following conditions are met:<br>- `ping_method` must be equal
            to `'ping'`<br> Default: OpenVPNClientPingAction.PING_RESTART.
        ping_action_seconds (int | Unset): The number of seconds that must elapse before the ping is considered a
            timeout and the configured `ping_action` is performed.<br><br>This field is only available when the following
            conditions are met:<br>- `ping_method` must be equal to `'ping'`<br> Default: 60.
        custom_options (list[str] | Unset): Additional options to add to the OpenVPN client configuration.<br>
        udp_fast_io (bool | Unset): Enables or disables fast I/O operations with UDP writes to tun/tap
            (Experimental).<br>
        exit_notify (OpenVPNClientExitNotify | Unset): The number of times this client will attempt to send an exit
            notifications.<br> Default: OpenVPNClientExitNotify.NONE.
        sndrcvbuf (OpenVPNClientSndrcvbuf | Unset): The send and receive buffer size for OpenVPN. Set to null to use the
            system default.<br>
        create_gw (OpenVPNClientCreateGw | Unset): The gateway type(s) that will be created when a virtual interface is
            assigned to this OpenVPN server<br> Default: OpenVPNClientCreateGw.BOTH.
        verbosity_level (OpenVPNClientVerbosityLevel | Unset): The OpenVPN logging verbosity level.<br> Default:
            OpenVPNClientVerbosityLevel.VALUE_1.
    """

    mode: OpenVPNClientMode
    dev_mode: OpenVPNClientDevMode
    protocol: OpenVPNClientProtocol
    interface: str
    server_addr: str
    server_port: str
    proxy_user: str
    proxy_passwd: str
    tls_type: OpenVPNClientTlsType
    caref: str
    data_ciphers: list[str]
    data_ciphers_fallback: str
    digest: str
    vpnid: int | None | Unset = UNSET
    vpnif: None | str | Unset = UNSET
    description: str | Unset = UNSET
    disable: bool | Unset = UNSET
    local_port: None | str | Unset = UNSET
    proxy_addr: None | str | Unset = UNSET
    proxy_port: None | str | Unset = UNSET
    proxy_authtype: OpenVPNClientProxyAuthtype | Unset = OpenVPNClientProxyAuthtype.NONE
    auth_user: None | str | Unset = UNSET
    auth_pass: None | str | Unset = UNSET
    auth_retry_none: bool | Unset = UNSET
    tls: None | str | Unset = UNSET
    tlsauth_keydir: OpenVPNClientTlsauthKeydir | Unset = OpenVPNClientTlsauthKeydir.DEFAULT
    certref: None | str | Unset = UNSET
    remote_cert_tls: bool | Unset = True
    tunnel_network: str | Unset = UNSET
    tunnel_networkv6: str | Unset = UNSET
    remote_network: list[str] | Unset = UNSET
    remote_networkv6: list[str] | Unset = UNSET
    use_shaper: int | None | Unset = UNSET
    allow_compression: OpenVPNClientAllowCompression | Unset = OpenVPNClientAllowCompression.NO
    passtos: bool | Unset = UNSET
    route_no_pull: bool | Unset = UNSET
    route_no_exec: bool | Unset = UNSET
    dns_add: bool | Unset = UNSET
    topology: OpenVPNClientTopology | Unset = OpenVPNClientTopology.SUBNET
    inactive_seconds: int | Unset = 300
    ping_method: OpenVPNClientPingMethod | Unset = OpenVPNClientPingMethod.KEEPALIVE
    keepalive_interval: int | Unset = 10
    keepalive_timeout: int | Unset = 60
    ping_seconds: int | Unset = 10
    ping_action: OpenVPNClientPingAction | Unset = OpenVPNClientPingAction.PING_RESTART
    ping_action_seconds: int | Unset = 60
    custom_options: list[str] | Unset = UNSET
    udp_fast_io: bool | Unset = UNSET
    exit_notify: OpenVPNClientExitNotify | Unset = OpenVPNClientExitNotify.NONE
    sndrcvbuf: OpenVPNClientSndrcvbuf | Unset = UNSET
    create_gw: OpenVPNClientCreateGw | Unset = OpenVPNClientCreateGw.BOTH
    verbosity_level: OpenVPNClientVerbosityLevel | Unset = OpenVPNClientVerbosityLevel.VALUE_1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        dev_mode = self.dev_mode.value

        protocol = self.protocol.value

        interface = self.interface

        server_addr = self.server_addr

        server_port = self.server_port

        proxy_user = self.proxy_user

        proxy_passwd = self.proxy_passwd

        tls_type = self.tls_type.value

        caref = self.caref

        data_ciphers = self.data_ciphers

        data_ciphers_fallback = self.data_ciphers_fallback

        digest = self.digest

        vpnid: int | None | Unset
        if isinstance(self.vpnid, Unset):
            vpnid = UNSET
        else:
            vpnid = self.vpnid

        vpnif: None | str | Unset
        if isinstance(self.vpnif, Unset):
            vpnif = UNSET
        else:
            vpnif = self.vpnif

        description = self.description

        disable = self.disable

        local_port: None | str | Unset
        if isinstance(self.local_port, Unset):
            local_port = UNSET
        else:
            local_port = self.local_port

        proxy_addr: None | str | Unset
        if isinstance(self.proxy_addr, Unset):
            proxy_addr = UNSET
        else:
            proxy_addr = self.proxy_addr

        proxy_port: None | str | Unset
        if isinstance(self.proxy_port, Unset):
            proxy_port = UNSET
        else:
            proxy_port = self.proxy_port

        proxy_authtype: str | Unset = UNSET
        if not isinstance(self.proxy_authtype, Unset):
            proxy_authtype = self.proxy_authtype.value

        auth_user: None | str | Unset
        if isinstance(self.auth_user, Unset):
            auth_user = UNSET
        else:
            auth_user = self.auth_user

        auth_pass: None | str | Unset
        if isinstance(self.auth_pass, Unset):
            auth_pass = UNSET
        else:
            auth_pass = self.auth_pass

        auth_retry_none = self.auth_retry_none

        tls: None | str | Unset
        if isinstance(self.tls, Unset):
            tls = UNSET
        else:
            tls = self.tls

        tlsauth_keydir: str | Unset = UNSET
        if not isinstance(self.tlsauth_keydir, Unset):
            tlsauth_keydir = self.tlsauth_keydir.value

        certref: None | str | Unset
        if isinstance(self.certref, Unset):
            certref = UNSET
        else:
            certref = self.certref

        remote_cert_tls = self.remote_cert_tls

        tunnel_network = self.tunnel_network

        tunnel_networkv6 = self.tunnel_networkv6

        remote_network: list[str] | Unset = UNSET
        if not isinstance(self.remote_network, Unset):
            remote_network = self.remote_network

        remote_networkv6: list[str] | Unset = UNSET
        if not isinstance(self.remote_networkv6, Unset):
            remote_networkv6 = self.remote_networkv6

        use_shaper: int | None | Unset
        if isinstance(self.use_shaper, Unset):
            use_shaper = UNSET
        else:
            use_shaper = self.use_shaper

        allow_compression: str | Unset = UNSET
        if not isinstance(self.allow_compression, Unset):
            allow_compression = self.allow_compression.value

        passtos = self.passtos

        route_no_pull = self.route_no_pull

        route_no_exec = self.route_no_exec

        dns_add = self.dns_add

        topology: str | Unset = UNSET
        if not isinstance(self.topology, Unset):
            topology = self.topology.value

        inactive_seconds = self.inactive_seconds

        ping_method: str | Unset = UNSET
        if not isinstance(self.ping_method, Unset):
            ping_method = self.ping_method.value

        keepalive_interval = self.keepalive_interval

        keepalive_timeout = self.keepalive_timeout

        ping_seconds = self.ping_seconds

        ping_action: str | Unset = UNSET
        if not isinstance(self.ping_action, Unset):
            ping_action = self.ping_action.value

        ping_action_seconds = self.ping_action_seconds

        custom_options: list[str] | Unset = UNSET
        if not isinstance(self.custom_options, Unset):
            custom_options = self.custom_options

        udp_fast_io = self.udp_fast_io

        exit_notify: str | Unset = UNSET
        if not isinstance(self.exit_notify, Unset):
            exit_notify = self.exit_notify.value

        sndrcvbuf: int | Unset = UNSET
        if not isinstance(self.sndrcvbuf, Unset):
            sndrcvbuf = self.sndrcvbuf.value

        create_gw: str | Unset = UNSET
        if not isinstance(self.create_gw, Unset):
            create_gw = self.create_gw.value

        verbosity_level: int | Unset = UNSET
        if not isinstance(self.verbosity_level, Unset):
            verbosity_level = self.verbosity_level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "dev_mode": dev_mode,
                "protocol": protocol,
                "interface": interface,
                "server_addr": server_addr,
                "server_port": server_port,
                "proxy_user": proxy_user,
                "proxy_passwd": proxy_passwd,
                "tls_type": tls_type,
                "caref": caref,
                "data_ciphers": data_ciphers,
                "data_ciphers_fallback": data_ciphers_fallback,
                "digest": digest,
            }
        )
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if vpnif is not UNSET:
            field_dict["vpnif"] = vpnif
        if description is not UNSET:
            field_dict["description"] = description
        if disable is not UNSET:
            field_dict["disable"] = disable
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if proxy_addr is not UNSET:
            field_dict["proxy_addr"] = proxy_addr
        if proxy_port is not UNSET:
            field_dict["proxy_port"] = proxy_port
        if proxy_authtype is not UNSET:
            field_dict["proxy_authtype"] = proxy_authtype
        if auth_user is not UNSET:
            field_dict["auth_user"] = auth_user
        if auth_pass is not UNSET:
            field_dict["auth_pass"] = auth_pass
        if auth_retry_none is not UNSET:
            field_dict["auth_retry_none"] = auth_retry_none
        if tls is not UNSET:
            field_dict["tls"] = tls
        if tlsauth_keydir is not UNSET:
            field_dict["tlsauth_keydir"] = tlsauth_keydir
        if certref is not UNSET:
            field_dict["certref"] = certref
        if remote_cert_tls is not UNSET:
            field_dict["remote_cert_tls"] = remote_cert_tls
        if tunnel_network is not UNSET:
            field_dict["tunnel_network"] = tunnel_network
        if tunnel_networkv6 is not UNSET:
            field_dict["tunnel_networkv6"] = tunnel_networkv6
        if remote_network is not UNSET:
            field_dict["remote_network"] = remote_network
        if remote_networkv6 is not UNSET:
            field_dict["remote_networkv6"] = remote_networkv6
        if use_shaper is not UNSET:
            field_dict["use_shaper"] = use_shaper
        if allow_compression is not UNSET:
            field_dict["allow_compression"] = allow_compression
        if passtos is not UNSET:
            field_dict["passtos"] = passtos
        if route_no_pull is not UNSET:
            field_dict["route_no_pull"] = route_no_pull
        if route_no_exec is not UNSET:
            field_dict["route_no_exec"] = route_no_exec
        if dns_add is not UNSET:
            field_dict["dns_add"] = dns_add
        if topology is not UNSET:
            field_dict["topology"] = topology
        if inactive_seconds is not UNSET:
            field_dict["inactive_seconds"] = inactive_seconds
        if ping_method is not UNSET:
            field_dict["ping_method"] = ping_method
        if keepalive_interval is not UNSET:
            field_dict["keepalive_interval"] = keepalive_interval
        if keepalive_timeout is not UNSET:
            field_dict["keepalive_timeout"] = keepalive_timeout
        if ping_seconds is not UNSET:
            field_dict["ping_seconds"] = ping_seconds
        if ping_action is not UNSET:
            field_dict["ping_action"] = ping_action
        if ping_action_seconds is not UNSET:
            field_dict["ping_action_seconds"] = ping_action_seconds
        if custom_options is not UNSET:
            field_dict["custom_options"] = custom_options
        if udp_fast_io is not UNSET:
            field_dict["udp_fast_io"] = udp_fast_io
        if exit_notify is not UNSET:
            field_dict["exit_notify"] = exit_notify
        if sndrcvbuf is not UNSET:
            field_dict["sndrcvbuf"] = sndrcvbuf
        if create_gw is not UNSET:
            field_dict["create_gw"] = create_gw
        if verbosity_level is not UNSET:
            field_dict["verbosity_level"] = verbosity_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = OpenVPNClientMode(d.pop("mode"))

        dev_mode = OpenVPNClientDevMode(d.pop("dev_mode"))

        protocol = OpenVPNClientProtocol(d.pop("protocol"))

        interface = d.pop("interface")

        server_addr = d.pop("server_addr")

        server_port = d.pop("server_port")

        proxy_user = d.pop("proxy_user")

        proxy_passwd = d.pop("proxy_passwd")

        tls_type = OpenVPNClientTlsType(d.pop("tls_type"))

        caref = d.pop("caref")

        data_ciphers = cast(list[str], d.pop("data_ciphers"))

        data_ciphers_fallback = d.pop("data_ciphers_fallback")

        digest = d.pop("digest")

        def _parse_vpnid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vpnid = _parse_vpnid(d.pop("vpnid", UNSET))

        def _parse_vpnif(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vpnif = _parse_vpnif(d.pop("vpnif", UNSET))

        description = d.pop("description", UNSET)

        disable = d.pop("disable", UNSET)

        def _parse_local_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_port = _parse_local_port(d.pop("local_port", UNSET))

        def _parse_proxy_addr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proxy_addr = _parse_proxy_addr(d.pop("proxy_addr", UNSET))

        def _parse_proxy_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proxy_port = _parse_proxy_port(d.pop("proxy_port", UNSET))

        _proxy_authtype = d.pop("proxy_authtype", UNSET)
        proxy_authtype: OpenVPNClientProxyAuthtype | Unset
        if isinstance(_proxy_authtype, Unset):
            proxy_authtype = UNSET
        else:
            proxy_authtype = OpenVPNClientProxyAuthtype(_proxy_authtype)

        def _parse_auth_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_user = _parse_auth_user(d.pop("auth_user", UNSET))

        def _parse_auth_pass(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auth_pass = _parse_auth_pass(d.pop("auth_pass", UNSET))

        auth_retry_none = d.pop("auth_retry_none", UNSET)

        def _parse_tls(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tls = _parse_tls(d.pop("tls", UNSET))

        _tlsauth_keydir = d.pop("tlsauth_keydir", UNSET)
        tlsauth_keydir: OpenVPNClientTlsauthKeydir | Unset
        if isinstance(_tlsauth_keydir, Unset):
            tlsauth_keydir = UNSET
        else:
            tlsauth_keydir = OpenVPNClientTlsauthKeydir(_tlsauth_keydir)

        def _parse_certref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certref = _parse_certref(d.pop("certref", UNSET))

        remote_cert_tls = d.pop("remote_cert_tls", UNSET)

        tunnel_network = d.pop("tunnel_network", UNSET)

        tunnel_networkv6 = d.pop("tunnel_networkv6", UNSET)

        remote_network = cast(list[str], d.pop("remote_network", UNSET))

        remote_networkv6 = cast(list[str], d.pop("remote_networkv6", UNSET))

        def _parse_use_shaper(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        use_shaper = _parse_use_shaper(d.pop("use_shaper", UNSET))

        _allow_compression = d.pop("allow_compression", UNSET)
        allow_compression: OpenVPNClientAllowCompression | Unset
        if isinstance(_allow_compression, Unset):
            allow_compression = UNSET
        else:
            allow_compression = OpenVPNClientAllowCompression(_allow_compression)

        passtos = d.pop("passtos", UNSET)

        route_no_pull = d.pop("route_no_pull", UNSET)

        route_no_exec = d.pop("route_no_exec", UNSET)

        dns_add = d.pop("dns_add", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: OpenVPNClientTopology | Unset
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = OpenVPNClientTopology(_topology)

        inactive_seconds = d.pop("inactive_seconds", UNSET)

        _ping_method = d.pop("ping_method", UNSET)
        ping_method: OpenVPNClientPingMethod | Unset
        if isinstance(_ping_method, Unset):
            ping_method = UNSET
        else:
            ping_method = OpenVPNClientPingMethod(_ping_method)

        keepalive_interval = d.pop("keepalive_interval", UNSET)

        keepalive_timeout = d.pop("keepalive_timeout", UNSET)

        ping_seconds = d.pop("ping_seconds", UNSET)

        _ping_action = d.pop("ping_action", UNSET)
        ping_action: OpenVPNClientPingAction | Unset
        if isinstance(_ping_action, Unset):
            ping_action = UNSET
        else:
            ping_action = OpenVPNClientPingAction(_ping_action)

        ping_action_seconds = d.pop("ping_action_seconds", UNSET)

        custom_options = cast(list[str], d.pop("custom_options", UNSET))

        udp_fast_io = d.pop("udp_fast_io", UNSET)

        _exit_notify = d.pop("exit_notify", UNSET)
        exit_notify: OpenVPNClientExitNotify | Unset
        if isinstance(_exit_notify, Unset):
            exit_notify = UNSET
        else:
            exit_notify = OpenVPNClientExitNotify(_exit_notify)

        _sndrcvbuf = d.pop("sndrcvbuf", UNSET)
        sndrcvbuf: OpenVPNClientSndrcvbuf | Unset
        if isinstance(_sndrcvbuf, Unset):
            sndrcvbuf = UNSET
        else:
            sndrcvbuf = OpenVPNClientSndrcvbuf(_sndrcvbuf)

        _create_gw = d.pop("create_gw", UNSET)
        create_gw: OpenVPNClientCreateGw | Unset
        if isinstance(_create_gw, Unset):
            create_gw = UNSET
        else:
            create_gw = OpenVPNClientCreateGw(_create_gw)

        _verbosity_level = d.pop("verbosity_level", UNSET)
        verbosity_level: OpenVPNClientVerbosityLevel | Unset
        if isinstance(_verbosity_level, Unset):
            verbosity_level = UNSET
        else:
            verbosity_level = OpenVPNClientVerbosityLevel(_verbosity_level)

        post_vpn_open_vpn_client_endpoint_data_body = cls(
            mode=mode,
            dev_mode=dev_mode,
            protocol=protocol,
            interface=interface,
            server_addr=server_addr,
            server_port=server_port,
            proxy_user=proxy_user,
            proxy_passwd=proxy_passwd,
            tls_type=tls_type,
            caref=caref,
            data_ciphers=data_ciphers,
            data_ciphers_fallback=data_ciphers_fallback,
            digest=digest,
            vpnid=vpnid,
            vpnif=vpnif,
            description=description,
            disable=disable,
            local_port=local_port,
            proxy_addr=proxy_addr,
            proxy_port=proxy_port,
            proxy_authtype=proxy_authtype,
            auth_user=auth_user,
            auth_pass=auth_pass,
            auth_retry_none=auth_retry_none,
            tls=tls,
            tlsauth_keydir=tlsauth_keydir,
            certref=certref,
            remote_cert_tls=remote_cert_tls,
            tunnel_network=tunnel_network,
            tunnel_networkv6=tunnel_networkv6,
            remote_network=remote_network,
            remote_networkv6=remote_networkv6,
            use_shaper=use_shaper,
            allow_compression=allow_compression,
            passtos=passtos,
            route_no_pull=route_no_pull,
            route_no_exec=route_no_exec,
            dns_add=dns_add,
            topology=topology,
            inactive_seconds=inactive_seconds,
            ping_method=ping_method,
            keepalive_interval=keepalive_interval,
            keepalive_timeout=keepalive_timeout,
            ping_seconds=ping_seconds,
            ping_action=ping_action,
            ping_action_seconds=ping_action_seconds,
            custom_options=custom_options,
            udp_fast_io=udp_fast_io,
            exit_notify=exit_notify,
            sndrcvbuf=sndrcvbuf,
            create_gw=create_gw,
            verbosity_level=verbosity_level,
        )

        post_vpn_open_vpn_client_endpoint_data_body.additional_properties = d
        return post_vpn_open_vpn_client_endpoint_data_body

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
