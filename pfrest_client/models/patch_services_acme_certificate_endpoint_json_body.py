from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acme_certificate_keylength import ACMECertificateKeylength
from ..models.acme_certificate_status import ACMECertificateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acme_certificate_a_actionlist_item import ACMECertificateAActionlistItem
    from ..models.acme_certificate_a_domainlist_item import ACMECertificateADomainlistItem


T = TypeVar("T", bound="PatchServicesACMECertificateEndpointJsonBody")


@_attrs_define
class PatchServicesACMECertificateEndpointJsonBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        name (str | Unset): The name of the ACME certificate.<br>
        descr (str | Unset): A description of the ACME certificate.<br>
        status (ACMECertificateStatus | Unset): The activation status of the ACME certificate.<br> Default:
            ACMECertificateStatus.ACTIVE.
        acmeaccount (str | Unset): The ACME account key to use for the ACME certificate.<br>
        keylength (ACMECertificateKeylength | Unset): The length of the private key to use for the ACME certificate.<br>
            Default: ACMECertificateKeylength.VALUE_0.
        keypaste (str | Unset): The custom private key to use for the ACME certificate.<br><br>This field is only
            available when the following conditions are met:<br>- `keylength` must be equal to `'custom'`<br>
        preferredchain (None | str | Unset): The preferred certificate chain to use for the ACME certificate.<br>
        oscpstaple (bool | Unset): Whether to enable OCSP Stapling for the ACME certificate.<br>
        dnssleep (int | None | Unset): The number of seconds to wait for DNS propagation before requesting
            verification.<br>
        renewafter (int | Unset): The number of days before expiration to renew the ACME certificate.<br> Default: 60.
        a_domainlist (list[ACMECertificateADomainlistItem] | Unset): The list of domain verifications  to include in the
            ACME certificate.<br>
        a_actionlist (list[ACMECertificateAActionlistItem] | Unset): The list of actions to perform on the ACME
            certificate after being issued/renewed.<br>
    """

    id: int
    name: str | Unset = UNSET
    descr: str | Unset = UNSET
    status: ACMECertificateStatus | Unset = ACMECertificateStatus.ACTIVE
    acmeaccount: str | Unset = UNSET
    keylength: ACMECertificateKeylength | Unset = ACMECertificateKeylength.VALUE_0
    keypaste: str | Unset = UNSET
    preferredchain: None | str | Unset = UNSET
    oscpstaple: bool | Unset = UNSET
    dnssleep: int | None | Unset = UNSET
    renewafter: int | Unset = 60
    a_domainlist: list[ACMECertificateADomainlistItem] | Unset = UNSET
    a_actionlist: list[ACMECertificateAActionlistItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        descr = self.descr

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        acmeaccount = self.acmeaccount

        keylength: str | Unset = UNSET
        if not isinstance(self.keylength, Unset):
            keylength = self.keylength.value

        keypaste = self.keypaste

        preferredchain: None | str | Unset
        if isinstance(self.preferredchain, Unset):
            preferredchain = UNSET
        else:
            preferredchain = self.preferredchain

        oscpstaple = self.oscpstaple

        dnssleep: int | None | Unset
        if isinstance(self.dnssleep, Unset):
            dnssleep = UNSET
        else:
            dnssleep = self.dnssleep

        renewafter = self.renewafter

        a_domainlist: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.a_domainlist, Unset):
            a_domainlist = []
            for a_domainlist_item_data in self.a_domainlist:
                a_domainlist_item = a_domainlist_item_data.to_dict()
                a_domainlist.append(a_domainlist_item)

        a_actionlist: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.a_actionlist, Unset):
            a_actionlist = []
            for a_actionlist_item_data in self.a_actionlist:
                a_actionlist_item = a_actionlist_item_data.to_dict()
                a_actionlist.append(a_actionlist_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if descr is not UNSET:
            field_dict["descr"] = descr
        if status is not UNSET:
            field_dict["status"] = status
        if acmeaccount is not UNSET:
            field_dict["acmeaccount"] = acmeaccount
        if keylength is not UNSET:
            field_dict["keylength"] = keylength
        if keypaste is not UNSET:
            field_dict["keypaste"] = keypaste
        if preferredchain is not UNSET:
            field_dict["preferredchain"] = preferredchain
        if oscpstaple is not UNSET:
            field_dict["oscpstaple"] = oscpstaple
        if dnssleep is not UNSET:
            field_dict["dnssleep"] = dnssleep
        if renewafter is not UNSET:
            field_dict["renewafter"] = renewafter
        if a_domainlist is not UNSET:
            field_dict["a_domainlist"] = a_domainlist
        if a_actionlist is not UNSET:
            field_dict["a_actionlist"] = a_actionlist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acme_certificate_a_actionlist_item import ACMECertificateAActionlistItem
        from ..models.acme_certificate_a_domainlist_item import ACMECertificateADomainlistItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        descr = d.pop("descr", UNSET)

        _status = d.pop("status", UNSET)
        status: ACMECertificateStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ACMECertificateStatus(_status)

        acmeaccount = d.pop("acmeaccount", UNSET)

        _keylength = d.pop("keylength", UNSET)
        keylength: ACMECertificateKeylength | Unset
        if isinstance(_keylength, Unset):
            keylength = UNSET
        else:
            keylength = ACMECertificateKeylength(_keylength)

        keypaste = d.pop("keypaste", UNSET)

        def _parse_preferredchain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferredchain = _parse_preferredchain(d.pop("preferredchain", UNSET))

        oscpstaple = d.pop("oscpstaple", UNSET)

        def _parse_dnssleep(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dnssleep = _parse_dnssleep(d.pop("dnssleep", UNSET))

        renewafter = d.pop("renewafter", UNSET)

        _a_domainlist = d.pop("a_domainlist", UNSET)
        a_domainlist: list[ACMECertificateADomainlistItem] | Unset = UNSET
        if _a_domainlist is not UNSET:
            a_domainlist = []
            for a_domainlist_item_data in _a_domainlist:
                a_domainlist_item = ACMECertificateADomainlistItem.from_dict(a_domainlist_item_data)

                a_domainlist.append(a_domainlist_item)

        _a_actionlist = d.pop("a_actionlist", UNSET)
        a_actionlist: list[ACMECertificateAActionlistItem] | Unset = UNSET
        if _a_actionlist is not UNSET:
            a_actionlist = []
            for a_actionlist_item_data in _a_actionlist:
                a_actionlist_item = ACMECertificateAActionlistItem.from_dict(a_actionlist_item_data)

                a_actionlist.append(a_actionlist_item)

        patch_services_acme_certificate_endpoint_json_body = cls(
            id=id,
            name=name,
            descr=descr,
            status=status,
            acmeaccount=acmeaccount,
            keylength=keylength,
            keypaste=keypaste,
            preferredchain=preferredchain,
            oscpstaple=oscpstaple,
            dnssleep=dnssleep,
            renewafter=renewafter,
            a_domainlist=a_domainlist,
            a_actionlist=a_actionlist,
        )

        patch_services_acme_certificate_endpoint_json_body.additional_properties = d
        return patch_services_acme_certificate_endpoint_json_body

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
