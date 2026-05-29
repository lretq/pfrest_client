from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.i_psec_phase_2_encryption_name import IPsecPhase2EncryptionName
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchVPNIPsecPhase2EncryptionEndpointDataBody")


@_attrs_define
class PatchVPNIPsecPhase2EncryptionEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        name (IPsecPhase2EncryptionName | Unset): The name of the encryption algorithm to use for this P2 encryption
            item.<br>
        keylen (int | Unset): The key length for the encryption algorithm.<br><br>This field is only available when the
            following conditions are met:<br>- `name` must be one of [ aes, aes128gcm, aes192gcm, aes256gcm ]<br>
    """

    parent_id: int
    id: int
    name: IPsecPhase2EncryptionName | Unset = UNSET
    keylen: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        keylen = self.keylen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if keylen is not UNSET:
            field_dict["keylen"] = keylen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        _name = d.pop("name", UNSET)
        name: IPsecPhase2EncryptionName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = IPsecPhase2EncryptionName(_name)

        keylen = d.pop("keylen", UNSET)

        patch_vpni_psec_phase_2_encryption_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            name=name,
            keylen=keylen,
        )

        patch_vpni_psec_phase_2_encryption_endpoint_data_body.additional_properties = d
        return patch_vpni_psec_phase_2_encryption_endpoint_data_body

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
