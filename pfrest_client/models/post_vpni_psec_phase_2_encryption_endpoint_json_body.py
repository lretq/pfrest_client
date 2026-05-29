from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.i_psec_phase_2_encryption_name import IPsecPhase2EncryptionName

T = TypeVar("T", bound="PostVPNIPsecPhase2EncryptionEndpointJsonBody")


@_attrs_define
class PostVPNIPsecPhase2EncryptionEndpointJsonBody:
    """
    Attributes:
        name (IPsecPhase2EncryptionName): The name of the encryption algorithm to use for this P2 encryption item.<br>
        keylen (int): The key length for the encryption algorithm.<br><br>This field is only available when the
            following conditions are met:<br>- `name` must be one of [ aes, aes128gcm, aes192gcm, aes256gcm ]<br>
        parent_id (int): The ID of the parent this object is nested under.
    """

    name: IPsecPhase2EncryptionName
    keylen: int
    parent_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        keylen = self.keylen

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "keylen": keylen,
                "parent_id": parent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = IPsecPhase2EncryptionName(d.pop("name"))

        keylen = d.pop("keylen")

        parent_id = d.pop("parent_id")

        post_vpni_psec_phase_2_encryption_endpoint_json_body = cls(
            name=name,
            keylen=keylen,
            parent_id=parent_id,
        )

        post_vpni_psec_phase_2_encryption_endpoint_json_body.additional_properties = d
        return post_vpni_psec_phase_2_encryption_endpoint_json_body

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
