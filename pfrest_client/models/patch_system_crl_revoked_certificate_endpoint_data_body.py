from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.certificate_revocation_list_revoked_certificate_reason import (
    CertificateRevocationListRevokedCertificateReason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchSystemCRLRevokedCertificateEndpointDataBody")


@_attrs_define
class PatchSystemCRLRevokedCertificateEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        certref (str | Unset): The reference ID of the certificate to be revoked<br><br>This field is only available
            when the following conditions are met:<br>- `serial` must be equal to `NULL`<br>
        serial (None | str | Unset): The serial number of the certificate to be revoked.<br>
        reason (CertificateRevocationListRevokedCertificateReason | Unset): The CRL reason for revocation code.<br>
        revoke_time (int | Unset): The unix timestamp of when the certificate was revoked.<br>
        caref (None | str | Unset): The unique ID of the CA that signed the revoked certificate.<br>
        descr (None | str | Unset): The unique name/description for this CRL.<br>
        type_ (None | str | Unset): The type of the certificate to be revoked.<br>
        crt (None | str | Unset): The X509 certificate string.<br>
        prv (None | str | Unset): The X509 private key string.<br>
    """

    parent_id: int
    id: int
    certref: str | Unset = UNSET
    serial: None | str | Unset = UNSET
    reason: CertificateRevocationListRevokedCertificateReason | Unset = UNSET
    revoke_time: int | Unset = UNSET
    caref: None | str | Unset = UNSET
    descr: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    crt: None | str | Unset = UNSET
    prv: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        certref = self.certref

        serial: None | str | Unset
        if isinstance(self.serial, Unset):
            serial = UNSET
        else:
            serial = self.serial

        reason: int | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        revoke_time = self.revoke_time

        caref: None | str | Unset
        if isinstance(self.caref, Unset):
            caref = UNSET
        else:
            caref = self.caref

        descr: None | str | Unset
        if isinstance(self.descr, Unset):
            descr = UNSET
        else:
            descr = self.descr

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        crt: None | str | Unset
        if isinstance(self.crt, Unset):
            crt = UNSET
        else:
            crt = self.crt

        prv: None | str | Unset
        if isinstance(self.prv, Unset):
            prv = UNSET
        else:
            prv = self.prv

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if certref is not UNSET:
            field_dict["certref"] = certref
        if serial is not UNSET:
            field_dict["serial"] = serial
        if reason is not UNSET:
            field_dict["reason"] = reason
        if revoke_time is not UNSET:
            field_dict["revoke_time"] = revoke_time
        if caref is not UNSET:
            field_dict["caref"] = caref
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type_ is not UNSET:
            field_dict["type"] = type_
        if crt is not UNSET:
            field_dict["crt"] = crt
        if prv is not UNSET:
            field_dict["prv"] = prv

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        certref = d.pop("certref", UNSET)

        def _parse_serial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial = _parse_serial(d.pop("serial", UNSET))

        _reason = d.pop("reason", UNSET)
        reason: CertificateRevocationListRevokedCertificateReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = CertificateRevocationListRevokedCertificateReason(_reason)

        revoke_time = d.pop("revoke_time", UNSET)

        def _parse_caref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caref = _parse_caref(d.pop("caref", UNSET))

        def _parse_descr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        descr = _parse_descr(d.pop("descr", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_crt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        crt = _parse_crt(d.pop("crt", UNSET))

        def _parse_prv(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prv = _parse_prv(d.pop("prv", UNSET))

        patch_system_crl_revoked_certificate_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            certref=certref,
            serial=serial,
            reason=reason,
            revoke_time=revoke_time,
            caref=caref,
            descr=descr,
            type_=type_,
            crt=crt,
            prv=prv,
        )

        patch_system_crl_revoked_certificate_endpoint_data_body.additional_properties = d
        return patch_system_crl_revoked_certificate_endpoint_data_body

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
