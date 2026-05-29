from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.i_psec_phase_2_encryption_name import IPsecPhase2EncryptionName

T = TypeVar("T", bound="IPsecPhase2EncryptionAlgorithmOptionItem")


@_attrs_define
class IPsecPhase2EncryptionAlgorithmOptionItem:
    """
    Attributes:
        name (IPsecPhase2EncryptionName): The name of the encryption algorithm to use for this P2 encryption item.<br>
        keylen (int): The key length for the encryption algorithm.<br><br>This field is only available when the
            following conditions are met:<br>- `name` must be one of [ aes, aes128gcm, aes192gcm, aes256gcm ]<br>
    """

    name: IPsecPhase2EncryptionName
    keylen: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        keylen = self.keylen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "keylen": keylen,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = IPsecPhase2EncryptionName(d.pop("name"))

        keylen = d.pop("keylen")

        i_psec_phase_2_encryption_algorithm_option_item = cls(
            name=name,
            keylen=keylen,
        )

        i_psec_phase_2_encryption_algorithm_option_item.additional_properties = d
        return i_psec_phase_2_encryption_algorithm_option_item

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
