from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dns_resolver_settings_python_order import DNSResolverSettingsPythonOrder
from ..models.dns_resolver_settings_system_domain_local_zone_type import DNSResolverSettingsSystemDomainLocalZoneType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesDNSResolverSettingsEndpointDataBody")


@_attrs_define
class PatchServicesDNSResolverSettingsEndpointDataBody:
    """
    Attributes:
        sslcertref (str): The SSL/TLS certificate to use for the DNS Resolver service.<br><br>This field is only
            available when the following conditions are met:<br>- `enablessl` must be equal to `true`<br>
        enable (bool | Unset): Enables or disables the DNS Resolver service.<br>
        port (str | Unset): The port on which the DNS Resolver service listens. Valid options are: a TCP/UDP port
            number<br> Default: '53'.
        enablessl (bool | Unset): Enables or disables SSL/TLS for the DNS Resolver service.<br>
        tlsport (str | Unset): The port on which the DNS Resolver service listens for SSL/TLS connections. Valid options
            are: a TCP/UDP port number<br><br>This field is only available when the following conditions are met:<br>-
            `enablessl` must be equal to `true`<br> Default: '853'.
        active_interface (list[str] | Unset): The interface on which the DNS Resolver service listens for DNS queries.
            Set empty value ".
                            "to listen on all interfaces.<br>
        outgoing_interface (list[str] | Unset): The interface on which the DNS Resolver service sends outgoing DNS
            queries. Set empty value ".
                            "to use any interface.<br>
        strictout (bool | Unset): Enables or disables sending recursive queries if none of the selected Outgoing Network
            ".
                            "Interfaces are available.<br>
        system_domain_local_zone_type (DNSResolverSettingsSystemDomainLocalZoneType | Unset): The type of local zone
            used for the system domain.<br> Default: DNSResolverSettingsSystemDomainLocalZoneType.TRANSPARENT.
        dnssec (bool | Unset): Enables or disables DNSSEC validation.<br>
        python (bool | Unset): Enables or disables the Python module.<br>
        python_order (DNSResolverSettingsPythonOrder | Unset): The order in which the Python module is
            loaded.<br><br>This field is only available when the following conditions are met:<br>- `python` must be equal
            to `true`<br> Default: DNSResolverSettingsPythonOrder.PRE_VALIDATOR.
        python_script (str | Unset): The Python module to utilize.<br><br>This field is only available when the
            following conditions are met:<br>- `python` must be equal to `true`<br>
        forwarding (bool | Unset): Enables or disables DNS Resolver forwarding mode.<br>
        regdhcp (bool | Unset): Enables or disables registering DHCP leases in the DNS Resolver service.<br>
        regdhcpstatic (bool | Unset): Enables or disables registering static DHCP mappings in the DNS Resolver
            service.<br>
        regovpnclients (bool | Unset): Enables or disables registering OpenVPN clients in the DNS Resolver service.<br>
        custom_options (str | Unset): Custom options to add to the DNS Resolver configuration.<br>
    """

    sslcertref: str
    enable: bool | Unset = UNSET
    port: str | Unset = "53"
    enablessl: bool | Unset = UNSET
    tlsport: str | Unset = "853"
    active_interface: list[str] | Unset = UNSET
    outgoing_interface: list[str] | Unset = UNSET
    strictout: bool | Unset = UNSET
    system_domain_local_zone_type: DNSResolverSettingsSystemDomainLocalZoneType | Unset = (
        DNSResolverSettingsSystemDomainLocalZoneType.TRANSPARENT
    )
    dnssec: bool | Unset = UNSET
    python: bool | Unset = UNSET
    python_order: DNSResolverSettingsPythonOrder | Unset = DNSResolverSettingsPythonOrder.PRE_VALIDATOR
    python_script: str | Unset = UNSET
    forwarding: bool | Unset = UNSET
    regdhcp: bool | Unset = UNSET
    regdhcpstatic: bool | Unset = UNSET
    regovpnclients: bool | Unset = UNSET
    custom_options: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sslcertref = self.sslcertref

        enable = self.enable

        port = self.port

        enablessl = self.enablessl

        tlsport = self.tlsport

        active_interface: list[str] | Unset = UNSET
        if not isinstance(self.active_interface, Unset):
            active_interface = self.active_interface

        outgoing_interface: list[str] | Unset = UNSET
        if not isinstance(self.outgoing_interface, Unset):
            outgoing_interface = self.outgoing_interface

        strictout = self.strictout

        system_domain_local_zone_type: str | Unset = UNSET
        if not isinstance(self.system_domain_local_zone_type, Unset):
            system_domain_local_zone_type = self.system_domain_local_zone_type.value

        dnssec = self.dnssec

        python = self.python

        python_order: str | Unset = UNSET
        if not isinstance(self.python_order, Unset):
            python_order = self.python_order.value

        python_script = self.python_script

        forwarding = self.forwarding

        regdhcp = self.regdhcp

        regdhcpstatic = self.regdhcpstatic

        regovpnclients = self.regovpnclients

        custom_options = self.custom_options

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sslcertref": sslcertref,
            }
        )
        if enable is not UNSET:
            field_dict["enable"] = enable
        if port is not UNSET:
            field_dict["port"] = port
        if enablessl is not UNSET:
            field_dict["enablessl"] = enablessl
        if tlsport is not UNSET:
            field_dict["tlsport"] = tlsport
        if active_interface is not UNSET:
            field_dict["active_interface"] = active_interface
        if outgoing_interface is not UNSET:
            field_dict["outgoing_interface"] = outgoing_interface
        if strictout is not UNSET:
            field_dict["strictout"] = strictout
        if system_domain_local_zone_type is not UNSET:
            field_dict["system_domain_local_zone_type"] = system_domain_local_zone_type
        if dnssec is not UNSET:
            field_dict["dnssec"] = dnssec
        if python is not UNSET:
            field_dict["python"] = python
        if python_order is not UNSET:
            field_dict["python_order"] = python_order
        if python_script is not UNSET:
            field_dict["python_script"] = python_script
        if forwarding is not UNSET:
            field_dict["forwarding"] = forwarding
        if regdhcp is not UNSET:
            field_dict["regdhcp"] = regdhcp
        if regdhcpstatic is not UNSET:
            field_dict["regdhcpstatic"] = regdhcpstatic
        if regovpnclients is not UNSET:
            field_dict["regovpnclients"] = regovpnclients
        if custom_options is not UNSET:
            field_dict["custom_options"] = custom_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sslcertref = d.pop("sslcertref")

        enable = d.pop("enable", UNSET)

        port = d.pop("port", UNSET)

        enablessl = d.pop("enablessl", UNSET)

        tlsport = d.pop("tlsport", UNSET)

        active_interface = cast(list[str], d.pop("active_interface", UNSET))

        outgoing_interface = cast(list[str], d.pop("outgoing_interface", UNSET))

        strictout = d.pop("strictout", UNSET)

        _system_domain_local_zone_type = d.pop("system_domain_local_zone_type", UNSET)
        system_domain_local_zone_type: DNSResolverSettingsSystemDomainLocalZoneType | Unset
        if isinstance(_system_domain_local_zone_type, Unset):
            system_domain_local_zone_type = UNSET
        else:
            system_domain_local_zone_type = DNSResolverSettingsSystemDomainLocalZoneType(_system_domain_local_zone_type)

        dnssec = d.pop("dnssec", UNSET)

        python = d.pop("python", UNSET)

        _python_order = d.pop("python_order", UNSET)
        python_order: DNSResolverSettingsPythonOrder | Unset
        if isinstance(_python_order, Unset):
            python_order = UNSET
        else:
            python_order = DNSResolverSettingsPythonOrder(_python_order)

        python_script = d.pop("python_script", UNSET)

        forwarding = d.pop("forwarding", UNSET)

        regdhcp = d.pop("regdhcp", UNSET)

        regdhcpstatic = d.pop("regdhcpstatic", UNSET)

        regovpnclients = d.pop("regovpnclients", UNSET)

        custom_options = d.pop("custom_options", UNSET)

        patch_services_dns_resolver_settings_endpoint_data_body = cls(
            sslcertref=sslcertref,
            enable=enable,
            port=port,
            enablessl=enablessl,
            tlsport=tlsport,
            active_interface=active_interface,
            outgoing_interface=outgoing_interface,
            strictout=strictout,
            system_domain_local_zone_type=system_domain_local_zone_type,
            dnssec=dnssec,
            python=python,
            python_order=python_order,
            python_script=python_script,
            forwarding=forwarding,
            regdhcp=regdhcp,
            regdhcpstatic=regdhcpstatic,
            regovpnclients=regovpnclients,
            custom_options=custom_options,
        )

        patch_services_dns_resolver_settings_endpoint_data_body.additional_properties = d
        return patch_services_dns_resolver_settings_endpoint_data_body

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
