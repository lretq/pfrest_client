from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPsecChildSAStatus")


@_attrs_define
class IPsecChildSAStatus:
    """
    Attributes:
        name (None | str | Unset): The name of the connection ID for the child SA.<br>
        uniqueid (int | None | Unset): The unique ID of the child SA.<br>
        reqid (int | None | Unset): The request ID of the child SA.<br>
        state (None | str | Unset): The current state of the child SA.<br>
        mode (None | str | Unset): The mode of the child SA.<br>
        protocol (None | str | Unset): The protocol of the child SA.<br>
        encap (bool | None | Unset): Whether encapsulation is used for the child SA.<br>
        spi_in (None | str | Unset): The incoming SPI of the child SA.<br>
        spi_out (None | str | Unset): The outgoing SPI of the child SA.<br>
        encr_alg (None | str | Unset): The encryption algorithm used by the child SA.<br>
        encr_keysize (int | None | Unset): The encryption key size used by the child SA.<br>
        integ_alg (None | str | Unset): The integrity algorithm used by the child SA.<br>
        dh_group (None | str | Unset): The Diffie-Hellman group used by the child SA.<br>
        bytes_in (int | None | Unset): The number of bytes received by the child SA.<br>
        bytes_out (int | None | Unset): The number of bytes sent by the child SA.<br>
        packets_in (int | None | Unset): The number of packets received by the child SA.<br>
        packets_out (int | None | Unset): The number of packets sent by the child SA.<br>
        use_in (int | None | Unset): The number of times the child SA has been used to receive data.<br>
        use_out (int | None | Unset): The number of times the child SA has been used to send data.<br>
        rekey_time (int | None | Unset): The time at which the child SA will be rekeyed.<br>
        life_time (int | None | Unset): The time at which the child SA will expire.<br>
        install_time (int | None | Unset): The time at which the child SA was installed.<br>
        local_ts (list[str] | None | Unset): The local traffic selector of the child SA.<br>
        remote_ts (list[str] | None | Unset): The remote traffic selector of the child SA.<br>
    """

    name: None | str | Unset = UNSET
    uniqueid: int | None | Unset = UNSET
    reqid: int | None | Unset = UNSET
    state: None | str | Unset = UNSET
    mode: None | str | Unset = UNSET
    protocol: None | str | Unset = UNSET
    encap: bool | None | Unset = UNSET
    spi_in: None | str | Unset = UNSET
    spi_out: None | str | Unset = UNSET
    encr_alg: None | str | Unset = UNSET
    encr_keysize: int | None | Unset = UNSET
    integ_alg: None | str | Unset = UNSET
    dh_group: None | str | Unset = UNSET
    bytes_in: int | None | Unset = UNSET
    bytes_out: int | None | Unset = UNSET
    packets_in: int | None | Unset = UNSET
    packets_out: int | None | Unset = UNSET
    use_in: int | None | Unset = UNSET
    use_out: int | None | Unset = UNSET
    rekey_time: int | None | Unset = UNSET
    life_time: int | None | Unset = UNSET
    install_time: int | None | Unset = UNSET
    local_ts: list[str] | None | Unset = UNSET
    remote_ts: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        uniqueid: int | None | Unset
        if isinstance(self.uniqueid, Unset):
            uniqueid = UNSET
        else:
            uniqueid = self.uniqueid

        reqid: int | None | Unset
        if isinstance(self.reqid, Unset):
            reqid = UNSET
        else:
            reqid = self.reqid

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        protocol: None | str | Unset
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        else:
            protocol = self.protocol

        encap: bool | None | Unset
        if isinstance(self.encap, Unset):
            encap = UNSET
        else:
            encap = self.encap

        spi_in: None | str | Unset
        if isinstance(self.spi_in, Unset):
            spi_in = UNSET
        else:
            spi_in = self.spi_in

        spi_out: None | str | Unset
        if isinstance(self.spi_out, Unset):
            spi_out = UNSET
        else:
            spi_out = self.spi_out

        encr_alg: None | str | Unset
        if isinstance(self.encr_alg, Unset):
            encr_alg = UNSET
        else:
            encr_alg = self.encr_alg

        encr_keysize: int | None | Unset
        if isinstance(self.encr_keysize, Unset):
            encr_keysize = UNSET
        else:
            encr_keysize = self.encr_keysize

        integ_alg: None | str | Unset
        if isinstance(self.integ_alg, Unset):
            integ_alg = UNSET
        else:
            integ_alg = self.integ_alg

        dh_group: None | str | Unset
        if isinstance(self.dh_group, Unset):
            dh_group = UNSET
        else:
            dh_group = self.dh_group

        bytes_in: int | None | Unset
        if isinstance(self.bytes_in, Unset):
            bytes_in = UNSET
        else:
            bytes_in = self.bytes_in

        bytes_out: int | None | Unset
        if isinstance(self.bytes_out, Unset):
            bytes_out = UNSET
        else:
            bytes_out = self.bytes_out

        packets_in: int | None | Unset
        if isinstance(self.packets_in, Unset):
            packets_in = UNSET
        else:
            packets_in = self.packets_in

        packets_out: int | None | Unset
        if isinstance(self.packets_out, Unset):
            packets_out = UNSET
        else:
            packets_out = self.packets_out

        use_in: int | None | Unset
        if isinstance(self.use_in, Unset):
            use_in = UNSET
        else:
            use_in = self.use_in

        use_out: int | None | Unset
        if isinstance(self.use_out, Unset):
            use_out = UNSET
        else:
            use_out = self.use_out

        rekey_time: int | None | Unset
        if isinstance(self.rekey_time, Unset):
            rekey_time = UNSET
        else:
            rekey_time = self.rekey_time

        life_time: int | None | Unset
        if isinstance(self.life_time, Unset):
            life_time = UNSET
        else:
            life_time = self.life_time

        install_time: int | None | Unset
        if isinstance(self.install_time, Unset):
            install_time = UNSET
        else:
            install_time = self.install_time

        local_ts: list[str] | None | Unset
        if isinstance(self.local_ts, Unset):
            local_ts = UNSET
        elif isinstance(self.local_ts, list):
            local_ts = self.local_ts

        else:
            local_ts = self.local_ts

        remote_ts: list[str] | None | Unset
        if isinstance(self.remote_ts, Unset):
            remote_ts = UNSET
        elif isinstance(self.remote_ts, list):
            remote_ts = self.remote_ts

        else:
            remote_ts = self.remote_ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if uniqueid is not UNSET:
            field_dict["uniqueid"] = uniqueid
        if reqid is not UNSET:
            field_dict["reqid"] = reqid
        if state is not UNSET:
            field_dict["state"] = state
        if mode is not UNSET:
            field_dict["mode"] = mode
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if encap is not UNSET:
            field_dict["encap"] = encap
        if spi_in is not UNSET:
            field_dict["spi_in"] = spi_in
        if spi_out is not UNSET:
            field_dict["spi_out"] = spi_out
        if encr_alg is not UNSET:
            field_dict["encr_alg"] = encr_alg
        if encr_keysize is not UNSET:
            field_dict["encr_keysize"] = encr_keysize
        if integ_alg is not UNSET:
            field_dict["integ_alg"] = integ_alg
        if dh_group is not UNSET:
            field_dict["dh_group"] = dh_group
        if bytes_in is not UNSET:
            field_dict["bytes_in"] = bytes_in
        if bytes_out is not UNSET:
            field_dict["bytes_out"] = bytes_out
        if packets_in is not UNSET:
            field_dict["packets_in"] = packets_in
        if packets_out is not UNSET:
            field_dict["packets_out"] = packets_out
        if use_in is not UNSET:
            field_dict["use_in"] = use_in
        if use_out is not UNSET:
            field_dict["use_out"] = use_out
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if life_time is not UNSET:
            field_dict["life_time"] = life_time
        if install_time is not UNSET:
            field_dict["install_time"] = install_time
        if local_ts is not UNSET:
            field_dict["local_ts"] = local_ts
        if remote_ts is not UNSET:
            field_dict["remote_ts"] = remote_ts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_uniqueid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        uniqueid = _parse_uniqueid(d.pop("uniqueid", UNSET))

        def _parse_reqid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reqid = _parse_reqid(d.pop("reqid", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_protocol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_encap(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        encap = _parse_encap(d.pop("encap", UNSET))

        def _parse_spi_in(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spi_in = _parse_spi_in(d.pop("spi_in", UNSET))

        def _parse_spi_out(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spi_out = _parse_spi_out(d.pop("spi_out", UNSET))

        def _parse_encr_alg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        encr_alg = _parse_encr_alg(d.pop("encr_alg", UNSET))

        def _parse_encr_keysize(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        encr_keysize = _parse_encr_keysize(d.pop("encr_keysize", UNSET))

        def _parse_integ_alg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        integ_alg = _parse_integ_alg(d.pop("integ_alg", UNSET))

        def _parse_dh_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_group = _parse_dh_group(d.pop("dh_group", UNSET))

        def _parse_bytes_in(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bytes_in = _parse_bytes_in(d.pop("bytes_in", UNSET))

        def _parse_bytes_out(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bytes_out = _parse_bytes_out(d.pop("bytes_out", UNSET))

        def _parse_packets_in(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        packets_in = _parse_packets_in(d.pop("packets_in", UNSET))

        def _parse_packets_out(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        packets_out = _parse_packets_out(d.pop("packets_out", UNSET))

        def _parse_use_in(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        use_in = _parse_use_in(d.pop("use_in", UNSET))

        def _parse_use_out(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        use_out = _parse_use_out(d.pop("use_out", UNSET))

        def _parse_rekey_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rekey_time = _parse_rekey_time(d.pop("rekey_time", UNSET))

        def _parse_life_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        life_time = _parse_life_time(d.pop("life_time", UNSET))

        def _parse_install_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        install_time = _parse_install_time(d.pop("install_time", UNSET))

        def _parse_local_ts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                local_ts_type_0 = cast(list[str], data)

                return local_ts_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[str] | None | Unset, data)

        local_ts = _parse_local_ts(d.pop("local_ts", UNSET))

        def _parse_remote_ts(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                remote_ts_type_0 = cast(list[str], data)

                return remote_ts_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[str] | None | Unset, data)

        remote_ts = _parse_remote_ts(d.pop("remote_ts", UNSET))

        i_psec_child_sa_status = cls(
            name=name,
            uniqueid=uniqueid,
            reqid=reqid,
            state=state,
            mode=mode,
            protocol=protocol,
            encap=encap,
            spi_in=spi_in,
            spi_out=spi_out,
            encr_alg=encr_alg,
            encr_keysize=encr_keysize,
            integ_alg=integ_alg,
            dh_group=dh_group,
            bytes_in=bytes_in,
            bytes_out=bytes_out,
            packets_in=packets_in,
            packets_out=packets_out,
            use_in=use_in,
            use_out=use_out,
            rekey_time=rekey_time,
            life_time=life_time,
            install_time=install_time,
            local_ts=local_ts,
            remote_ts=remote_ts,
        )

        i_psec_child_sa_status.additional_properties = d
        return i_psec_child_sa_status

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
