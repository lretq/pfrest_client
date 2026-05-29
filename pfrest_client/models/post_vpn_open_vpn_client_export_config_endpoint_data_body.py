from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.open_vpn_client_export_config_bindmode import OpenVPNClientExportConfigBindmode
from ..models.open_vpn_client_export_config_p12_encryption import OpenVPNClientExportConfigP12Encryption
from ..models.open_vpn_client_export_config_useaddr import OpenVPNClientExportConfigUseaddr
from ..models.open_vpn_client_export_config_useproxypass import OpenVPNClientExportConfigUseproxypass
from ..models.open_vpn_client_export_config_useproxytype import OpenVPNClientExportConfigUseproxytype
from ..models.open_vpn_client_export_config_verifyservercn import OpenVPNClientExportConfigVerifyservercn
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostVPNOpenVPNClientExportConfigEndpointDataBody")


@_attrs_define
class PostVPNOpenVPNClientExportConfigEndpointDataBody:
    """
    Attributes:
        server (int): The VPN ID of the OpenVPN server this client export corresponds to.<br>
        pkcs11providers (list[str]): The client local path to the PKCS#11 provider(s) (DLL, module)<br><br>This field is
            only available when the following conditions are met:<br>- `usepkcs11` must be equal to `true`<br>
        pkcs11id (str): The object's ID on the PKCS#11 device.<br><br>This field is only available when the following
            conditions are met:<br>- `usepkcs11` must be equal to `true`<br>
        pass_ (str): Password used to protect the certificate file contents.<br><br>This field is only available when
            the following conditions are met:<br>- `usepass` must be equal to `true`<br>
        proxyaddr (str): The IP address or hostname of the proxy server to use.<br><br>This field is only available when
            the following conditions are met:<br>- `useproxy` must be equal to `true`<br>
        proxyport (str): The port where the proxy server is listening. Valid options are: a TCP/UDP port
            number<br><br>This field is only available when the following conditions are met:<br>- `useproxy` must be equal
            to `true`<br>
        useproxypass (OpenVPNClientExportConfigUseproxypass): The type of authentication to use for the proxy
            server.<br><br>This field is only available when the following conditions are met:<br>- `useproxy` must be equal
            to `true`<br>
        proxyuser (str): The username to use to authenticate with the proxy server.<br><br>This field is only available
            when the following conditions are met:<br>- `useproxy` must be equal to `true`<br>- `useproxypass` must be one
            of [ basic, ntlm ]<br>
        proxypass (str): The password to use to authenticate with the proxy server.<br><br>This field is only available
            when the following conditions are met:<br>- `useproxy` must be equal to `true`<br>- `useproxypass` must be one
            of [ basic, ntlm ]<br>
        useaddr (OpenVPNClientExportConfigUseaddr | Unset): The method to use for the OpenVPN server address listed in
            the config export.<br> Default: OpenVPNClientExportConfigUseaddr.SERVERADDR.
        useaddr_hostname (str | Unset): The hostname to use for the OpenVPN server address.<br><br>This field is only
            available when the following conditions are met:<br>- `useaddr` must be equal to `'other'`<br>
        verifyservercn (OpenVPNClientExportConfigVerifyservercn | Unset): Verify the server certificate Common Name (CN)
            when the client connects.<br> Default: OpenVPNClientExportConfigVerifyservercn.AUTO.
        blockoutsidedns (bool | Unset): Block access to DNS servers except across OpenVPN while connected, forcing
            clients to use only VPN DNS servers.<br>
        legacy (bool | Unset): Do not include OpenVPN 2.5 and later settings in the client configuration.<br>
        silent (bool | Unset): Create Windows installer for unattended deploy.<br>
        bindmode (OpenVPNClientExportConfigBindmode | Unset): The port binding mode to use. If OpenVPN client binds to
            the default OpenVPN port (1194), two clients may not run concurrently.<br> Default:
            OpenVPNClientExportConfigBindmode.NOBIND.
        usepkcs11 (bool | Unset): Use PKCS#11 storage device (cryptographic token, HSM, smart card) instead of local
            files.<br>
        usetoken (bool | Unset): Use Microsoft Certificate Storage instead of local files.<br>
        usepass (bool | Unset): Use a password to protect the PKCS#12 file contents or key in Viscosity bundles.<br>
        p12encryption (OpenVPNClientExportConfigP12Encryption | Unset): The level of encryption to use when exporting a
            PKCS#12 archive. Encryption support varies by Operating System and program<br> Default:
            OpenVPNClientExportConfigP12Encryption.HIGH.
        useproxy (bool | Unset): Use proxy to communicate with the OpenVPN server.<br>
        useproxytype (OpenVPNClientExportConfigUseproxytype | Unset): The proxy type to use.<br><br>This field is only
            available when the following conditions are met:<br>- `useproxy` must be equal to `true`<br> Default:
            OpenVPNClientExportConfigUseproxytype.HTTP.
        advancedoptions (str | Unset): Additional options to add to the OpenVPN client export configuration.<br>
    """

    server: int
    pkcs11providers: list[str]
    pkcs11id: str
    pass_: str
    proxyaddr: str
    proxyport: str
    useproxypass: OpenVPNClientExportConfigUseproxypass
    proxyuser: str
    proxypass: str
    useaddr: OpenVPNClientExportConfigUseaddr | Unset = OpenVPNClientExportConfigUseaddr.SERVERADDR
    useaddr_hostname: str | Unset = UNSET
    verifyservercn: OpenVPNClientExportConfigVerifyservercn | Unset = OpenVPNClientExportConfigVerifyservercn.AUTO
    blockoutsidedns: bool | Unset = UNSET
    legacy: bool | Unset = UNSET
    silent: bool | Unset = UNSET
    bindmode: OpenVPNClientExportConfigBindmode | Unset = OpenVPNClientExportConfigBindmode.NOBIND
    usepkcs11: bool | Unset = UNSET
    usetoken: bool | Unset = UNSET
    usepass: bool | Unset = UNSET
    p12encryption: OpenVPNClientExportConfigP12Encryption | Unset = OpenVPNClientExportConfigP12Encryption.HIGH
    useproxy: bool | Unset = UNSET
    useproxytype: OpenVPNClientExportConfigUseproxytype | Unset = OpenVPNClientExportConfigUseproxytype.HTTP
    advancedoptions: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server = self.server

        pkcs11providers = self.pkcs11providers

        pkcs11id = self.pkcs11id

        pass_ = self.pass_

        proxyaddr = self.proxyaddr

        proxyport = self.proxyport

        useproxypass = self.useproxypass.value

        proxyuser = self.proxyuser

        proxypass = self.proxypass

        useaddr: str | Unset = UNSET
        if not isinstance(self.useaddr, Unset):
            useaddr = self.useaddr.value

        useaddr_hostname = self.useaddr_hostname

        verifyservercn: str | Unset = UNSET
        if not isinstance(self.verifyservercn, Unset):
            verifyservercn = self.verifyservercn.value

        blockoutsidedns = self.blockoutsidedns

        legacy = self.legacy

        silent = self.silent

        bindmode: str | Unset = UNSET
        if not isinstance(self.bindmode, Unset):
            bindmode = self.bindmode.value

        usepkcs11 = self.usepkcs11

        usetoken = self.usetoken

        usepass = self.usepass

        p12encryption: str | Unset = UNSET
        if not isinstance(self.p12encryption, Unset):
            p12encryption = self.p12encryption.value

        useproxy = self.useproxy

        useproxytype: str | Unset = UNSET
        if not isinstance(self.useproxytype, Unset):
            useproxytype = self.useproxytype.value

        advancedoptions = self.advancedoptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server": server,
                "pkcs11providers": pkcs11providers,
                "pkcs11id": pkcs11id,
                "pass": pass_,
                "proxyaddr": proxyaddr,
                "proxyport": proxyport,
                "useproxypass": useproxypass,
                "proxyuser": proxyuser,
                "proxypass": proxypass,
            }
        )
        if useaddr is not UNSET:
            field_dict["useaddr"] = useaddr
        if useaddr_hostname is not UNSET:
            field_dict["useaddr_hostname"] = useaddr_hostname
        if verifyservercn is not UNSET:
            field_dict["verifyservercn"] = verifyservercn
        if blockoutsidedns is not UNSET:
            field_dict["blockoutsidedns"] = blockoutsidedns
        if legacy is not UNSET:
            field_dict["legacy"] = legacy
        if silent is not UNSET:
            field_dict["silent"] = silent
        if bindmode is not UNSET:
            field_dict["bindmode"] = bindmode
        if usepkcs11 is not UNSET:
            field_dict["usepkcs11"] = usepkcs11
        if usetoken is not UNSET:
            field_dict["usetoken"] = usetoken
        if usepass is not UNSET:
            field_dict["usepass"] = usepass
        if p12encryption is not UNSET:
            field_dict["p12encryption"] = p12encryption
        if useproxy is not UNSET:
            field_dict["useproxy"] = useproxy
        if useproxytype is not UNSET:
            field_dict["useproxytype"] = useproxytype
        if advancedoptions is not UNSET:
            field_dict["advancedoptions"] = advancedoptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        server = d.pop("server")

        pkcs11providers = cast(list[str], d.pop("pkcs11providers"))

        pkcs11id = d.pop("pkcs11id")

        pass_ = d.pop("pass")

        proxyaddr = d.pop("proxyaddr")

        proxyport = d.pop("proxyport")

        useproxypass = OpenVPNClientExportConfigUseproxypass(d.pop("useproxypass"))

        proxyuser = d.pop("proxyuser")

        proxypass = d.pop("proxypass")

        _useaddr = d.pop("useaddr", UNSET)
        useaddr: OpenVPNClientExportConfigUseaddr | Unset
        if isinstance(_useaddr, Unset):
            useaddr = UNSET
        else:
            useaddr = OpenVPNClientExportConfigUseaddr(_useaddr)

        useaddr_hostname = d.pop("useaddr_hostname", UNSET)

        _verifyservercn = d.pop("verifyservercn", UNSET)
        verifyservercn: OpenVPNClientExportConfigVerifyservercn | Unset
        if isinstance(_verifyservercn, Unset):
            verifyservercn = UNSET
        else:
            verifyservercn = OpenVPNClientExportConfigVerifyservercn(_verifyservercn)

        blockoutsidedns = d.pop("blockoutsidedns", UNSET)

        legacy = d.pop("legacy", UNSET)

        silent = d.pop("silent", UNSET)

        _bindmode = d.pop("bindmode", UNSET)
        bindmode: OpenVPNClientExportConfigBindmode | Unset
        if isinstance(_bindmode, Unset):
            bindmode = UNSET
        else:
            bindmode = OpenVPNClientExportConfigBindmode(_bindmode)

        usepkcs11 = d.pop("usepkcs11", UNSET)

        usetoken = d.pop("usetoken", UNSET)

        usepass = d.pop("usepass", UNSET)

        _p12encryption = d.pop("p12encryption", UNSET)
        p12encryption: OpenVPNClientExportConfigP12Encryption | Unset
        if isinstance(_p12encryption, Unset):
            p12encryption = UNSET
        else:
            p12encryption = OpenVPNClientExportConfigP12Encryption(_p12encryption)

        useproxy = d.pop("useproxy", UNSET)

        _useproxytype = d.pop("useproxytype", UNSET)
        useproxytype: OpenVPNClientExportConfigUseproxytype | Unset
        if isinstance(_useproxytype, Unset):
            useproxytype = UNSET
        else:
            useproxytype = OpenVPNClientExportConfigUseproxytype(_useproxytype)

        advancedoptions = d.pop("advancedoptions", UNSET)

        post_vpn_open_vpn_client_export_config_endpoint_data_body = cls(
            server=server,
            pkcs11providers=pkcs11providers,
            pkcs11id=pkcs11id,
            pass_=pass_,
            proxyaddr=proxyaddr,
            proxyport=proxyport,
            useproxypass=useproxypass,
            proxyuser=proxyuser,
            proxypass=proxypass,
            useaddr=useaddr,
            useaddr_hostname=useaddr_hostname,
            verifyservercn=verifyservercn,
            blockoutsidedns=blockoutsidedns,
            legacy=legacy,
            silent=silent,
            bindmode=bindmode,
            usepkcs11=usepkcs11,
            usetoken=usetoken,
            usepass=usepass,
            p12encryption=p12encryption,
            useproxy=useproxy,
            useproxytype=useproxytype,
            advancedoptions=advancedoptions,
        )

        post_vpn_open_vpn_client_export_config_endpoint_data_body.additional_properties = d
        return post_vpn_open_vpn_client_export_config_endpoint_data_body

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
