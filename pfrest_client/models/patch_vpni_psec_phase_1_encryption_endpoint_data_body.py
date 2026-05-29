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

T = TypeVar("T", bound="PatchVPNIPsecPhase1EncryptionEndpointDataBody")


@_attrs_define
class PatchVPNIPsecPhase1EncryptionEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        encryption_algorithm_name (IPsecPhase1EncryptionEncryptionAlgorithmName | Unset): The name of the encryption
            algorithm to use for this P1 encryption item.<br>
        encryption_algorithm_keylen (int | Unset): The key length for the encryption algorithm.<br><br>This field is
            only available when the following conditions are met:<br>- `encryption_algorithm_name` must be one of [ aes,
            aes128gcm, aes192gcm, aes256gcm ]<br>
        hash_algorithm (IPsecPhase1EncryptionHashAlgorithm | Unset): The hash algorithm to use for this P1 encryption
            item.<br>
        dhgroup (IPsecPhase1EncryptionDhgroup | Unset): The Diffie-Hellman (DH) group to use for this P1 encryption
            item.<br>
        prf_algorithm (IPsecPhase1EncryptionPrfAlgorithm | Unset): The PRF algorithm to use for this P1 encryption item.
            This value has no affect unless the P1 entry has PRF enabled.<br> Default:
            IPsecPhase1EncryptionPrfAlgorithm.SHA256.
    """

    parent_id: int
    id: int
    encryption_algorithm_name: IPsecPhase1EncryptionEncryptionAlgorithmName | Unset = UNSET
    encryption_algorithm_keylen: int | Unset = UNSET
    hash_algorithm: IPsecPhase1EncryptionHashAlgorithm | Unset = UNSET
    dhgroup: IPsecPhase1EncryptionDhgroup | Unset = UNSET
    prf_algorithm: IPsecPhase1EncryptionPrfAlgorithm | Unset = IPsecPhase1EncryptionPrfAlgorithm.SHA256
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        encryption_algorithm_name: str | Unset = UNSET
        if not isinstance(self.encryption_algorithm_name, Unset):
            encryption_algorithm_name = self.encryption_algorithm_name.value

        encryption_algorithm_keylen = self.encryption_algorithm_keylen

        hash_algorithm: str | Unset = UNSET
        if not isinstance(self.hash_algorithm, Unset):
            hash_algorithm = self.hash_algorithm.value

        dhgroup: int | Unset = UNSET
        if not isinstance(self.dhgroup, Unset):
            dhgroup = self.dhgroup.value

        prf_algorithm: str | Unset = UNSET
        if not isinstance(self.prf_algorithm, Unset):
            prf_algorithm = self.prf_algorithm.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if encryption_algorithm_name is not UNSET:
            field_dict["encryption_algorithm_name"] = encryption_algorithm_name
        if encryption_algorithm_keylen is not UNSET:
            field_dict["encryption_algorithm_keylen"] = encryption_algorithm_keylen
        if hash_algorithm is not UNSET:
            field_dict["hash_algorithm"] = hash_algorithm
        if dhgroup is not UNSET:
            field_dict["dhgroup"] = dhgroup
        if prf_algorithm is not UNSET:
            field_dict["prf_algorithm"] = prf_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        _encryption_algorithm_name = d.pop("encryption_algorithm_name", UNSET)
        encryption_algorithm_name: IPsecPhase1EncryptionEncryptionAlgorithmName | Unset
        if isinstance(_encryption_algorithm_name, Unset):
            encryption_algorithm_name = UNSET
        else:
            encryption_algorithm_name = IPsecPhase1EncryptionEncryptionAlgorithmName(_encryption_algorithm_name)

        encryption_algorithm_keylen = d.pop("encryption_algorithm_keylen", UNSET)

        _hash_algorithm = d.pop("hash_algorithm", UNSET)
        hash_algorithm: IPsecPhase1EncryptionHashAlgorithm | Unset
        if isinstance(_hash_algorithm, Unset):
            hash_algorithm = UNSET
        else:
            hash_algorithm = IPsecPhase1EncryptionHashAlgorithm(_hash_algorithm)

        _dhgroup = d.pop("dhgroup", UNSET)
        dhgroup: IPsecPhase1EncryptionDhgroup | Unset
        if isinstance(_dhgroup, Unset):
            dhgroup = UNSET
        else:
            dhgroup = IPsecPhase1EncryptionDhgroup(_dhgroup)

        _prf_algorithm = d.pop("prf_algorithm", UNSET)
        prf_algorithm: IPsecPhase1EncryptionPrfAlgorithm | Unset
        if isinstance(_prf_algorithm, Unset):
            prf_algorithm = UNSET
        else:
            prf_algorithm = IPsecPhase1EncryptionPrfAlgorithm(_prf_algorithm)

        patch_vpni_psec_phase_1_encryption_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            encryption_algorithm_name=encryption_algorithm_name,
            encryption_algorithm_keylen=encryption_algorithm_keylen,
            hash_algorithm=hash_algorithm,
            dhgroup=dhgroup,
            prf_algorithm=prf_algorithm,
        )

        patch_vpni_psec_phase_1_encryption_endpoint_data_body.additional_properties = d
        return patch_vpni_psec_phase_1_encryption_endpoint_data_body

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
