from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesACMECertificateRenewEndpointDataBody")


@_attrs_define
class PostServicesACMECertificateRenewEndpointDataBody:
    """
    Attributes:
        certificate (str): The name of the ACME certificate to be renewed.<br>
        status (None | str | Unset): The status of the ACME certificate renew process. This will show 'pending' if the
            renew process is still running or 'completed' if the renew process has finished. This status only indicates
            whether the renew process has completed, not whether it was successful. You will needto refer to the result log
            for that information. Note: This log is only populated when the renew process is initiated via REST API, not
            when it is initiated via the pfSense webConfigurator or auto-renewals.<br> Default: 'pending'.
        last_updated (int | None | Unset): The unix timestamp of when the ACME certificate renew status last changed.
            Note: This timestamp is only updated when the renew process is initiated via REST API, not when it is initiated
            via the pfSense webConfigurator or auto-renewals.<br>
        result_log (None | str | Unset): The output result of the acme.sh renew command. Note: This log is only
            populated when the renew process is initiated via REST API, not when it is initiated via the pfSense
            webConfigurator or auto-renewals.<br>
    """

    certificate: str
    status: None | str | Unset = "pending"
    last_updated: int | None | Unset = UNSET
    result_log: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificate = self.certificate

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        last_updated: int | None | Unset
        if isinstance(self.last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = self.last_updated

        result_log: None | str | Unset
        if isinstance(self.result_log, Unset):
            result_log = UNSET
        else:
            result_log = self.result_log

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certificate": certificate,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if result_log is not UNSET:
            field_dict["result_log"] = result_log

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        certificate = d.pop("certificate")

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_last_updated(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_updated = _parse_last_updated(d.pop("last_updated", UNSET))

        def _parse_result_log(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        result_log = _parse_result_log(d.pop("result_log", UNSET))

        post_services_acme_certificate_renew_endpoint_data_body = cls(
            certificate=certificate,
            status=status,
            last_updated=last_updated,
            result_log=result_log,
        )

        post_services_acme_certificate_renew_endpoint_data_body.additional_properties = d
        return post_services_acme_certificate_renew_endpoint_data_body

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
