from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.free_radius_client_ip_version import FreeRADIUSClientIpVersion
from ..models.free_radius_client_nastype import FreeRADIUSClientNastype
from ..models.free_radius_client_proto import FreeRADIUSClientProto
from ..types import UNSET, Unset

T = TypeVar("T", bound="FreeRADIUSClient")


@_attrs_define
class FreeRADIUSClient:
    """
    Attributes:
        addr (str | Unset): The IP address or network of the RADIUS client(s) in CIDR notation. This is the IP of the
            NAS (switch, access point, firewall, router, etc.)<br>
        ip_version (FreeRADIUSClientIpVersion | Unset): The IP version of the this Client.<br> Default:
            FreeRADIUSClientIpVersion.IPADDR.
        description (str | Unset): The description for this interface.<br>
        shortname (str | Unset): A short name for the client. This is generally the hostname of the NAS.<br>
        secret (str | Unset): This is the shared secret (password) which the NAS (switch, accesspoint, etc.) needs to
            communicate with the RADIUS server.<br>
        proto (FreeRADIUSClientProto | Unset): The protocol the client uses.<br> Default: FreeRADIUSClientProto.UDP.
        nastype (FreeRADIUSClientNastype | Unset): The NAS type of the client. This is used by checkrad.pl for
            simultaneous use checks.<br> Default: FreeRADIUSClientNastype.OTHER.
        msgauth (bool | Unset): RFC5080 requires Message-Authenticator in Access-Request. But older NAS (switches or
            accesspoints) do not include that.<br>
        maxconn (int | Unset): Takes only effect if you use TCP as protocol. Limits the number of simultaneous TCP
                            connections from a client.<br> Default: 16.
        naslogin (str | Unset): If supported by your NAS, you can use SNMP or finger for simultaneous-use checks instead
            of (s)radutmp file and accounting. Leave empty to choose (s)radutmp.<br>
        naspassword (str | Unset): If supported by your NAS, you can use SNMP or finger for simultaneous-use checks
            instead of (s)radutmp file and accounting. Leave empty to choose (s)radutmp.<br>
    """

    addr: str | Unset = UNSET
    ip_version: FreeRADIUSClientIpVersion | Unset = FreeRADIUSClientIpVersion.IPADDR
    description: str | Unset = UNSET
    shortname: str | Unset = UNSET
    secret: str | Unset = UNSET
    proto: FreeRADIUSClientProto | Unset = FreeRADIUSClientProto.UDP
    nastype: FreeRADIUSClientNastype | Unset = FreeRADIUSClientNastype.OTHER
    msgauth: bool | Unset = UNSET
    maxconn: int | Unset = 16
    naslogin: str | Unset = UNSET
    naspassword: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addr = self.addr

        ip_version: str | Unset = UNSET
        if not isinstance(self.ip_version, Unset):
            ip_version = self.ip_version.value

        description = self.description

        shortname = self.shortname

        secret = self.secret

        proto: str | Unset = UNSET
        if not isinstance(self.proto, Unset):
            proto = self.proto.value

        nastype: str | Unset = UNSET
        if not isinstance(self.nastype, Unset):
            nastype = self.nastype.value

        msgauth = self.msgauth

        maxconn = self.maxconn

        naslogin = self.naslogin

        naspassword = self.naspassword

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addr is not UNSET:
            field_dict["addr"] = addr
        if ip_version is not UNSET:
            field_dict["ip_version"] = ip_version
        if description is not UNSET:
            field_dict["description"] = description
        if shortname is not UNSET:
            field_dict["shortname"] = shortname
        if secret is not UNSET:
            field_dict["secret"] = secret
        if proto is not UNSET:
            field_dict["proto"] = proto
        if nastype is not UNSET:
            field_dict["nastype"] = nastype
        if msgauth is not UNSET:
            field_dict["msgauth"] = msgauth
        if maxconn is not UNSET:
            field_dict["maxconn"] = maxconn
        if naslogin is not UNSET:
            field_dict["naslogin"] = naslogin
        if naspassword is not UNSET:
            field_dict["naspassword"] = naspassword

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        addr = d.pop("addr", UNSET)

        _ip_version = d.pop("ip_version", UNSET)
        ip_version: FreeRADIUSClientIpVersion | Unset
        if isinstance(_ip_version, Unset):
            ip_version = UNSET
        else:
            ip_version = FreeRADIUSClientIpVersion(_ip_version)

        description = d.pop("description", UNSET)

        shortname = d.pop("shortname", UNSET)

        secret = d.pop("secret", UNSET)

        _proto = d.pop("proto", UNSET)
        proto: FreeRADIUSClientProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = FreeRADIUSClientProto(_proto)

        _nastype = d.pop("nastype", UNSET)
        nastype: FreeRADIUSClientNastype | Unset
        if isinstance(_nastype, Unset):
            nastype = UNSET
        else:
            nastype = FreeRADIUSClientNastype(_nastype)

        msgauth = d.pop("msgauth", UNSET)

        maxconn = d.pop("maxconn", UNSET)

        naslogin = d.pop("naslogin", UNSET)

        naspassword = d.pop("naspassword", UNSET)

        free_radius_client = cls(
            addr=addr,
            ip_version=ip_version,
            description=description,
            shortname=shortname,
            secret=secret,
            proto=proto,
            nastype=nastype,
            msgauth=msgauth,
            maxconn=maxconn,
            naslogin=naslogin,
            naspassword=naspassword,
        )

        free_radius_client.additional_properties = d
        return free_radius_client

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
