from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.one_to_one_nat_mapping_ipprotocol import OneToOneNATMappingIpprotocol
from ..models.one_to_one_nat_mapping_natreflection import OneToOneNATMappingNatreflection
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchFirewallNATOneToOneMappingEndpointDataBody")


@_attrs_define
class PatchFirewallNATOneToOneMappingEndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        interface (str | Unset): The interface this 1:1 NAT mapping applies to.<br>
        disabled (bool | Unset): Disables this 1:1 NAT mapping.<br>
        nobinat (bool | Unset): Exclude traffic matching this mapping from a later, more general, mapping.<br>
        natreflection (OneToOneNATMappingNatreflection | Unset): Enables or disables NAT reflection for traffic matching
            this mapping. Set to `null` to use the system default.<br>
        ipprotocol (OneToOneNATMappingIpprotocol | Unset): The IP version this mapping applies to.<br> Default:
            OneToOneNATMappingIpprotocol.INET.
        external (str | Unset): The external IP address or interface for the 1:1 mapping. Valid value options are: an IP
            address. For interface values, the `:ip`  modifier can be appended to the value to use the interface's IP
            address instead of its entire subnet.<br>
        source (str | Unset): The source IP address or subnet that traffic must match to apply this mapping. Valid value
            options are: an existing interface, an IP address, a subnet CIDR, `any`, `l2tp`, `pppoe`. The context of this
            address can be inverted by prefixing the value with `!`. For interface values, the `:ip`  modifier can be
            appended to the value to use the interface's IP address instead of its entire subnet.<br>
        destination (str | Unset): The destination IP address or subnet that traffic must match to apply this mapping.
            Valid value options are: an existing interface, an IP address, a subnet CIDR, an existing alias, `any`, `l2tp`,
            `pppoe`. The context of this address can be inverted by prefixing the value with `!`. For interface values, the
            `:ip`  modifier can be appended to the value to use the interface's IP address instead of its entire subnet.<br>
        descr (str | Unset): A description for this 1:1 NAT mapping<br>
    """

    id: int
    interface: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    nobinat: bool | Unset = UNSET
    natreflection: OneToOneNATMappingNatreflection | Unset = UNSET
    ipprotocol: OneToOneNATMappingIpprotocol | Unset = OneToOneNATMappingIpprotocol.INET
    external: str | Unset = UNSET
    source: str | Unset = UNSET
    destination: str | Unset = UNSET
    descr: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        interface = self.interface

        disabled = self.disabled

        nobinat = self.nobinat

        natreflection: str | Unset = UNSET
        if not isinstance(self.natreflection, Unset):
            natreflection = self.natreflection.value

        ipprotocol: str | Unset = UNSET
        if not isinstance(self.ipprotocol, Unset):
            ipprotocol = self.ipprotocol.value

        external = self.external

        source = self.source

        destination = self.destination

        descr = self.descr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if interface is not UNSET:
            field_dict["interface"] = interface
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if nobinat is not UNSET:
            field_dict["nobinat"] = nobinat
        if natreflection is not UNSET:
            field_dict["natreflection"] = natreflection
        if ipprotocol is not UNSET:
            field_dict["ipprotocol"] = ipprotocol
        if external is not UNSET:
            field_dict["external"] = external
        if source is not UNSET:
            field_dict["source"] = source
        if destination is not UNSET:
            field_dict["destination"] = destination
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        interface = d.pop("interface", UNSET)

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

        external = d.pop("external", UNSET)

        source = d.pop("source", UNSET)

        destination = d.pop("destination", UNSET)

        descr = d.pop("descr", UNSET)

        patch_firewall_nat_one_to_one_mapping_endpoint_data_body = cls(
            id=id,
            interface=interface,
            disabled=disabled,
            nobinat=nobinat,
            natreflection=natreflection,
            ipprotocol=ipprotocol,
            external=external,
            source=source,
            destination=destination,
            descr=descr,
        )

        patch_firewall_nat_one_to_one_mapping_endpoint_data_body.additional_properties = d
        return patch_firewall_nat_one_to_one_mapping_endpoint_data_body

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
