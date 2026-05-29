from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.open_vpn_server_allow_compression import OpenVPNServerAllowCompression
from ..models.open_vpn_server_cert_depth import OpenVPNServerCertDepth
from ..models.open_vpn_server_create_gw import OpenVPNServerCreateGw
from ..models.open_vpn_server_dev_mode import OpenVPNServerDevMode
from ..models.open_vpn_server_mode import OpenVPNServerMode
from ..models.open_vpn_server_netbios_ntype import OpenVPNServerNetbiosNtype
from ..models.open_vpn_server_ping_action import OpenVPNServerPingAction
from ..models.open_vpn_server_ping_method import OpenVPNServerPingMethod
from ..models.open_vpn_server_protocol import OpenVPNServerProtocol
from ..models.open_vpn_server_sndrcvbuf import OpenVPNServerSndrcvbuf
from ..models.open_vpn_server_tls_type import OpenVPNServerTlsType
from ..models.open_vpn_server_tlsauth_keydir import OpenVPNServerTlsauthKeydir
from ..models.open_vpn_server_topology import OpenVPNServerTopology
from ..models.open_vpn_server_verbosity_level import OpenVPNServerVerbosityLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenVPNServer")


@_attrs_define
class OpenVPNServer:
    """
    Attributes:
        vpnid (int | None | Unset): The unique ID for this OpenVPN server. This value is assigned by the system and
            cannot be changed.<br>
        vpnif (None | str | Unset): The VPN interface name for this OpenVPN server. This value is assigned by the system
            and cannot be changed.<br>
        description (str | Unset): The description for this OpenVPN server.<br>
        disable (bool | Unset): Disables this OpenVPN server.<br>
        mode (OpenVPNServerMode | Unset): The OpenVPN server mode.<br>
        authmode (list[str] | Unset): The name of the authentication server to use as the authentication backend for
            this OpenVPN server<br><br>This field is only available when the following conditions are met:<br>- `mode` must
            be one of [ server_user, server_tls_user ]<br>
        dev_mode (OpenVPNServerDevMode | Unset): The carrier mode for this OpenVPN server. `tun` mode carries IPv4 and
            IPv6 (layer 3) and is the most common and compatible mode across all platforms. `tap` mode is capable of
            carrying 802.3 (layer 2).<br>
        protocol (OpenVPNServerProtocol | Unset): The protocol used by this OpenVPN server.<br>
        interface (str | Unset): The interface or Virtual IP address where OpenVPN will receive client
            connections.<br><br>This field is only available when the following conditions are met:<br>- `protocol` must not
            be one of [ UDP, TCP ]<br>
        local_port (str | Unset): The port used by OpenVPN to receive client connections. Valid options are: a TCP/UDP
            port number<br> Default: '1194'.
        use_tls (bool | Unset): Enables or disables the use of a TLS key for this OpenVPN server.<br>
        tls (str | Unset): The TLS key this OpenVPN server will use to sign control channel packets with an HMAC
            signature for authentication when establishing the tunnel.<br><br>This field is only available when the
            following conditions are met:<br>- `use_tls` must be equal to `true`<br>
        tls_type (OpenVPNServerTlsType | Unset): The TLS key usage type. In `auth` mode, the TLS key is used only as
            HMAC authentication for the control channel, protecting the peers from unauthorized connections. The `crypt`
            mode encrypts the control channel communication in addition to providing authentication, providing more privacy
            and traffic control channel obfuscation.<br><br>This field is only available when the following conditions are
            met:<br>- `use_tls` must be equal to `true`<br>
        tlsauth_keydir (OpenVPNServerTlsauthKeydir | Unset): The TLS key direction. This must be set to complementary
            values on the client and server. For example, if the server is set to 0, the client must be set to 1. Both may
            be set to omit the direction, in which case the TLS Key will be used bidirectionally.<br><br>This field is only
            available when the following conditions are met:<br>- `use_tls` must be equal to `true`<br> Default:
            OpenVPNServerTlsauthKeydir.DEFAULT.
        caref (str | Unset): The `refid` of the CA object to assume as the peer CA.<br>
        certref (str | Unset): The `refid` of the certificate object to assume as the OpenVPN server certificate.<br>
        cert_depth (OpenVPNServerCertDepth | Unset): The depth of the certificate chain to check when a certificate
            based client signs in. Certificates below this depth are not accepted. This is useful for denying certificates
            made with intermediate CAs generated from the same CA as the server. Set to null to use system default.<br>
            Default: OpenVPNServerCertDepth.VALUE_1.
        dh_length (str | Unset): The Diffie-Hellman (DH) parameter set used for key exchange.<br>
        ecdh_curve (str | Unset): The Elliptic Curve to use for key exchange. The curve from the server certificate is
            used by default when the server uses an ECDSA certificate. Otherwise, secp384r1 is used as a fallback.<br>
        data_ciphers (list[str] | Unset): The encryption algorithms/ciphers allowed by this OpenVPN server.<br>
        data_ciphers_fallback (str | Unset): The fallback encryption algorithm/cipher used for data channel packets when
            communicating with clients that do not support data encryption algorithm negotiation (e.g. Shared Key).<br>
        digest (str | Unset): The algorithm used to authenticate data channel packets, and control channel packets if a
            TLS Key is present.<br>
        strictusercn (bool | Unset): Enables or disables enforcing a match between the common name of the client
            certificate and the username given at login.<br><br>This field is only available when the following conditions
            are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        remote_cert_tls (bool | Unset): Enables or disables requiring hosts to have a client certificate to connect.<br>
            Default: True.
        tunnel_network (str | Unset): The IPv4 virtual network used for private communications between this server and
            client hosts.<br>
        tunnel_networkv6 (str | Unset): The IPv6 virtual network used for private communications between this server and
            client hosts.<br>
        serverbridge_dhcp (bool | Unset): Enables or disables clients on the bridge to obtain DHCP.<br><br>This field is
            only available when the following conditions are met:<br>- `dev_mode` must be equal to `'tap'`<br>
        serverbridge_interface (str | Unset): The interface to which this TAP instance will be bridged. This is not done
            automatically. This interface must be assigned and the bridge created separately. This setting controls which
            existing IP address and subnet mask are used by OpenVPN for the bridge.<br><br>This field is only available when
            the following conditions are met:<br>- `serverbridge_dhcp` must be equal to `true`<br>
        serverbridge_routegateway (bool | Unset): Enables or disables pushing the bridge interface's IPv4 address to
            connecting clients as a route gateway.<br><br>This field is only available when the following conditions are
            met:<br>- `serverbridge_dhcp` must be equal to `true`<br>
        serverbridge_dhcp_start (str | Unset): The bridge DHCP range's start address.<br><br>This field is only
            available when the following conditions are met:<br>- `serverbridge_dhcp` must be equal to `true`<br>
        serverbridge_dhcp_end (str | Unset): The bridge DHCP range's end address.<br><br>This field is only available
            when the following conditions are met:<br>- `serverbridge_dhcp` must be equal to `true`<br>
        gwredir (bool | Unset): Enable forcing all client-generated IPv4 traffic through the tunnel.<br>
        gwredir6 (bool | Unset): Enable forcing all client-generated IPv6 traffic through the tunnel.<br>
        local_network (list[str] | Unset): The IPv4 networks that will be accessible from the remote endpoint. Expressed
            as a list of one or more CIDR ranges or host/network type aliases. This may be left blank if not adding a route
            to the local network through this tunnel on the remote machine. This is generally set to the LAN
            network.<br><br>This field is only available when the following conditions are met:<br>- `gwredir` must be equal
            to `false`<br>
        local_networkv6 (list[str] | Unset): The IPv6 networks that will be accessible from the remote endpoint.
            Expressed as a list of one or more CIDR ranges or host/network type aliases. This may be left blank if not
            adding a route to the local network through this tunnel on the remote machine. This is generally set to the LAN
            network.<br><br>This field is only available when the following conditions are met:<br>- `gwredir6` must be
            equal to `false`<br>
        remote_network (list[str] | Unset): IPv4 networks that will be routed through the tunnel, so that a site-to-site
            VPN can be established without manually changing the routing tables. Expressed as a list of one or more CIDR
            ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be left
            empty for non site-to-site VPN.<br>
        remote_networkv6 (list[str] | Unset): IPv6 networks that will be routed through the tunnel, so that a site-to-
            site VPN can be established without manually changing the routing tables. Expressed as a list of one or more
            CIDR ranges or host/network type aliases. If this is a site-to-site VPN, enter the remote LAN/s here. May be
            left empty for non site-to-site VPN.<br>
        maxclients (int | None | Unset): The maximum number of clients allowed to concurrently connect to this
            server.<br>
        allow_compression (OpenVPNServerAllowCompression | Unset): The compression mode allowed by this OpenVPN server.
            Compression can potentially increase throughput but may allow an attacker to extract secrets if they can control
            compressed plaintext traversing the VPN (e.g. HTTP)<br> Default: OpenVPNServerAllowCompression.NO.
        passtos (bool | Unset): Enables or disables setting the TOS IP header value of tunnel packets to match the
            encapsulated packet value.<br>
        client2client (bool | Unset): Enables or disables allowing communication between clients connected to this
            server.<br>
        duplicate_cn (bool | Unset): Enables or disable allowing the same user to connect multiple times.<br>
        connlimit (int | None | Unset): The number of concurrent connections a single user can have.<br><br>This field
            is only available when the following conditions are met:<br>- `duplicate_cn` must be equal to `true`<br>
        dynamic_ip (bool | Unset): Enables or disables allowing connected clients to retain their connections if their
            IP address changes.<br>
        topology (OpenVPNServerTopology | Unset): The method used to supply a virtual adapter IP address to clients when
            using TUN mode on IPv4.<br><br>This field is only available when the following conditions are met:<br>-
            `dev_mode` must be equal to `'tun'`<br> Default: OpenVPNServerTopology.SUBNET.
        inactive_seconds (int | Unset): The amount of time (in seconds) until a client connection is closed for
            inactivity.<br> Default: 300.
        ping_method (OpenVPNServerPingMethod | Unset): The method used to define ping configuration.<br> Default:
            OpenVPNServerPingMethod.KEEPALIVE.
        keepalive_interval (int | Unset): The keepalive interval parameter.<br><br>This field is only available when the
            following conditions are met:<br>- `ping_method` must be equal to `'keepalive'`<br> Default: 10.
        keepalive_timeout (int | Unset): The keepalive timeout parameter.<br><br>This field is only available when the
            following conditions are met:<br>- `ping_method` must be equal to `'keepalive'`<br> Default: 60.
        ping_seconds (int | Unset): The number of seconds to accept no packets before sending a ping to the remote peer
            over the TCP/UDP control channel.<br><br>This field is only available when the following conditions are
            met:<br>- `ping_method` must be equal to `'ping'`<br> Default: 10.
        ping_push (bool | Unset): Enables or disables push ping to the VPN client.<br><br>This field is only available
            when the following conditions are met:<br>- `ping_method` must be equal to `'ping'`<br>
        ping_action (OpenVPNServerPingAction | Unset): The action to take after a ping to the remote peer times-
            out.<br><br>This field is only available when the following conditions are met:<br>- `ping_method` must be equal
            to `'ping'`<br> Default: OpenVPNServerPingAction.PING_RESTART.
        ping_action_seconds (int | Unset): The number of seconds that must elapse before the ping is considered a
            timeout and the configured `ping_action` is performed.<br><br>This field is only available when the following
            conditions are met:<br>- `ping_method` must be equal to `'ping'`<br> Default: 60.
        ping_action_push (bool | Unset): Enables or disables pushing the ping action to the VPN client.<br><br>This
            field is only available when the following conditions are met:<br>- `ping_method` must be equal to `'ping'`<br>
        dns_domain (str | Unset): The default domain to provide to clients.<br><br>This field is only available when the
            following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        dns_server1 (str | Unset): The primary DNS server to provide to clients.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        dns_server2 (str | Unset): The secondary DNS server to provide to clients.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        dns_server3 (str | Unset): The tertiary DNS server to provide to clients.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        dns_server4 (str | Unset): The quaternary DNS server to provide to clients.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        push_blockoutsidedns (bool | Unset): Enables or disables blocking Windows 10 clients' access to DNS servers
            except across OpenVPN while connected, forcing clients to use only VPN DNS servers.<br><br>This field is only
            available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        push_register_dns (bool | Unset): Enables or disables running `net stop dnscache`, `net start dnscache`,
            `ipconfig /flushdns` and `ipconfig /registerdns` on connection initiation for Windows clients.<br><br>This field
            is only available when the following conditions are met:<br>- `mode` must be one of [ server_user,
            server_tls_user ]<br>
        ntp_server1 (str | Unset): The primary NTP server to provide to clients.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        ntp_server2 (str | Unset): The secondary NTP server to provide to clients.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        netbios_enable (bool | Unset): Enables or disables NetBIOS over TCP/IP.<br><br>This field is only available when
            the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        netbios_ntype (OpenVPNServerNetbiosNtype | Unset): The NetBIOS node type.<br><br>This field is only available
            when the following conditions are met:<br>- `netbios_enable` must be equal to `true`<br>
        netbios_scope (str | Unset): The NetBIOS Scope ID. This provides an extended naming service for NetBIOS over
            TCP/IP. The NetBIOS scope ID isolates NetBIOS traffic on a single network to only those nodes with the same
            NetBIOS scope ID.<br><br>This field is only available when the following conditions are met:<br>-
            `netbios_enable` must be equal to `true`<br>
        wins_server1 (str | Unset): The primary WINS server to provide to clients.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        wins_server2 (str | Unset): The secondary WINS server to provide to clients.<br><br>This field is only available
            when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        custom_options (list[str] | Unset): Additional options to add to the OpenVPN server configuration.<br>
        username_as_common_name (bool | Unset): Enables or disable the username of the client being used in place of the
            certificate common name for purposes such as determining Client Specific Overrides.<br><br>This field is only
            available when the following conditions are met:<br>- `mode` must be one of [ server_user, server_tls_user ]<br>
        sndrcvbuf (OpenVPNServerSndrcvbuf | Unset): The send and receive buffer size for OpenVPN. Set to null to use the
            system default.<br>
        create_gw (OpenVPNServerCreateGw | Unset): The gateway type(s) that will be created when a virtual interface is
            assigned to this OpenVPN server<br> Default: OpenVPNServerCreateGw.BOTH.
        verbosity_level (OpenVPNServerVerbosityLevel | Unset): The OpenVPN logging verbosity level.<br> Default:
            OpenVPNServerVerbosityLevel.VALUE_1.
    """

    vpnid: int | None | Unset = UNSET
    vpnif: None | str | Unset = UNSET
    description: str | Unset = UNSET
    disable: bool | Unset = UNSET
    mode: OpenVPNServerMode | Unset = UNSET
    authmode: list[str] | Unset = UNSET
    dev_mode: OpenVPNServerDevMode | Unset = UNSET
    protocol: OpenVPNServerProtocol | Unset = UNSET
    interface: str | Unset = UNSET
    local_port: str | Unset = "1194"
    use_tls: bool | Unset = UNSET
    tls: str | Unset = UNSET
    tls_type: OpenVPNServerTlsType | Unset = UNSET
    tlsauth_keydir: OpenVPNServerTlsauthKeydir | Unset = OpenVPNServerTlsauthKeydir.DEFAULT
    caref: str | Unset = UNSET
    certref: str | Unset = UNSET
    cert_depth: OpenVPNServerCertDepth | Unset = OpenVPNServerCertDepth.VALUE_1
    dh_length: str | Unset = UNSET
    ecdh_curve: str | Unset = UNSET
    data_ciphers: list[str] | Unset = UNSET
    data_ciphers_fallback: str | Unset = UNSET
    digest: str | Unset = UNSET
    strictusercn: bool | Unset = UNSET
    remote_cert_tls: bool | Unset = True
    tunnel_network: str | Unset = UNSET
    tunnel_networkv6: str | Unset = UNSET
    serverbridge_dhcp: bool | Unset = UNSET
    serverbridge_interface: str | Unset = UNSET
    serverbridge_routegateway: bool | Unset = UNSET
    serverbridge_dhcp_start: str | Unset = UNSET
    serverbridge_dhcp_end: str | Unset = UNSET
    gwredir: bool | Unset = UNSET
    gwredir6: bool | Unset = UNSET
    local_network: list[str] | Unset = UNSET
    local_networkv6: list[str] | Unset = UNSET
    remote_network: list[str] | Unset = UNSET
    remote_networkv6: list[str] | Unset = UNSET
    maxclients: int | None | Unset = UNSET
    allow_compression: OpenVPNServerAllowCompression | Unset = OpenVPNServerAllowCompression.NO
    passtos: bool | Unset = UNSET
    client2client: bool | Unset = UNSET
    duplicate_cn: bool | Unset = UNSET
    connlimit: int | None | Unset = UNSET
    dynamic_ip: bool | Unset = UNSET
    topology: OpenVPNServerTopology | Unset = OpenVPNServerTopology.SUBNET
    inactive_seconds: int | Unset = 300
    ping_method: OpenVPNServerPingMethod | Unset = OpenVPNServerPingMethod.KEEPALIVE
    keepalive_interval: int | Unset = 10
    keepalive_timeout: int | Unset = 60
    ping_seconds: int | Unset = 10
    ping_push: bool | Unset = UNSET
    ping_action: OpenVPNServerPingAction | Unset = OpenVPNServerPingAction.PING_RESTART
    ping_action_seconds: int | Unset = 60
    ping_action_push: bool | Unset = UNSET
    dns_domain: str | Unset = UNSET
    dns_server1: str | Unset = UNSET
    dns_server2: str | Unset = UNSET
    dns_server3: str | Unset = UNSET
    dns_server4: str | Unset = UNSET
    push_blockoutsidedns: bool | Unset = UNSET
    push_register_dns: bool | Unset = UNSET
    ntp_server1: str | Unset = UNSET
    ntp_server2: str | Unset = UNSET
    netbios_enable: bool | Unset = UNSET
    netbios_ntype: OpenVPNServerNetbiosNtype | Unset = UNSET
    netbios_scope: str | Unset = UNSET
    wins_server1: str | Unset = UNSET
    wins_server2: str | Unset = UNSET
    custom_options: list[str] | Unset = UNSET
    username_as_common_name: bool | Unset = UNSET
    sndrcvbuf: OpenVPNServerSndrcvbuf | Unset = UNSET
    create_gw: OpenVPNServerCreateGw | Unset = OpenVPNServerCreateGw.BOTH
    verbosity_level: OpenVPNServerVerbosityLevel | Unset = OpenVPNServerVerbosityLevel.VALUE_1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        authmode: list[str] | Unset = UNSET
        if not isinstance(self.authmode, Unset):
            authmode = self.authmode

        dev_mode: str | Unset = UNSET
        if not isinstance(self.dev_mode, Unset):
            dev_mode = self.dev_mode.value

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        interface = self.interface

        local_port = self.local_port

        use_tls = self.use_tls

        tls = self.tls

        tls_type: str | Unset = UNSET
        if not isinstance(self.tls_type, Unset):
            tls_type = self.tls_type.value

        tlsauth_keydir: str | Unset = UNSET
        if not isinstance(self.tlsauth_keydir, Unset):
            tlsauth_keydir = self.tlsauth_keydir.value

        caref = self.caref

        certref = self.certref

        cert_depth: int | Unset = UNSET
        if not isinstance(self.cert_depth, Unset):
            cert_depth = self.cert_depth.value

        dh_length = self.dh_length

        ecdh_curve = self.ecdh_curve

        data_ciphers: list[str] | Unset = UNSET
        if not isinstance(self.data_ciphers, Unset):
            data_ciphers = self.data_ciphers

        data_ciphers_fallback = self.data_ciphers_fallback

        digest = self.digest

        strictusercn = self.strictusercn

        remote_cert_tls = self.remote_cert_tls

        tunnel_network = self.tunnel_network

        tunnel_networkv6 = self.tunnel_networkv6

        serverbridge_dhcp = self.serverbridge_dhcp

        serverbridge_interface = self.serverbridge_interface

        serverbridge_routegateway = self.serverbridge_routegateway

        serverbridge_dhcp_start = self.serverbridge_dhcp_start

        serverbridge_dhcp_end = self.serverbridge_dhcp_end

        gwredir = self.gwredir

        gwredir6 = self.gwredir6

        local_network: list[str] | Unset = UNSET
        if not isinstance(self.local_network, Unset):
            local_network = self.local_network

        local_networkv6: list[str] | Unset = UNSET
        if not isinstance(self.local_networkv6, Unset):
            local_networkv6 = self.local_networkv6

        remote_network: list[str] | Unset = UNSET
        if not isinstance(self.remote_network, Unset):
            remote_network = self.remote_network

        remote_networkv6: list[str] | Unset = UNSET
        if not isinstance(self.remote_networkv6, Unset):
            remote_networkv6 = self.remote_networkv6

        maxclients: int | None | Unset
        if isinstance(self.maxclients, Unset):
            maxclients = UNSET
        else:
            maxclients = self.maxclients

        allow_compression: str | Unset = UNSET
        if not isinstance(self.allow_compression, Unset):
            allow_compression = self.allow_compression.value

        passtos = self.passtos

        client2client = self.client2client

        duplicate_cn = self.duplicate_cn

        connlimit: int | None | Unset
        if isinstance(self.connlimit, Unset):
            connlimit = UNSET
        else:
            connlimit = self.connlimit

        dynamic_ip = self.dynamic_ip

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

        ping_push = self.ping_push

        ping_action: str | Unset = UNSET
        if not isinstance(self.ping_action, Unset):
            ping_action = self.ping_action.value

        ping_action_seconds = self.ping_action_seconds

        ping_action_push = self.ping_action_push

        dns_domain = self.dns_domain

        dns_server1 = self.dns_server1

        dns_server2 = self.dns_server2

        dns_server3 = self.dns_server3

        dns_server4 = self.dns_server4

        push_blockoutsidedns = self.push_blockoutsidedns

        push_register_dns = self.push_register_dns

        ntp_server1 = self.ntp_server1

        ntp_server2 = self.ntp_server2

        netbios_enable = self.netbios_enable

        netbios_ntype: int | Unset = UNSET
        if not isinstance(self.netbios_ntype, Unset):
            netbios_ntype = self.netbios_ntype.value

        netbios_scope = self.netbios_scope

        wins_server1 = self.wins_server1

        wins_server2 = self.wins_server2

        custom_options: list[str] | Unset = UNSET
        if not isinstance(self.custom_options, Unset):
            custom_options = self.custom_options

        username_as_common_name = self.username_as_common_name

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
        field_dict.update({})
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if vpnif is not UNSET:
            field_dict["vpnif"] = vpnif
        if description is not UNSET:
            field_dict["description"] = description
        if disable is not UNSET:
            field_dict["disable"] = disable
        if mode is not UNSET:
            field_dict["mode"] = mode
        if authmode is not UNSET:
            field_dict["authmode"] = authmode
        if dev_mode is not UNSET:
            field_dict["dev_mode"] = dev_mode
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if interface is not UNSET:
            field_dict["interface"] = interface
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if use_tls is not UNSET:
            field_dict["use_tls"] = use_tls
        if tls is not UNSET:
            field_dict["tls"] = tls
        if tls_type is not UNSET:
            field_dict["tls_type"] = tls_type
        if tlsauth_keydir is not UNSET:
            field_dict["tlsauth_keydir"] = tlsauth_keydir
        if caref is not UNSET:
            field_dict["caref"] = caref
        if certref is not UNSET:
            field_dict["certref"] = certref
        if cert_depth is not UNSET:
            field_dict["cert_depth"] = cert_depth
        if dh_length is not UNSET:
            field_dict["dh_length"] = dh_length
        if ecdh_curve is not UNSET:
            field_dict["ecdh_curve"] = ecdh_curve
        if data_ciphers is not UNSET:
            field_dict["data_ciphers"] = data_ciphers
        if data_ciphers_fallback is not UNSET:
            field_dict["data_ciphers_fallback"] = data_ciphers_fallback
        if digest is not UNSET:
            field_dict["digest"] = digest
        if strictusercn is not UNSET:
            field_dict["strictusercn"] = strictusercn
        if remote_cert_tls is not UNSET:
            field_dict["remote_cert_tls"] = remote_cert_tls
        if tunnel_network is not UNSET:
            field_dict["tunnel_network"] = tunnel_network
        if tunnel_networkv6 is not UNSET:
            field_dict["tunnel_networkv6"] = tunnel_networkv6
        if serverbridge_dhcp is not UNSET:
            field_dict["serverbridge_dhcp"] = serverbridge_dhcp
        if serverbridge_interface is not UNSET:
            field_dict["serverbridge_interface"] = serverbridge_interface
        if serverbridge_routegateway is not UNSET:
            field_dict["serverbridge_routegateway"] = serverbridge_routegateway
        if serverbridge_dhcp_start is not UNSET:
            field_dict["serverbridge_dhcp_start"] = serverbridge_dhcp_start
        if serverbridge_dhcp_end is not UNSET:
            field_dict["serverbridge_dhcp_end"] = serverbridge_dhcp_end
        if gwredir is not UNSET:
            field_dict["gwredir"] = gwredir
        if gwredir6 is not UNSET:
            field_dict["gwredir6"] = gwredir6
        if local_network is not UNSET:
            field_dict["local_network"] = local_network
        if local_networkv6 is not UNSET:
            field_dict["local_networkv6"] = local_networkv6
        if remote_network is not UNSET:
            field_dict["remote_network"] = remote_network
        if remote_networkv6 is not UNSET:
            field_dict["remote_networkv6"] = remote_networkv6
        if maxclients is not UNSET:
            field_dict["maxclients"] = maxclients
        if allow_compression is not UNSET:
            field_dict["allow_compression"] = allow_compression
        if passtos is not UNSET:
            field_dict["passtos"] = passtos
        if client2client is not UNSET:
            field_dict["client2client"] = client2client
        if duplicate_cn is not UNSET:
            field_dict["duplicate_cn"] = duplicate_cn
        if connlimit is not UNSET:
            field_dict["connlimit"] = connlimit
        if dynamic_ip is not UNSET:
            field_dict["dynamic_ip"] = dynamic_ip
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
        if ping_push is not UNSET:
            field_dict["ping_push"] = ping_push
        if ping_action is not UNSET:
            field_dict["ping_action"] = ping_action
        if ping_action_seconds is not UNSET:
            field_dict["ping_action_seconds"] = ping_action_seconds
        if ping_action_push is not UNSET:
            field_dict["ping_action_push"] = ping_action_push
        if dns_domain is not UNSET:
            field_dict["dns_domain"] = dns_domain
        if dns_server1 is not UNSET:
            field_dict["dns_server1"] = dns_server1
        if dns_server2 is not UNSET:
            field_dict["dns_server2"] = dns_server2
        if dns_server3 is not UNSET:
            field_dict["dns_server3"] = dns_server3
        if dns_server4 is not UNSET:
            field_dict["dns_server4"] = dns_server4
        if push_blockoutsidedns is not UNSET:
            field_dict["push_blockoutsidedns"] = push_blockoutsidedns
        if push_register_dns is not UNSET:
            field_dict["push_register_dns"] = push_register_dns
        if ntp_server1 is not UNSET:
            field_dict["ntp_server1"] = ntp_server1
        if ntp_server2 is not UNSET:
            field_dict["ntp_server2"] = ntp_server2
        if netbios_enable is not UNSET:
            field_dict["netbios_enable"] = netbios_enable
        if netbios_ntype is not UNSET:
            field_dict["netbios_ntype"] = netbios_ntype
        if netbios_scope is not UNSET:
            field_dict["netbios_scope"] = netbios_scope
        if wins_server1 is not UNSET:
            field_dict["wins_server1"] = wins_server1
        if wins_server2 is not UNSET:
            field_dict["wins_server2"] = wins_server2
        if custom_options is not UNSET:
            field_dict["custom_options"] = custom_options
        if username_as_common_name is not UNSET:
            field_dict["username_as_common_name"] = username_as_common_name
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

        _mode = d.pop("mode", UNSET)
        mode: OpenVPNServerMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = OpenVPNServerMode(_mode)

        authmode = cast(list[str], d.pop("authmode", UNSET))

        _dev_mode = d.pop("dev_mode", UNSET)
        dev_mode: OpenVPNServerDevMode | Unset
        if isinstance(_dev_mode, Unset):
            dev_mode = UNSET
        else:
            dev_mode = OpenVPNServerDevMode(_dev_mode)

        _protocol = d.pop("protocol", UNSET)
        protocol: OpenVPNServerProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = OpenVPNServerProtocol(_protocol)

        interface = d.pop("interface", UNSET)

        local_port = d.pop("local_port", UNSET)

        use_tls = d.pop("use_tls", UNSET)

        tls = d.pop("tls", UNSET)

        _tls_type = d.pop("tls_type", UNSET)
        tls_type: OpenVPNServerTlsType | Unset
        if isinstance(_tls_type, Unset):
            tls_type = UNSET
        else:
            tls_type = OpenVPNServerTlsType(_tls_type)

        _tlsauth_keydir = d.pop("tlsauth_keydir", UNSET)
        tlsauth_keydir: OpenVPNServerTlsauthKeydir | Unset
        if isinstance(_tlsauth_keydir, Unset):
            tlsauth_keydir = UNSET
        else:
            tlsauth_keydir = OpenVPNServerTlsauthKeydir(_tlsauth_keydir)

        caref = d.pop("caref", UNSET)

        certref = d.pop("certref", UNSET)

        _cert_depth = d.pop("cert_depth", UNSET)
        cert_depth: OpenVPNServerCertDepth | Unset
        if isinstance(_cert_depth, Unset):
            cert_depth = UNSET
        else:
            cert_depth = OpenVPNServerCertDepth(_cert_depth)

        dh_length = d.pop("dh_length", UNSET)

        ecdh_curve = d.pop("ecdh_curve", UNSET)

        data_ciphers = cast(list[str], d.pop("data_ciphers", UNSET))

        data_ciphers_fallback = d.pop("data_ciphers_fallback", UNSET)

        digest = d.pop("digest", UNSET)

        strictusercn = d.pop("strictusercn", UNSET)

        remote_cert_tls = d.pop("remote_cert_tls", UNSET)

        tunnel_network = d.pop("tunnel_network", UNSET)

        tunnel_networkv6 = d.pop("tunnel_networkv6", UNSET)

        serverbridge_dhcp = d.pop("serverbridge_dhcp", UNSET)

        serverbridge_interface = d.pop("serverbridge_interface", UNSET)

        serverbridge_routegateway = d.pop("serverbridge_routegateway", UNSET)

        serverbridge_dhcp_start = d.pop("serverbridge_dhcp_start", UNSET)

        serverbridge_dhcp_end = d.pop("serverbridge_dhcp_end", UNSET)

        gwredir = d.pop("gwredir", UNSET)

        gwredir6 = d.pop("gwredir6", UNSET)

        local_network = cast(list[str], d.pop("local_network", UNSET))

        local_networkv6 = cast(list[str], d.pop("local_networkv6", UNSET))

        remote_network = cast(list[str], d.pop("remote_network", UNSET))

        remote_networkv6 = cast(list[str], d.pop("remote_networkv6", UNSET))

        def _parse_maxclients(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        maxclients = _parse_maxclients(d.pop("maxclients", UNSET))

        _allow_compression = d.pop("allow_compression", UNSET)
        allow_compression: OpenVPNServerAllowCompression | Unset
        if isinstance(_allow_compression, Unset):
            allow_compression = UNSET
        else:
            allow_compression = OpenVPNServerAllowCompression(_allow_compression)

        passtos = d.pop("passtos", UNSET)

        client2client = d.pop("client2client", UNSET)

        duplicate_cn = d.pop("duplicate_cn", UNSET)

        def _parse_connlimit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        connlimit = _parse_connlimit(d.pop("connlimit", UNSET))

        dynamic_ip = d.pop("dynamic_ip", UNSET)

        _topology = d.pop("topology", UNSET)
        topology: OpenVPNServerTopology | Unset
        if isinstance(_topology, Unset):
            topology = UNSET
        else:
            topology = OpenVPNServerTopology(_topology)

        inactive_seconds = d.pop("inactive_seconds", UNSET)

        _ping_method = d.pop("ping_method", UNSET)
        ping_method: OpenVPNServerPingMethod | Unset
        if isinstance(_ping_method, Unset):
            ping_method = UNSET
        else:
            ping_method = OpenVPNServerPingMethod(_ping_method)

        keepalive_interval = d.pop("keepalive_interval", UNSET)

        keepalive_timeout = d.pop("keepalive_timeout", UNSET)

        ping_seconds = d.pop("ping_seconds", UNSET)

        ping_push = d.pop("ping_push", UNSET)

        _ping_action = d.pop("ping_action", UNSET)
        ping_action: OpenVPNServerPingAction | Unset
        if isinstance(_ping_action, Unset):
            ping_action = UNSET
        else:
            ping_action = OpenVPNServerPingAction(_ping_action)

        ping_action_seconds = d.pop("ping_action_seconds", UNSET)

        ping_action_push = d.pop("ping_action_push", UNSET)

        dns_domain = d.pop("dns_domain", UNSET)

        dns_server1 = d.pop("dns_server1", UNSET)

        dns_server2 = d.pop("dns_server2", UNSET)

        dns_server3 = d.pop("dns_server3", UNSET)

        dns_server4 = d.pop("dns_server4", UNSET)

        push_blockoutsidedns = d.pop("push_blockoutsidedns", UNSET)

        push_register_dns = d.pop("push_register_dns", UNSET)

        ntp_server1 = d.pop("ntp_server1", UNSET)

        ntp_server2 = d.pop("ntp_server2", UNSET)

        netbios_enable = d.pop("netbios_enable", UNSET)

        _netbios_ntype = d.pop("netbios_ntype", UNSET)
        netbios_ntype: OpenVPNServerNetbiosNtype | Unset
        if isinstance(_netbios_ntype, Unset):
            netbios_ntype = UNSET
        else:
            netbios_ntype = OpenVPNServerNetbiosNtype(_netbios_ntype)

        netbios_scope = d.pop("netbios_scope", UNSET)

        wins_server1 = d.pop("wins_server1", UNSET)

        wins_server2 = d.pop("wins_server2", UNSET)

        custom_options = cast(list[str], d.pop("custom_options", UNSET))

        username_as_common_name = d.pop("username_as_common_name", UNSET)

        _sndrcvbuf = d.pop("sndrcvbuf", UNSET)
        sndrcvbuf: OpenVPNServerSndrcvbuf | Unset
        if isinstance(_sndrcvbuf, Unset):
            sndrcvbuf = UNSET
        else:
            sndrcvbuf = OpenVPNServerSndrcvbuf(_sndrcvbuf)

        _create_gw = d.pop("create_gw", UNSET)
        create_gw: OpenVPNServerCreateGw | Unset
        if isinstance(_create_gw, Unset):
            create_gw = UNSET
        else:
            create_gw = OpenVPNServerCreateGw(_create_gw)

        _verbosity_level = d.pop("verbosity_level", UNSET)
        verbosity_level: OpenVPNServerVerbosityLevel | Unset
        if isinstance(_verbosity_level, Unset):
            verbosity_level = UNSET
        else:
            verbosity_level = OpenVPNServerVerbosityLevel(_verbosity_level)

        open_vpn_server = cls(
            vpnid=vpnid,
            vpnif=vpnif,
            description=description,
            disable=disable,
            mode=mode,
            authmode=authmode,
            dev_mode=dev_mode,
            protocol=protocol,
            interface=interface,
            local_port=local_port,
            use_tls=use_tls,
            tls=tls,
            tls_type=tls_type,
            tlsauth_keydir=tlsauth_keydir,
            caref=caref,
            certref=certref,
            cert_depth=cert_depth,
            dh_length=dh_length,
            ecdh_curve=ecdh_curve,
            data_ciphers=data_ciphers,
            data_ciphers_fallback=data_ciphers_fallback,
            digest=digest,
            strictusercn=strictusercn,
            remote_cert_tls=remote_cert_tls,
            tunnel_network=tunnel_network,
            tunnel_networkv6=tunnel_networkv6,
            serverbridge_dhcp=serverbridge_dhcp,
            serverbridge_interface=serverbridge_interface,
            serverbridge_routegateway=serverbridge_routegateway,
            serverbridge_dhcp_start=serverbridge_dhcp_start,
            serverbridge_dhcp_end=serverbridge_dhcp_end,
            gwredir=gwredir,
            gwredir6=gwredir6,
            local_network=local_network,
            local_networkv6=local_networkv6,
            remote_network=remote_network,
            remote_networkv6=remote_networkv6,
            maxclients=maxclients,
            allow_compression=allow_compression,
            passtos=passtos,
            client2client=client2client,
            duplicate_cn=duplicate_cn,
            connlimit=connlimit,
            dynamic_ip=dynamic_ip,
            topology=topology,
            inactive_seconds=inactive_seconds,
            ping_method=ping_method,
            keepalive_interval=keepalive_interval,
            keepalive_timeout=keepalive_timeout,
            ping_seconds=ping_seconds,
            ping_push=ping_push,
            ping_action=ping_action,
            ping_action_seconds=ping_action_seconds,
            ping_action_push=ping_action_push,
            dns_domain=dns_domain,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            push_blockoutsidedns=push_blockoutsidedns,
            push_register_dns=push_register_dns,
            ntp_server1=ntp_server1,
            ntp_server2=ntp_server2,
            netbios_enable=netbios_enable,
            netbios_ntype=netbios_ntype,
            netbios_scope=netbios_scope,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            custom_options=custom_options,
            username_as_common_name=username_as_common_name,
            sndrcvbuf=sndrcvbuf,
            create_gw=create_gw,
            verbosity_level=verbosity_level,
        )

        open_vpn_server.additional_properties = d
        return open_vpn_server

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
