from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.one_to_one_nat_mapping_ipprotocol import OneToOneNATMappingIpprotocol
from ..models.one_to_one_nat_mapping_natreflection import OneToOneNATMappingNatreflection
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutFirewallNATOneToOneMappingsEndpointJsonBodyItem")


@_attrs_define
class PutFirewallNATOneToOneMappingsEndpointJsonBodyItem:
    """
    Attributes:
        interface (str): The interface this 1:1 NAT mapping applies to.<br>
        external (str): The external IP address or interface for the 1:1 mapping. Valid value options are: an IP
            address. For interface values, the `:ip`  modifier can be appended to the value to use the interface's IP
            address instead of its entire subnet.<br>
        source (str): The source IP address or subnet that traffic must match to apply this mapping. Valid value options
            are: an existing interface, an IP address, a subnet CIDR, `any`, `l2tp`, `pppoe`. The context of this address
            can be inverted by prefixing the value with `!`. For interface values, the `:ip`  modifier can be appended to
            the value to use the interface's IP address instead of its entire subnet.<br>
        destination (str): The destination IP address or subnet that traffic must match to apply this mapping. Valid
            value options are: an existing interface, an IP address, a subnet CIDR, an existing alias, `any`, `l2tp`,
            `pppoe`. The context of this address can be inverted by prefixing the value with `!`. For interface values, the
            `:ip`  modifier can be appended to the value to use the interface's IP address instead of its entire subnet.<br>
        disabled (bool | Unset): Disables this 1:1 NAT mapping.<br>
        nobinat (bool | Unset): Exclude traffic matching this mapping from a later, more general, mapping.<br>
        natreflection (OneToOneNATMappingNatreflection | Unset): Enables or disables NAT reflection for traffic matching
            this mapping. Set to `null` to use the system default.<br>
        ipprotocol (OneToOneNATMappingIpprotocol | Unset): The IP version this mapping applies to.<br> Default:
            OneToOneNATMappingIpprotocol.INET.
        descr (str | Unset): A description for this 1:1 NAT mapping<br>
    """

    interface: str
    external: str
    source: str
    destination: str
    disabled: bool | Unset = UNSET
    nobinat: bool | Unset = UNSET
    natreflection: OneToOneNATMappingNatreflection | Unset = UNSET
    ipprotocol: OneToOneNATMappingIpprotocol | Unset = OneToOneNATMappingIpprotocol.INET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface = self.interface

        external = self.external

        source = self.source

        destination = self.destination

        disabled = self.disabled

        nobinat = self.nobinat

        natreflection: str | Unset = UNSET
        if not isinstance(self.natreflection, Unset):
            natreflection = self.natreflection.value

        ipprotocol: str | Unset = UNSET
        if not isinstance(self.ipprotocol, Unset):
            ipprotocol = self.ipprotocol.value

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interface": interface,
                "external": external,
                "source": source,
                "destination": destination,
            }
        )
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if nobinat is not UNSET:
            field_dict["nobinat"] = nobinat
        if natreflection is not UNSET:
            field_dict["natreflection"] = natreflection
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interface = d.pop("interface")

        external = d.pop("external")

        source = d.pop("source")

        destination = d.pop("destination")

        disabled = d.pop("disabled", UNSET)

        nobinat = d.pop("nobinat", UNSET)

        _natreflection = d.pop("natreflection", UNSET)
        natreflection: OneToOneNATMappingNatreflection | Unset
        if isinstance(_natreflection, Unset):
            natreflection = UNSET
        else:
            natreflection = OneToOneNATMappingNatreflection(_natreflection)

        _ipprotocol = d.pop("ipprotocol", UNSET)
        ipprotocol: OneToOneNATMappingIpprotocol | Unset
        if isinstance(_ipprotocol, Unset):
            ipprotocol = UNSET
        else:
            ipprotocol = OneToOneNATMappingIpprotocol(_ipprotocol)

        descr = d.pop("descr", UNSET)

        put_firewall_nat_one_to_one_mappings_endpoint_json_body_item = cls(
            interface=interface,
            external=external,
            source=source,
            destination=destination,
            disabled=disabled,
            nobinat=nobinat,
            natreflection=natreflection,
            ipprotocol=ipprotocol,
            descr=descr,
        )

        put_firewall_nat_one_to_one_mappings_endpoint_json_body_item.additional_properties = d
        return put_firewall_nat_one_to_one_mappings_endpoint_json_body_item

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
