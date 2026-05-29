from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bind_zone_type import BINDZoneType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bind_zone_records_item import BINDZoneRecordsItem


T = TypeVar("T", bound="PostServicesBINDZoneEndpointDataBody")


@_attrs_define
class PostServicesBINDZoneEndpointDataBody:
    """
    Attributes:
        name (str): The name of this BIND zone.<br>
        forwarders (list[str]): The forwarders for this BIND zone.<br><br>This field is only available when the
            following conditions are met:<br>- `type` must be equal to `'forward'`<br>
        baseip (str): The IP address of the base domain for this zone. This sets an A record for the base
            domain.<br><br>This field is only available when the following conditions are met:<br>- `type` must be equal to
            `'master'`<br>
        nameserver (str): The SOA nameserver for this zone.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be one of [ master, redirect ]<br>
        mail (str): The SOA email address (RNAME) for this zone. This must be in an FQDN format.<br><br>This field is
            only available when the following conditions are met:<br>- `type` must be one of [ master, redirect ]<br>
        serial (int): The SOA serial number for this zone.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be one of [ master, redirect ]<br>
        disabled (bool | Unset): Disable this BIND zone.<br>
        description (str | Unset): A description for this BIND zone.<br>
        type_ (BINDZoneType | Unset): The type of this BIND zone.<br> Default: BINDZoneType.MASTER.
        view (list[str] | Unset): The views this BIND zone belongs to.<br>
        reversev4 (bool | Unset): Enable reverse DNS for this BIND zone.<br><br>This field is only available when the
            following conditions are met:<br>- `type` must be one of [ master, slave ]<br>
        reversev6 (bool | Unset): Enable reverse IPv6 DNS for this BIND zone.<br><br>This field is only available when
            the following conditions are met:<br>- `type` must be one of [ master, slave ]<br>
        rpz (bool | Unset): Enable this zone as part of a response policy.<br><br>This field is only available when the
            following conditions are met:<br>- `type` must be one of [ master, slave ]<br>
        custom (str | Unset): Custom BIND options for this BIND zone.<br>
        dnssec (bool | Unset): Enable DNSSEC for this BIND zone.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be one of [ master, slave ]<br>
        backupkeys (bool | Unset): Enable backing up DNSSEC keys in the XML configuration for this BIND
            zone.<br><br>This field is only available when the following conditions are met:<br>- `dnssec` must be equal to
            `true`<br>
        slaveip (str | Unset): The IP address of the slave server for this BIND zone.<br><br>This field is only
            available when the following conditions are met:<br>- `type` must be equal to `'slave'`<br>
        ttl (int | None | Unset): The default TTL interval (in seconds) for records within this BIND zone without a
            specific TTL.<br><br>This field is only available when the following conditions are met:<br>- `type` must be
            equal to `'master'`<br>
        refresh (None | str | Unset): The SOA refresh interval for this zone. TTL-style time-unit suffixes are supported
            (e.g. 1h, 1d, 1w), otherwise time in seconds is assumed.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be one of [ master, redirect ]<br>
        retry (None | str | Unset): The SOA retry interval for this zone. TTL-style time-unit suffixes are supported
            (e.g. 1h, 1d, 1w), otherwise time in seconds is assumed.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be one of [ master, redirect ]<br>
        expire (None | str | Unset): The SOA expiry interval for this zone. TTL-style time-unit suffixes are supported
            (e.g. 1h, 1d, 1w), otherwise time in seconds is assumed.<br><br>This field is only available when the following
            conditions are met:<br>- `type` must be one of [ master, redirect ]<br>
        minimum (None | str | Unset): The SOA minimum TTL interval (in seconds) for this zone. This is also referred to
            as the negative TTL. TTL-style time-unit suffixes are supported (e.g. 1h, 1d, 1w), otherwise time in seconds is
            assumed.<br><br>This field is only available when the following conditions are met:<br>- `type` must be one of [
            master, redirect ]<br>
        enable_updatepolicy (bool | Unset): Enable a specific dynamic update policy for this BIND zone.<br><br>This
            field is only available when the following conditions are met:<br>- `type` must be equal to `'master'`<br>
        updatepolicy (str | Unset): The update policy for this BIND zone.<br><br>This field is only available when the
            following conditions are met:<br>- `type` must be equal to `'master'`<br>- `enable_updatepolicy` must be equal
            to `true`<br>
        allowupdate (list[str] | Unset): The access lists that are allowed to submit dynamic updates for 'master' zones
            (e.g. dynamic DNS).<br><br>This field is only available when the following conditions are met:<br>- `type` must
            be equal to `'master'`<br>- `enable_updatepolicy` must be equal to `false`<br>
        allowtransfer (list[str] | Unset): The access lists that are allowed to transfer this BIND zone.<br><br>This
            field is only available when the following conditions are met:<br>- `type` must be equal to `'master'`<br>
        allowquery (list[str] | Unset): The access lists that are allowed to query this BIND zone.<br>
        regdhcpstatic (bool | Unset): Register DHCP static mappings as records in this BIND zone.<br>
        customzonerecords (str | Unset): Custom records for this BIND zone.<br>
        records (list[BINDZoneRecordsItem] | Unset): The records for this BIND zone.<br>
    """

    name: str
    forwarders: list[str]
    baseip: str
    nameserver: str
    mail: str
    serial: int
    disabled: bool | Unset = UNSET
    description: str | Unset = UNSET
    type_: BINDZoneType | Unset = BINDZoneType.MASTER
    view: list[str] | Unset = UNSET
    reversev4: bool | Unset = UNSET
    reversev6: bool | Unset = UNSET
    rpz: bool | Unset = UNSET
    custom: str | Unset = UNSET
    dnssec: bool | Unset = UNSET
    backupkeys: bool | Unset = UNSET
    slaveip: str | Unset = UNSET
    ttl: int | None | Unset = UNSET
    refresh: None | str | Unset = UNSET
    retry: None | str | Unset = UNSET
    expire: None | str | Unset = UNSET
    minimum: None | str | Unset = UNSET
    enable_updatepolicy: bool | Unset = UNSET
    updatepolicy: str | Unset = UNSET
    allowupdate: list[str] | Unset = UNSET
    allowtransfer: list[str] | Unset = UNSET
    allowquery: list[str] | Unset = UNSET
    regdhcpstatic: bool | Unset = UNSET
    customzonerecords: str | Unset = UNSET
    records: list[BINDZoneRecordsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        forwarders = self.forwarders

        baseip = self.baseip

        nameserver = self.nameserver

        mail = self.mail

        serial = self.serial

        disabled = self.disabled

        description = self.description

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        view: list[str] | Unset = UNSET
        if not isinstance(self.view, Unset):
            view = self.view

        reversev4 = self.reversev4

        reversev6 = self.reversev6

        rpz = self.rpz

        custom = self.custom

        dnssec = self.dnssec

        backupkeys = self.backupkeys

        slaveip = self.slaveip

        ttl: int | None | Unset
        if isinstance(self.ttl, Unset):
            ttl = UNSET
        else:
            ttl = self.ttl

        refresh: None | str | Unset
        if isinstance(self.refresh, Unset):
            refresh = UNSET
        else:
            refresh = self.refresh

        retry: None | str | Unset
        if isinstance(self.retry, Unset):
            retry = UNSET
        else:
            retry = self.retry

        expire: None | str | Unset
        if isinstance(self.expire, Unset):
            expire = UNSET
        else:
            expire = self.expire

        minimum: None | str | Unset
        if isinstance(self.minimum, Unset):
            minimum = UNSET
        else:
            minimum = self.minimum

        enable_updatepolicy = self.enable_updatepolicy

        updatepolicy = self.updatepolicy

        allowupdate: list[str] | Unset = UNSET
        if not isinstance(self.allowupdate, Unset):
            allowupdate = self.allowupdate

        allowtransfer: list[str] | Unset = UNSET
        if not isinstance(self.allowtransfer, Unset):
            allowtransfer = self.allowtransfer

        allowquery: list[str] | Unset = UNSET
        if not isinstance(self.allowquery, Unset):
            allowquery = self.allowquery

        regdhcpstatic = self.regdhcpstatic

        customzonerecords = self.customzonerecords

        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "forwarders": forwarders,
                "baseip": baseip,
                "nameserver": nameserver,
                "mail": mail,
                "serial": serial,
            }
        )
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if view is not UNSET:
            field_dict["view"] = view
        if reversev4 is not UNSET:
            field_dict["reversev4"] = reversev4
        if reversev6 is not UNSET:
            field_dict["reversev6"] = reversev6
        if rpz is not UNSET:
            field_dict["rpz"] = rpz
        if custom is not UNSET:
            field_dict["custom"] = custom
        if dnssec is not UNSET:
            field_dict["dnssec"] = dnssec
        if backupkeys is not UNSET:
            field_dict["backupkeys"] = backupkeys
        if slaveip is not UNSET:
            field_dict["slaveip"] = slaveip
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if refresh is not UNSET:
            field_dict["refresh"] = refresh
        if retry is not UNSET:
            field_dict["retry"] = retry
        if expire is not UNSET:
            field_dict["expire"] = expire
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if enable_updatepolicy is not UNSET:
            field_dict["enable_updatepolicy"] = enable_updatepolicy
        if updatepolicy is not UNSET:
            field_dict["updatepolicy"] = updatepolicy
        if allowupdate is not UNSET:
            field_dict["allowupdate"] = allowupdate
        if allowtransfer is not UNSET:
            field_dict["allowtransfer"] = allowtransfer
        if allowquery is not UNSET:
            field_dict["allowquery"] = allowquery
        if regdhcpstatic is not UNSET:
            field_dict["regdhcpstatic"] = regdhcpstatic
        if customzonerecords is not UNSET:
            field_dict["customzonerecords"] = customzonerecords
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bind_zone_records_item import BINDZoneRecordsItem

        d = dict(src_dict)
        name = d.pop("name")

        forwarders = cast(list[str], d.pop("forwarders"))

        baseip = d.pop("baseip")

        nameserver = d.pop("nameserver")

        mail = d.pop("mail")

        serial = d.pop("serial")

        disabled = d.pop("disabled", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: BINDZoneType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BINDZoneType(_type_)

        view = cast(list[str], d.pop("view", UNSET))

        reversev4 = d.pop("reversev4", UNSET)

        reversev6 = d.pop("reversev6", UNSET)

        rpz = d.pop("rpz", UNSET)

        custom = d.pop("custom", UNSET)

        dnssec = d.pop("dnssec", UNSET)

        backupkeys = d.pop("backupkeys", UNSET)

        slaveip = d.pop("slaveip", UNSET)

        def _parse_ttl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ttl = _parse_ttl(d.pop("ttl", UNSET))

        def _parse_refresh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refresh = _parse_refresh(d.pop("refresh", UNSET))

        def _parse_retry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retry = _parse_retry(d.pop("retry", UNSET))

        def _parse_expire(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expire = _parse_expire(d.pop("expire", UNSET))

        def _parse_minimum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum = _parse_minimum(d.pop("minimum", UNSET))

        enable_updatepolicy = d.pop("enable_updatepolicy", UNSET)

        updatepolicy = d.pop("updatepolicy", UNSET)

        allowupdate = cast(list[str], d.pop("allowupdate", UNSET))

        allowtransfer = cast(list[str], d.pop("allowtransfer", UNSET))

        allowquery = cast(list[str], d.pop("allowquery", UNSET))

        regdhcpstatic = d.pop("regdhcpstatic", UNSET)

        customzonerecords = d.pop("customzonerecords", UNSET)

        _records = d.pop("records", UNSET)
        records: list[BINDZoneRecordsItem] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:
                records_item = BINDZoneRecordsItem.from_dict(records_item_data)

                records.append(records_item)

        post_services_bind_zone_endpoint_data_body = cls(
            name=name,
            forwarders=forwarders,
            baseip=baseip,
            nameserver=nameserver,
            mail=mail,
            serial=serial,
            disabled=disabled,
            description=description,
            type_=type_,
            view=view,
            reversev4=reversev4,
            reversev6=reversev6,
            rpz=rpz,
            custom=custom,
            dnssec=dnssec,
            backupkeys=backupkeys,
            slaveip=slaveip,
            ttl=ttl,
            refresh=refresh,
            retry=retry,
            expire=expire,
            minimum=minimum,
            enable_updatepolicy=enable_updatepolicy,
            updatepolicy=updatepolicy,
            allowupdate=allowupdate,
            allowtransfer=allowtransfer,
            allowquery=allowquery,
            regdhcpstatic=regdhcpstatic,
            customzonerecords=customzonerecords,
            records=records,
        )

        post_services_bind_zone_endpoint_data_body.additional_properties = d
        return post_services_bind_zone_endpoint_data_body

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
