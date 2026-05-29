from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostDiagnosticsPingEndpointDataBody")


@_attrs_define
class PostDiagnosticsPingEndpointDataBody:
    """
    Attributes:
        host (str): The IP address or hostname to ping.<br>
        count (int | Unset): The number of ping requests to send.<br> Default: 3.
        source_address (str | Unset): The source IP address to use for ping requests.<br>
        output (None | str | Unset): The output from the ping command.<br>
        result_code (int | None | Unset): The result code from the ping command. 0 indicates success.<br>
    """

    host: str
    count: int | Unset = 3
    source_address: str | Unset = UNSET
    output: None | str | Unset = UNSET
    result_code: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host = self.host

        count = self.count

        source_address = self.source_address

        output: None | str | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        result_code: int | None | Unset
        if isinstance(self.result_code, Unset):
            result_code = UNSET
        else:
            result_code = self.result_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "host": host,
            }
        )
        if count is not UNSET:
            field_dict["count"] = count
        if source_address is not UNSET:
            field_dict["source_address"] = source_address
        if output is not UNSET:
            field_dict["output"] = output
        if result_code is not UNSET:
            field_dict["result_code"] = result_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host = d.pop("host")

        count = d.pop("count", UNSET)

        source_address = d.pop("source_address", UNSET)

        def _parse_output(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        output = _parse_output(d.pop("output", UNSET))

        def _parse_result_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_code = _parse_result_code(d.pop("result_code", UNSET))

        post_diagnostics_ping_endpoint_data_body = cls(
            host=host,
            count=count,
            source_address=source_address,
            output=output,
            result_code=result_code,
        )

        post_diagnostics_ping_endpoint_data_body.additional_properties = d
        return post_diagnostics_ping_endpoint_data_body

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
