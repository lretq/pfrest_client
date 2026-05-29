from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.open_vpn_client_export_bindmode import OpenVPNClientExportBindmode
from ..models.open_vpn_client_export_p12_encryption import OpenVPNClientExportP12Encryption
from ..models.open_vpn_client_export_type import OpenVPNClientExportType
from ..models.open_vpn_client_export_useaddr import OpenVPNClientExportUseaddr
from ..models.open_vpn_client_export_useproxypass import OpenVPNClientExportUseproxypass
from ..models.open_vpn_client_export_useproxytype import OpenVPNClientExportUseproxytype
from ..models.open_vpn_client_export_verifyservercn import OpenVPNClientExportVerifyservercn
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostVPNOpenVPNClientExportEndpointJsonBody")


@_attrs_define
class PostVPNOpenVPNClientExportEndpointJsonBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        type_ (OpenVPNClientExportType | Unset): The type of OpenVPN client export to generate. This determines the
            format and content of the export file.<br>
        certref (None | str | Unset): The reference ID of the certificate to use for this OpenVPN client export. This is
            only applicable for OpenVPN servers that require client certificates.<br>
        username (None | str | Unset): The username of the user this client export corresponds to. This is only
            applicable for OpenVPN servers that use the Local Database AND client certificates.<br>
        filename (None | str | Unset): The filename used when exporting the OpenVPN client export. This value cannot be
            changed<br>
        binary_data (None | str | Unset): The binary data of the OpenVPN client export. This is used to store the actual
            exported configuration file content. When the content-type is set to "application/octet-stream", this field will
            contain the data of the OpenVPN client export download.<br>
        server (int | Unset): The VPN ID of the OpenVPN server this client export corresponds to.<br>
        useaddr (OpenVPNClientExportUseaddr | Unset): The method to use for the OpenVPN server address listed in the
            config export.<br> Default: OpenVPNClientExportUseaddr.SERVERADDR.
        useaddr_hostname (str | Unset): The hostname to use for the OpenVPN server address.<br><br>This field is only
            available when the following conditions are met:<br>- `useaddr` must be equal to `'other'`<br>
        verifyservercn (OpenVPNClientExportVerifyservercn | Unset): Verify the server certificate Common Name (CN) when
            the client connects.<br> Default: OpenVPNClientExportVerifyservercn.AUTO.
        blockoutsidedns (bool | Unset): Block access to DNS servers except across OpenVPN while connected, forcing
            clients to use only VPN DNS servers.<br>
        legacy (bool | Unset): Do not include OpenVPN 2.5 and later settings in the client configuration.<br>
        silent (bool | Unset): Create Windows installer for unattended deploy.<br>
        bindmode (OpenVPNClientExportBindmode | Unset): The port binding mode to use. If OpenVPN client binds to the
            default OpenVPN port (1194), two clients may not run concurrently.<br> Default:
            OpenVPNClientExportBindmode.NOBIND.
        usepkcs11 (bool | Unset): Use PKCS#11 storage device (cryptographic token, HSM, smart card) instead of local
            files.<br>
        pkcs11providers (list[str] | Unset): The client local path to the PKCS#11 provider(s) (DLL, module)<br><br>This
            field is only available when the following conditions are met:<br>- `usepkcs11` must be equal to `true`<br>
        pkcs11id (str | Unset): The object's ID on the PKCS#11 device.<br><br>This field is only available when the
            following conditions are met:<br>- `usepkcs11` must be equal to `true`<br>
        usetoken (bool | Unset): Use Microsoft Certificate Storage instead of local files.<br>
        usepass (bool | Unset): Use a password to protect the PKCS#12 file contents or key in Viscosity bundles.<br>
        pass_ (str | Unset): Password used to protect the certificate file contents.<br><br>This field is only available
            when the following conditions are met:<br>- `usepass` must be equal to `true`<br>
        p12encryption (OpenVPNClientExportP12Encryption | Unset): The level of encryption to use when exporting a
            PKCS#12 archive. Encryption support varies by Operating System and program<br> Default:
            OpenVPNClientExportP12Encryption.HIGH.
        useproxy (bool | Unset): Use proxy to communicate with the OpenVPN server.<br>
        useproxytype (OpenVPNClientExportUseproxytype | Unset): The proxy type to use.<br><br>This field is only
            available when the following conditions are met:<br>- `useproxy` must be equal to `true`<br> Default:
            OpenVPNClientExportUseproxytype.HTTP.
        proxyaddr (str | Unset): The IP address or hostname of the proxy server to use.<br><br>This field is only
            available when the following conditions are met:<br>- `useproxy` must be equal to `true`<br>
        proxyport (str | Unset): The port where the proxy server is listening. Valid options are: a TCP/UDP port
            number<br><br>This field is only available when the following conditions are met:<br>- `useproxy` must be equal
            to `true`<br>
        useproxypass (OpenVPNClientExportUseproxypass | Unset): The type of authentication to use for the proxy
            server.<br><br>This field is only available when the following conditions are met:<br>- `useproxy` must be equal
            to `true`<br>
        proxyuser (str | Unset): The username to use to authenticate with the proxy server.<br><br>This field is only
            available when the following conditions are met:<br>- `useproxy` must be equal to `true`<br>- `useproxypass`
            must be one of [ basic, ntlm ]<br>
        proxypass (str | Unset): The password to use to authenticate with the proxy server.<br><br>This field is only
            available when the following conditions are met:<br>- `useproxy` must be equal to `true`<br>- `useproxypass`
            must be one of [ basic, ntlm ]<br>
        advancedoptions (str | Unset): Additional options to add to the OpenVPN client export configuration.<br>
    """

    id: int
    type_: OpenVPNClientExportType | Unset = UNSET
    certref: None | str | Unset = UNSET
    username: None | str | Unset = UNSET
    filename: None | str | Unset = UNSET
    binary_data: None | str | Unset = UNSET
    server: int | Unset = UNSET
    useaddr: OpenVPNClientExportUseaddr | Unset = OpenVPNClientExportUseaddr.SERVERADDR
    useaddr_hostname: str | Unset = UNSET
    verifyservercn: OpenVPNClientExportVerifyservercn | Unset = OpenVPNClientExportVerifyservercn.AUTO
    blockoutsidedns: bool | Unset = UNSET
    legacy: bool | Unset = UNSET
    silent: bool | Unset = UNSET
    bindmode: OpenVPNClientExportBindmode | Unset = OpenVPNClientExportBindmode.NOBIND
    usepkcs11: bool | Unset = UNSET
    pkcs11providers: list[str] | Unset = UNSET
    pkcs11id: str | Unset = UNSET
    usetoken: bool | Unset = UNSET
    usepass: bool | Unset = UNSET
    pass_: str | Unset = UNSET
    p12encryption: OpenVPNClientExportP12Encryption | Unset = OpenVPNClientExportP12Encryption.HIGH
    useproxy: bool | Unset = UNSET
    useproxytype: OpenVPNClientExportUseproxytype | Unset = OpenVPNClientExportUseproxytype.HTTP
    proxyaddr: str | Unset = UNSET
    proxyport: str | Unset = UNSET
    useproxypass: OpenVPNClientExportUseproxypass | Unset = UNSET
    proxyuser: str | Unset = UNSET
    proxypass: str | Unset = UNSET
    advancedoptions: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        certref: None | str | Unset
        if isinstance(self.certref, Unset):
            certref = UNSET
        else:
            certref = self.certref

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        binary_data: None | str | Unset
        if isinstance(self.binary_data, Unset):
            binary_data = UNSET
        else:
            binary_data = self.binary_data

        server = self.server

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

        pkcs11providers: list[str] | Unset = UNSET
        if not isinstance(self.pkcs11providers, Unset):
            pkcs11providers = self.pkcs11providers

        pkcs11id = self.pkcs11id

        usetoken = self.usetoken

        usepass = self.usepass

        pass_ = self.pass_

        p12encryption: str | Unset = UNSET
        if not isinstance(self.p12encryption, Unset):
            p12encryption = self.p12encryption.value

        useproxy = self.useproxy

        useproxytype: str | Unset = UNSET
        if not isinstance(self.useproxytype, Unset):
            useproxytype = self.useproxytype.value

        proxyaddr = self.proxyaddr

        proxyport = self.proxyport

        useproxypass: str | Unset = UNSET
        if not isinstance(self.useproxypass, Unset):
            useproxypass = self.useproxypass.value

        proxyuser = self.proxyuser

        proxypass = self.proxypass

        advancedoptions = self.advancedoptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if certref is not UNSET:
            field_dict["certref"] = certref
        if username is not UNSET:
            field_dict["username"] = username
        if filename is not UNSET:
            field_dict["filename"] = filename
        if binary_data is not UNSET:
            field_dict["binary_data"] = binary_data
        if server is not UNSET:
            field_dict["server"] = server
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
        if pkcs11providers is not UNSET:
            field_dict["pkcs11providers"] = pkcs11providers
        if pkcs11id is not UNSET:
            field_dict["pkcs11id"] = pkcs11id
        if usetoken is not UNSET:
            field_dict["usetoken"] = usetoken
        if usepass is not UNSET:
            field_dict["usepass"] = usepass
        if pass_ is not UNSET:
            field_dict["pass"] = pass_
        if p12encryption is not UNSET:
            field_dict["p12encryption"] = p12encryption
        if useproxy is not UNSET:
            field_dict["useproxy"] = useproxy
        if useproxytype is not UNSET:
            field_dict["useproxytype"] = useproxytype
        if proxyaddr is not UNSET:
            field_dict["proxyaddr"] = proxyaddr
        if proxyport is not UNSET:
            field_dict["proxyport"] = proxyport
        if useproxypass is not UNSET:
            field_dict["useproxypass"] = useproxypass
        if proxyuser is not UNSET:
            field_dict["proxyuser"] = proxyuser
        if proxypass is not UNSET:
            field_dict["proxypass"] = proxypass
        if advancedoptions is not UNSET:
            field_dict["advancedoptions"] = advancedoptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        _type_ = d.pop("type", UNSET)
        type_: OpenVPNClientExportType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OpenVPNClientExportType(_type_)

        def _parse_certref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        certref = _parse_certref(d.pop("certref", UNSET))

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))

        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))

        def _parse_binary_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        binary_data = _parse_binary_data(d.pop("binary_data", UNSET))

        server = d.pop("server", UNSET)

        _useaddr = d.pop("useaddr", UNSET)
        useaddr: OpenVPNClientExportUseaddr | Unset
        if isinstance(_useaddr, Unset):
            useaddr = UNSET
        else:
            useaddr = OpenVPNClientExportUseaddr(_useaddr)

        useaddr_hostname = d.pop("useaddr_hostname", UNSET)

        _verifyservercn = d.pop("verifyservercn", UNSET)
        verifyservercn: OpenVPNClientExportVerifyservercn | Unset
        if isinstance(_verifyservercn, Unset):
            verifyservercn = UNSET
        else:
            verifyservercn = OpenVPNClientExportVerifyservercn(_verifyservercn)

        blockoutsidedns = d.pop("blockoutsidedns", UNSET)

        legacy = d.pop("legacy", UNSET)

        silent = d.pop("silent", UNSET)

        _bindmode = d.pop("bindmode", UNSET)
        bindmode: OpenVPNClientExportBindmode | Unset
        if isinstance(_bindmode, Unset):
            bindmode = UNSET
        else:
            bindmode = OpenVPNClientExportBindmode(_bindmode)

        usepkcs11 = d.pop("usepkcs11", UNSET)

        pkcs11providers = cast(list[str], d.pop("pkcs11providers", UNSET))

        pkcs11id = d.pop("pkcs11id", UNSET)

        usetoken = d.pop("usetoken", UNSET)

        usepass = d.pop("usepass", UNSET)

        pass_ = d.pop("pass", UNSET)

        _p12encryption = d.pop("p12encryption", UNSET)
        p12encryption: OpenVPNClientExportP12Encryption | Unset
        if isinstance(_p12encryption, Unset):
            p12encryption = UNSET
        else:
            p12encryption = OpenVPNClientExportP12Encryption(_p12encryption)

        useproxy = d.pop("useproxy", UNSET)

        _useproxytype = d.pop("useproxytype", UNSET)
        useproxytype: OpenVPNClientExportUseproxytype | Unset
        if isinstance(_useproxytype, Unset):
            useproxytype = UNSET
        else:
            useproxytype = OpenVPNClientExportUseproxytype(_useproxytype)

        proxyaddr = d.pop("proxyaddr", UNSET)

        proxyport = d.pop("proxyport", UNSET)

        _useproxypass = d.pop("useproxypass", UNSET)
        useproxypass: OpenVPNClientExportUseproxypass | Unset
        if isinstance(_useproxypass, Unset):
            useproxypass = UNSET
        else:
            useproxypass = OpenVPNClientExportUseproxypass(_useproxypass)

        proxyuser = d.pop("proxyuser", UNSET)

        proxypass = d.pop("proxypass", UNSET)

        advancedoptions = d.pop("advancedoptions", UNSET)

        post_vpn_open_vpn_client_export_endpoint_json_body = cls(
            id=id,
            type_=type_,
            certref=certref,
            username=username,
            filename=filename,
            binary_data=binary_data,
            server=server,
            useaddr=useaddr,
            useaddr_hostname=useaddr_hostname,
            verifyservercn=verifyservercn,
            blockoutsidedns=blockoutsidedns,
            legacy=legacy,
            silent=silent,
            bindmode=bindmode,
            usepkcs11=usepkcs11,
            pkcs11providers=pkcs11providers,
            pkcs11id=pkcs11id,
            usetoken=usetoken,
            usepass=usepass,
            pass_=pass_,
            p12encryption=p12encryption,
            useproxy=useproxy,
            useproxytype=useproxytype,
            proxyaddr=proxyaddr,
            proxyport=proxyport,
            useproxypass=useproxypass,
            proxyuser=proxyuser,
            proxypass=proxypass,
            advancedoptions=advancedoptions,
        )

        post_vpn_open_vpn_client_export_endpoint_json_body.additional_properties = d
        return post_vpn_open_vpn_client_export_endpoint_json_body

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
