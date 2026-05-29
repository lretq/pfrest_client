from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.certificate_pkcs12_export_encryption import CertificatePKCS12ExportEncryption
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSystemCertificatePKCS12ExportEndpointJsonBody")


@_attrs_define
class PostSystemCertificatePKCS12ExportEndpointJsonBody:
    """
    Attributes:
        certref (str): The Certificate to export as a PKCS12 file.<br>
        encryption (CertificatePKCS12ExportEncryption | Unset): The level of encryption to use when exporting the
            PKCS#12 archive.<br> Default: CertificatePKCS12ExportEncryption.HIGH.
        passphrase (str | Unset): The passphrase to use when exporting the PKCS#12 archive. Leave empty for no
            passphrase.<br>
        filename (None | str | Unset): The filename used when exporting the PKCS#12 archive. This value cannot be
            changed and will always be certificate refid with the .p12 extension.<br>
        binary_data (None | str | Unset): The PKCS#12 archive binary data. This value cannot be changed.<br>
    """

    certref: str
    encryption: CertificatePKCS12ExportEncryption | Unset = CertificatePKCS12ExportEncryption.HIGH
    passphrase: str | Unset = UNSET
    filename: None | str | Unset = UNSET
    binary_data: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certref = self.certref

        encryption: str | Unset = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.value

        passphrase = self.passphrase

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        binary_data: None | str | Unset
        if isinstance(self.binary_data, Unset):
            binary_data = UNSET
        else:
            binary_data = self.binary_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certref": certref,
            }
        )
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase
        if filename is not UNSET:
            field_dict["filename"] = filename
        if binary_data is not UNSET:
            field_dict["binary_data"] = binary_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certref = d.pop("certref")

        _encryption = d.pop("encryption", UNSET)
        encryption: CertificatePKCS12ExportEncryption | Unset
        if isinstance(_encryption, Unset):
            encryption = UNSET
        else:
            encryption = CertificatePKCS12ExportEncryption(_encryption)

        passphrase = d.pop("passphrase", UNSET)

        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))

        def _parse_binary_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        binary_data = _parse_binary_data(d.pop("binary_data", UNSET))

        post_system_certificate_pkcs12_export_endpoint_json_body = cls(
            certref=certref,
            encryption=encryption,
            passphrase=passphrase,
            filename=filename,
            binary_data=binary_data,
        )

        post_system_certificate_pkcs12_export_endpoint_json_body.additional_properties = d
        return post_system_certificate_pkcs12_export_endpoint_json_body

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
