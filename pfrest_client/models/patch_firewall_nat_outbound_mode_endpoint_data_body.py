from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.outbound_nat_mode_mode import OutboundNATModeMode

T = TypeVar("T", bound="PatchFirewallNATOutboundModeEndpointDataBody")


@_attrs_define
class PatchFirewallNATOutboundModeEndpointDataBody:
    """
    Attributes:
        mode (OutboundNATModeMode): The outbound NAT mode to assign this system. Set to `automatic` to have this system
            automatically generate NAT rules this firewall, `hybrid` to automatically generate NAT rules AND allow manual
            outbound NAT mappings to be assigned, `manual` to prevent the system from automatically generating NAT rules and
            only allow manual outbound NAT mappings, or `disabled` to disable outbound NAT on this system entirely.<br>
    """

    mode: OutboundNATModeMode
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = OutboundNATModeMode(d.pop("mode"))

        patch_firewall_nat_outbound_mode_endpoint_data_body = cls(
            mode=mode,
        )

        patch_firewall_nat_outbound_mode_endpoint_data_body.additional_properties = d
        return patch_firewall_nat_outbound_mode_endpoint_data_body

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
