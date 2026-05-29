from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bind_sync_settings_synconchanges import BINDSyncSettingsSynconchanges
from ..models.bind_sync_settings_synctimeout import BINDSyncSettingsSynctimeout
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchServicesBINDSyncSettingsEndpointDataBody")


@_attrs_define
class PatchServicesBINDSyncSettingsEndpointDataBody:
    """
    Attributes:
        synconchanges (BINDSyncSettingsSynconchanges): The sync mode to use.<br>
        masterip (str): The IP address of the master BIND server.<br>
        synctimeout (BINDSyncSettingsSynctimeout | Unset): The timeout for the sync process.<br> Default:
            BINDSyncSettingsSynctimeout.VALUE_30.
    """

    synconchanges: BINDSyncSettingsSynconchanges
    masterip: str
    synctimeout: BINDSyncSettingsSynctimeout | Unset = BINDSyncSettingsSynctimeout.VALUE_30
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        synconchanges = self.synconchanges.value

        masterip = self.masterip

        synctimeout: int | Unset = UNSET
        if not isinstance(self.synctimeout, Unset):
            synctimeout = self.synctimeout.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "synconchanges": synconchanges,
                "masterip": masterip,
            }
        )
        if synctimeout is not UNSET:
            field_dict["synctimeout"] = synctimeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        synconchanges = BINDSyncSettingsSynconchanges(d.pop("synconchanges"))

        masterip = d.pop("masterip")

        _synctimeout = d.pop("synctimeout", UNSET)
        synctimeout: BINDSyncSettingsSynctimeout | Unset
        if isinstance(_synctimeout, Unset):
            synctimeout = UNSET
        else:
            synctimeout = BINDSyncSettingsSynctimeout(_synctimeout)

        patch_services_bind_sync_settings_endpoint_data_body = cls(
            synconchanges=synconchanges,
            masterip=masterip,
            synctimeout=synctimeout,
        )

        patch_services_bind_sync_settings_endpoint_data_body.additional_properties = d
        return patch_services_bind_sync_settings_endpoint_data_body

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
