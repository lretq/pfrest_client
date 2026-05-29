from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.i_psec_phase_1_encryption_dhgroup import IPsecPhase1EncryptionDhgroup
from ..models.i_psec_phase_1_encryption_encryption_algorithm_name import IPsecPhase1EncryptionEncryptionAlgorithmName
from ..models.i_psec_phase_1_encryption_hash_algorithm import IPsecPhase1EncryptionHashAlgorithm
from ..models.i_psec_phase_1_encryption_prf_algorithm import IPsecPhase1EncryptionPrfAlgorithm
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostVPNIPsecPhase1EncryptionEndpointJsonBody")


@_attrs_define
class PostVPNIPsecPhase1EncryptionEndpointJsonBody:
    """
    Attributes:
        encryption_algorithm_name (IPsecPhase1EncryptionEncryptionAlgorithmName): The name of the encryption algorithm
            to use for this P1 encryption item.<br>
        encryption_algorithm_keylen (int): The key length for the encryption algorithm.<br><br>This field is only
            available when the following conditions are met:<br>- `encryption_algorithm_name` must be one of [ aes,
            aes128gcm, aes192gcm, aes256gcm ]<br>
        hash_algorithm (IPsecPhase1EncryptionHashAlgorithm): The hash algorithm to use for this P1 encryption item.<br>
        dhgroup (IPsecPhase1EncryptionDhgroup): The Diffie-Hellman (DH) group to use for this P1 encryption item.<br>
        parent_id (int): The ID of the parent this object is nested under.
        prf_algorithm (IPsecPhase1EncryptionPrfAlgorithm | Unset): The PRF algorithm to use for this P1 encryption item.
            This value has no affect unless the P1 entry has PRF enabled.<br> Default:
            IPsecPhase1EncryptionPrfAlgorithm.SHA256.
    """

    encryption_algorithm_name: IPsecPhase1EncryptionEncryptionAlgorithmName
    encryption_algorithm_keylen: int
    hash_algorithm: IPsecPhase1EncryptionHashAlgorithm
    dhgroup: IPsecPhase1EncryptionDhgroup
    parent_id: int
    prf_algorithm: IPsecPhase1EncryptionPrfAlgorithm | Unset = IPsecPhase1EncryptionPrfAlgorithm.SHA256
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        encryption_algorithm_name = self.encryption_algorithm_name.value

        encryption_algorithm_keylen = self.encryption_algorithm_keylen

        hash_algorithm = self.hash_algorithm.value

        dhgroup = self.dhgroup.value

        parent_id = self.parent_id

        prf_algorithm: str | Unset = UNSET
        if not isinstance(self.prf_algorithm, Unset):
            prf_algorithm = self.prf_algorithm.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "encryption_algorithm_name": encryption_algorithm_name,
                "encryption_algorithm_keylen": encryption_algorithm_keylen,
                "hash_algorithm": hash_algorithm,
                "dhgroup": dhgroup,
                "parent_id": parent_id,
            }
        )
        if prf_algorithm is not UNSET:
            field_dict["prf_algorithm"] = prf_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        encryption_algorithm_name = IPsecPhase1EncryptionEncryptionAlgorithmName(d.pop("encryption_algorithm_name"))

        encryption_algorithm_keylen = d.pop("encryption_algorithm_keylen")

        hash_algorithm = IPsecPhase1EncryptionHashAlgorithm(d.pop("hash_algorithm"))

        dhgroup = IPsecPhase1EncryptionDhgroup(d.pop("dhgroup"))

        parent_id = d.pop("parent_id")

        _prf_algorithm = d.pop("prf_algorithm", UNSET)
        prf_algorithm: IPsecPhase1EncryptionPrfAlgorithm | Unset
        if isinstance(_prf_algorithm, Unset):
            prf_algorithm = UNSET
        else:
            prf_algorithm = IPsecPhase1EncryptionPrfAlgorithm(_prf_algorithm)

        post_vpni_psec_phase_1_encryption_endpoint_json_body = cls(
            encryption_algorithm_name=encryption_algorithm_name,
            encryption_algorithm_keylen=encryption_algorithm_keylen,
            hash_algorithm=hash_algorithm,
            dhgroup=dhgroup,
            parent_id=parent_id,
            prf_algorithm=prf_algorithm,
        )

        post_vpni_psec_phase_1_encryption_endpoint_json_body.additional_properties = d
        return post_vpni_psec_phase_1_encryption_endpoint_json_body

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
