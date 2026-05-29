from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acme_certificate_action_method import ACMECertificateActionMethod
from ..models.acme_certificate_action_status import ACMECertificateActionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesACMECertificateActionEndpointDataBody")


@_attrs_define
class PatchServicesACMECertificateActionEndpointDataBody:
    """
    Attributes:
        parent_id (int): The ID of the parent this object is nested under.
        id (int): The ID of the object or resource to interact with.
        status (ACMECertificateActionStatus | Unset): The activation status of the ACME certificate.<br> Default:
            ACMECertificateActionStatus.ACTIVE.
        command (str | Unset): The command to execute on the ACME certificate.<br>
        method (ACMECertificateActionMethod | Unset): The action method that should be used to run the command.<br>
    """

    parent_id: int
    id: int
    status: ACMECertificateActionStatus | Unset = ACMECertificateActionStatus.ACTIVE
    command: str | Unset = UNSET
    method: ACMECertificateActionMethod | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        command = self.command

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "id": id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if command is not UNSET:
            field_dict["command"] = command
        if method is not UNSET:
            field_dict["method"] = method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        id = d.pop("id")

        _status = d.pop("status", UNSET)
        status: ACMECertificateActionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ACMECertificateActionStatus(_status)

        command = d.pop("command", UNSET)

        _method = d.pop("method", UNSET)
        method: ACMECertificateActionMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = ACMECertificateActionMethod(_method)

        patch_services_acme_certificate_action_endpoint_data_body = cls(
            parent_id=parent_id,
            id=id,
            status=status,
            command=command,
            method=method,
        )

        patch_services_acme_certificate_action_endpoint_data_body.additional_properties = d
        return patch_services_acme_certificate_action_endpoint_data_body

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
