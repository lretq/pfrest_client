from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ntp_settings_dnsresolv import NTPSettingsDnsresolv
from ..models.ntp_settings_ntpmaxpoll import NTPSettingsNtpmaxpoll
from ..models.ntp_settings_ntpminpoll import NTPSettingsNtpminpoll
from ..models.ntp_settings_serverauthalgo import NTPSettingsServerauthalgo
from ..types import UNSET, Unset

T = TypeVar("T", bound="NTPSettings")


@_attrs_define
class NTPSettings:
    """
    Attributes:
        enable (bool | Unset): Enables or disabled the NTP server.<br> Default: True.
        interface (list[str] | Unset): The interfaces the NTP server will listen on.<br>
        ntpmaxpeers (int | Unset): The maximum number of candidate peers in the NTP pool.<br> Default: 5.
        orphan (int | Unset): The orphan mode stratum to set. Orphan mode allows the system clock to be used when no
            other clocks are available. The number here specifies the stratum reported during orphan mode and should
            normally be set to a number high enough to ensure that any other servers available to clients are preferred over
            this server<br> Default: 12.
        ntpminpoll (NTPSettingsNtpminpoll | Unset): The minimum poll interval for NTP messages. Use empty string to
            assume system default, and `omit` to not set this value.<br>
        ntpmaxpoll (NTPSettingsNtpmaxpoll | Unset): The maximum poll interval for NTP messages. Use empty string to
            assume system default, and `omit` to not set this value. This value must be greater than the `ntpminpoll`.<br>
        dnsresolv (NTPSettingsDnsresolv | Unset): The IP protocol peers are forced to use for DNS resolution.<br>
            Default: NTPSettingsDnsresolv.AUTO.
        logpeer (bool | Unset): Enable or disable logging peer messages.<br>
        logsys (bool | Unset): Enable or disable logging system messages.<br>
        clockstats (bool | Unset): Enable or disable logging reference clock statistics.<br>
        loopstats (bool | Unset): Enable or disable logging clock discipline statistics.<br>
        peerstats (bool | Unset): Enable or disable logging peer statistics.<br>
        statsgraph (bool | Unset): Enable or disable RRD graphs for NTP statistics.<br>
        leapsec (str | Unset): The Leap second configuration as text.<br>
        serverauth (bool | Unset): Enable or disable NTPv3 server authentication. (RFC 1305)<br>
        serverauthkey (str | Unset): The NTP server authentication key.<br><br>This field is only available when the
            following conditions are met:<br>- `serverauth` must be equal to `true`<br>
        serverauthalgo (NTPSettingsServerauthalgo | Unset): The digest algorithm for the server authentication key.<br>
            Default: NTPSettingsServerauthalgo.MD5.
    """

    enable: bool | Unset = True
    interface: list[str] | Unset = UNSET
    ntpmaxpeers: int | Unset = 5
    orphan: int | Unset = 12
    ntpminpoll: NTPSettingsNtpminpoll | Unset = UNSET
    ntpmaxpoll: NTPSettingsNtpmaxpoll | Unset = UNSET
    dnsresolv: NTPSettingsDnsresolv | Unset = NTPSettingsDnsresolv.AUTO
    logpeer: bool | Unset = UNSET
    logsys: bool | Unset = UNSET
    clockstats: bool | Unset = UNSET
    loopstats: bool | Unset = UNSET
    peerstats: bool | Unset = UNSET
    statsgraph: bool | Unset = UNSET
    leapsec: str | Unset = UNSET
    serverauth: bool | Unset = UNSET
    serverauthkey: str | Unset = UNSET
    serverauthalgo: NTPSettingsServerauthalgo | Unset = NTPSettingsServerauthalgo.MD5
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        interface: list[str] | Unset = UNSET
        if not isinstance(self.interface, Unset):
            interface = self.interface

        ntpmaxpeers = self.ntpmaxpeers

        orphan = self.orphan

        ntpminpoll: str | Unset = UNSET
        if not isinstance(self.ntpminpoll, Unset):
            ntpminpoll = self.ntpminpoll.value

        ntpmaxpoll: str | Unset = UNSET
        if not isinstance(self.ntpmaxpoll, Unset):
            ntpmaxpoll = self.ntpmaxpoll.value

        dnsresolv: str | Unset = UNSET
        if not isinstance(self.dnsresolv, Unset):
            dnsresolv = self.dnsresolv.value

        logpeer = self.logpeer

        logsys = self.logsys

        clockstats = self.clockstats

        loopstats = self.loopstats

        peerstats = self.peerstats

        statsgraph = self.statsgraph

        leapsec = self.leapsec

        serverauth = self.serverauth

        serverauthkey = self.serverauthkey

        serverauthalgo: str | Unset = UNSET
        if not isinstance(self.serverauthalgo, Unset):
            serverauthalgo = self.serverauthalgo.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if interface is not UNSET:
            field_dict["interface"] = interface
        if ntpmaxpeers is not UNSET:
            field_dict["ntpmaxpeers"] = ntpmaxpeers
        if orphan is not UNSET:
            field_dict["orphan"] = orphan
        if ntpminpoll is not UNSET:
            field_dict["ntpminpoll"] = ntpminpoll
        if ntpmaxpoll is not UNSET:
            field_dict["ntpmaxpoll"] = ntpmaxpoll
        if dnsresolv is not UNSET:
            field_dict["dnsresolv"] = dnsresolv
        if logpeer is not UNSET:
            field_dict["logpeer"] = logpeer
        if logsys is not UNSET:
            field_dict["logsys"] = logsys
        if clockstats is not UNSET:
            field_dict["clockstats"] = clockstats
        if loopstats is not UNSET:
            field_dict["loopstats"] = loopstats
        if peerstats is not UNSET:
            field_dict["peerstats"] = peerstats
        if statsgraph is not UNSET:
            field_dict["statsgraph"] = statsgraph
        if leapsec is not UNSET:
            field_dict["leapsec"] = leapsec
        if serverauth is not UNSET:
            field_dict["serverauth"] = serverauth
        if serverauthkey is not UNSET:
            field_dict["serverauthkey"] = serverauthkey
        if serverauthalgo is not UNSET:
            field_dict["serverauthalgo"] = serverauthalgo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        interface = cast(list[str], d.pop("interface", UNSET))

        ntpmaxpeers = d.pop("ntpmaxpeers", UNSET)

        orphan = d.pop("orphan", UNSET)

        _ntpminpoll = d.pop("ntpminpoll", UNSET)
        ntpminpoll: NTPSettingsNtpminpoll | Unset
        if isinstance(_ntpminpoll, Unset):
            ntpminpoll = UNSET
        else:
            ntpminpoll = NTPSettingsNtpminpoll(_ntpminpoll)

        _ntpmaxpoll = d.pop("ntpmaxpoll", UNSET)
        ntpmaxpoll: NTPSettingsNtpmaxpoll | Unset
        if isinstance(_ntpmaxpoll, Unset):
            ntpmaxpoll = UNSET
        else:
            ntpmaxpoll = NTPSettingsNtpmaxpoll(_ntpmaxpoll)

        _dnsresolv = d.pop("dnsresolv", UNSET)
        dnsresolv: NTPSettingsDnsresolv | Unset
        if isinstance(_dnsresolv, Unset):
            dnsresolv = UNSET
        else:
            dnsresolv = NTPSettingsDnsresolv(_dnsresolv)

        logpeer = d.pop("logpeer", UNSET)

        logsys = d.pop("logsys", UNSET)

        clockstats = d.pop("clockstats", UNSET)

        loopstats = d.pop("loopstats", UNSET)

        peerstats = d.pop("peerstats", UNSET)

        statsgraph = d.pop("statsgraph", UNSET)

        leapsec = d.pop("leapsec", UNSET)

        serverauth = d.pop("serverauth", UNSET)

        serverauthkey = d.pop("serverauthkey", UNSET)

        _serverauthalgo = d.pop("serverauthalgo", UNSET)
        serverauthalgo: NTPSettingsServerauthalgo | Unset
        if isinstance(_serverauthalgo, Unset):
            serverauthalgo = UNSET
        else:
            serverauthalgo = NTPSettingsServerauthalgo(_serverauthalgo)

        ntp_settings = cls(
            enable=enable,
            interface=interface,
            ntpmaxpeers=ntpmaxpeers,
            orphan=orphan,
            ntpminpoll=ntpminpoll,
            ntpmaxpoll=ntpmaxpoll,
            dnsresolv=dnsresolv,
            logpeer=logpeer,
            logsys=logsys,
            clockstats=clockstats,
            loopstats=loopstats,
            peerstats=peerstats,
            statsgraph=statsgraph,
            leapsec=leapsec,
            serverauth=serverauth,
            serverauthkey=serverauthkey,
            serverauthalgo=serverauthalgo,
        )

        ntp_settings.additional_properties = d
        return ntp_settings

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
