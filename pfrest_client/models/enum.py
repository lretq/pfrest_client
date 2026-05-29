from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enum_choices_type_0 import EnumChoicesType0


T = TypeVar("T", bound="Enum")


@_attrs_define
class Enum:
    """
    Attributes:
        model_name (str | Unset): The name of the model whose field's choices are being requested.<br>
        model_field (str | Unset): The name of the field whose choices are being requested.<br>
        choices (EnumChoicesType0 | None | Unset): The available choices for the specified model and field. The key
            represents the internal name of the choice, and the value is the verbose, human-friendly name of the choice.<br>
    """

    model_name: str | Unset = UNSET
    model_field: str | Unset = UNSET
    choices: EnumChoicesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.enum_choices_type_0 import EnumChoicesType0

        model_name = self.model_name

        model_field = self.model_field

        choices: dict[str, Any] | None | Unset
        if isinstance(self.choices, Unset):
            choices = UNSET
        elif isinstance(self.choices, EnumChoicesType0):
            choices = self.choices.to_dict()
        else:
            choices = self.choices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if model_field is not UNSET:
            field_dict["model_field"] = model_field
        if choices is not UNSET:
            field_dict["choices"] = choices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enum_choices_type_0 import EnumChoicesType0

        d = dict(src_dict)
        model_name = d.pop("model_name", UNSET)

        model_field = d.pop("model_field", UNSET)

        def _parse_choices(data: object) -> EnumChoicesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                choices_type_0 = EnumChoicesType0.from_dict(data)

                return choices_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(EnumChoicesType0 | None | Unset, data)

        choices = _parse_choices(d.pop("choices", UNSET))

        enum = cls(
            model_name=model_name,
            model_field=model_field,
            choices=choices,
        )

        enum.additional_properties = d
        return enum

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
