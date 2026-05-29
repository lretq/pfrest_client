from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateRenew")


@_attrs_define
class CertificateRenew:
    """
    Attributes:
        certref (str | Unset): The `refid` of the Certificate to renew.<br>
        reusekey (bool | Unset): Reuses the existing private key when renewing the certificate.<br> Default: True.
        reuseserial (bool | Unset): Reuses the existing serial number when renewing the certificate.<br> Default: True.
        strictsecurity (bool | Unset): Enforces strict security measures when renewing the certificate.<br>
        oldserial (None | str | Unset): The old serial number of the Certificate before the renewal.<br>
        newserial (None | str | Unset): The new serial number of the Certificate after the renewal.<br>
    """

    certref: str | Unset = UNSET
    reusekey: bool | Unset = True
    reuseserial: bool | Unset = True
    strictsecurity: bool | Unset = UNSET
    oldserial: None | str | Unset = UNSET
    newserial: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certref = self.certref

        reusekey = self.reusekey

        reuseserial = self.reuseserial

        strictsecurity = self.strictsecurity

        oldserial: None | str | Unset
        if isinstance(self.oldserial, Unset):
            oldserial = UNSET
        else:
            oldserial = self.oldserial

        newserial: None | str | Unset
        if isinstance(self.newserial, Unset):
            newserial = UNSET
        else:
            newserial = self.newserial

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certref is not UNSET:
            field_dict["certref"] = certref
        if reusekey is not UNSET:
            field_dict["reusekey"] = reusekey
        if reuseserial is not UNSET:
            field_dict["reuseserial"] = reuseserial
        if strictsecurity is not UNSET:
            field_dict["strictsecurity"] = strictsecurity
        if oldserial is not UNSET:
            field_dict["oldserial"] = oldserial
        if newserial is not UNSET:
            field_dict["newserial"] = newserial

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certref = d.pop("certref", UNSET)

        reusekey = d.pop("reusekey", UNSET)

        reuseserial = d.pop("reuseserial", UNSET)

        strictsecurity = d.pop("strictsecurity", UNSET)

        def _parse_oldserial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oldserial = _parse_oldserial(d.pop("oldserial", UNSET))

        def _parse_newserial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        newserial = _parse_newserial(d.pop("newserial", UNSET))

        certificate_renew = cls(
            certref=certref,
            reusekey=reusekey,
            reuseserial=reuseserial,
            strictsecurity=strictsecurity,
            oldserial=oldserial,
            newserial=newserial,
        )

        certificate_renew.additional_properties = d
        return certificate_renew

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
