from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acme_certificate_action_method import ACMECertificateActionMethod
from ..models.acme_certificate_action_status import ACMECertificateActionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostServicesACMECertificateActionEndpointJsonBody")


@_attrs_define
class PostServicesACMECertificateActionEndpointJsonBody:
    """
    Attributes:
        command (str): The command to execute on the ACME certificate.<br>
        method (ACMECertificateActionMethod): The action method that should be used to run the command.<br>
        parent_id (int): The ID of the parent this object is nested under.
        status (ACMECertificateActionStatus | Unset): The activation status of the ACME certificate.<br> Default:
            ACMECertificateActionStatus.ACTIVE.
    """

    command: str
    method: ACMECertificateActionMethod
    parent_id: int
    status: ACMECertificateActionStatus | Unset = ACMECertificateActionStatus.ACTIVE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        method = self.method.value

        parent_id = self.parent_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
                "method": method,
                "parent_id": parent_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        command = d.pop("command")

        method = ACMECertificateActionMethod(d.pop("method"))

        parent_id = d.pop("parent_id")

        _status = d.pop("status", UNSET)
        status: ACMECertificateActionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ACMECertificateActionStatus(_status)

        post_services_acme_certificate_action_endpoint_json_body = cls(
            command=command,
            method=method,
            parent_id=parent_id,
            status=status,
        )

        post_services_acme_certificate_action_endpoint_json_body.additional_properties = d
        return post_services_acme_certificate_action_endpoint_json_body

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
