from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_psec_sa_status_child_sas_type_0_item import IPsecSAStatusChildSasType0Item


T = TypeVar("T", bound="IPsecSAStatus")


@_attrs_define
class IPsecSAStatus:
    """
    Attributes:
        con_id (None | str | Unset): The connection ID of the tunnel.<br>
        uniqueid (int | None | Unset): The unique ID of the tunnel.<br>
        version (int | None | Unset): The IKE version used by the tunnel.<br>
        state (None | str | Unset): The current state of the tunnel.<br>
        local_host (None | str | Unset): The local host for the tunnel.<br>
        local_port (None | str | Unset): The local port for the tunnel. Valid options are: a TCP/UDP port number<br>
        local_id (None | str | Unset): The local ID for the tunnel.<br>
        remote_host (None | str | Unset): The remote host for the tunnel.<br>
        remote_port (None | str | Unset): The remote port for the tunnel. Valid options are: a TCP/UDP port number<br>
        remote_id (None | str | Unset): The remote ID for the tunnel.<br>
        initiator_spi (None | str | Unset): The initiator SPI for the tunnel.<br>
        responder_spi (None | str | Unset): The responder SPI for the tunnel.<br>
        nat_remote (bool | None | Unset): Whether the remote host is behind NAT.<br>
        nat_any (bool | None | Unset): Whether the remote host is behind any NAT.<br>
        encr_alg (None | str | Unset): The encryption algorithm used by the tunnel.<br>
        encr_keysize (int | None | Unset): The encryption key size used by the tunnel.<br>
        integ_alg (None | str | Unset): The integrity algorithm used by the tunnel.<br>
        prf_alg (None | str | Unset): The pseudo-random function algorithm used by the tunnel.<br>
        dh_group (None | str | Unset): The Diffie-Hellman group used by the tunnel.<br>
        established (int | None | Unset): The amount of time the tunnel has been established.<br>
        rekey_time (int | None | Unset): The amount of time until the tunnel rekeys.<br>
        child_sas (list[IPsecSAStatusChildSasType0Item] | None | Unset): The child SAs of the tunnel.<br>
    """

    con_id: None | str | Unset = UNSET
    uniqueid: int | None | Unset = UNSET
    version: int | None | Unset = UNSET
    state: None | str | Unset = UNSET
    local_host: None | str | Unset = UNSET
    local_port: None | str | Unset = UNSET
    local_id: None | str | Unset = UNSET
    remote_host: None | str | Unset = UNSET
    remote_port: None | str | Unset = UNSET
    remote_id: None | str | Unset = UNSET
    initiator_spi: None | str | Unset = UNSET
    responder_spi: None | str | Unset = UNSET
    nat_remote: bool | None | Unset = UNSET
    nat_any: bool | None | Unset = UNSET
    encr_alg: None | str | Unset = UNSET
    encr_keysize: int | None | Unset = UNSET
    integ_alg: None | str | Unset = UNSET
    prf_alg: None | str | Unset = UNSET
    dh_group: None | str | Unset = UNSET
    established: int | None | Unset = UNSET
    rekey_time: int | None | Unset = UNSET
    child_sas: list[IPsecSAStatusChildSasType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        con_id: None | str | Unset
        if isinstance(self.con_id, Unset):
            con_id = UNSET
        else:
            con_id = self.con_id

        uniqueid: int | None | Unset
        if isinstance(self.uniqueid, Unset):
            uniqueid = UNSET
        else:
            uniqueid = self.uniqueid

        version: int | None | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        local_host: None | str | Unset
        if isinstance(self.local_host, Unset):
            local_host = UNSET
        else:
            local_host = self.local_host

        local_port: None | str | Unset
        if isinstance(self.local_port, Unset):
            local_port = UNSET
        else:
            local_port = self.local_port

        local_id: None | str | Unset
        if isinstance(self.local_id, Unset):
            local_id = UNSET
        else:
            local_id = self.local_id

        remote_host: None | str | Unset
        if isinstance(self.remote_host, Unset):
            remote_host = UNSET
        else:
            remote_host = self.remote_host

        remote_port: None | str | Unset
        if isinstance(self.remote_port, Unset):
            remote_port = UNSET
        else:
            remote_port = self.remote_port

        remote_id: None | str | Unset
        if isinstance(self.remote_id, Unset):
            remote_id = UNSET
        else:
            remote_id = self.remote_id

        initiator_spi: None | str | Unset
        if isinstance(self.initiator_spi, Unset):
            initiator_spi = UNSET
        else:
            initiator_spi = self.initiator_spi

        responder_spi: None | str | Unset
        if isinstance(self.responder_spi, Unset):
            responder_spi = UNSET
        else:
            responder_spi = self.responder_spi

        nat_remote: bool | None | Unset
        if isinstance(self.nat_remote, Unset):
            nat_remote = UNSET
        else:
            nat_remote = self.nat_remote

        nat_any: bool | None | Unset
        if isinstance(self.nat_any, Unset):
            nat_any = UNSET
        else:
            nat_any = self.nat_any

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

        prf_alg: None | str | Unset
        if isinstance(self.prf_alg, Unset):
            prf_alg = UNSET
        else:
            prf_alg = self.prf_alg

        dh_group: None | str | Unset
        if isinstance(self.dh_group, Unset):
            dh_group = UNSET
        else:
            dh_group = self.dh_group

        established: int | None | Unset
        if isinstance(self.established, Unset):
            established = UNSET
        else:
            established = self.established

        rekey_time: int | None | Unset
        if isinstance(self.rekey_time, Unset):
            rekey_time = UNSET
        else:
            rekey_time = self.rekey_time

        child_sas: list[dict[str, Any]] | None | Unset
        if isinstance(self.child_sas, Unset):
            child_sas = UNSET
        elif isinstance(self.child_sas, list):
            child_sas = []
            for child_sas_type_0_item_data in self.child_sas:
                child_sas_type_0_item = child_sas_type_0_item_data.to_dict()
                child_sas.append(child_sas_type_0_item)

        else:
            child_sas = self.child_sas

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if con_id is not UNSET:
            field_dict["con_id"] = con_id
        if uniqueid is not UNSET:
            field_dict["uniqueid"] = uniqueid
        if version is not UNSET:
            field_dict["version"] = version
        if state is not UNSET:
            field_dict["state"] = state
        if local_host is not UNSET:
            field_dict["local_host"] = local_host
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if local_id is not UNSET:
            field_dict["local_id"] = local_id
        if remote_host is not UNSET:
            field_dict["remote_host"] = remote_host
        if remote_port is not UNSET:
            field_dict["remote_port"] = remote_port
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if initiator_spi is not UNSET:
            field_dict["initiator_spi"] = initiator_spi
        if responder_spi is not UNSET:
            field_dict["responder_spi"] = responder_spi
        if nat_remote is not UNSET:
            field_dict["nat_remote"] = nat_remote
        if nat_any is not UNSET:
            field_dict["nat_any"] = nat_any
        if encr_alg is not UNSET:
            field_dict["encr_alg"] = encr_alg
        if encr_keysize is not UNSET:
            field_dict["encr_keysize"] = encr_keysize
        if integ_alg is not UNSET:
            field_dict["integ_alg"] = integ_alg
        if prf_alg is not UNSET:
            field_dict["prf_alg"] = prf_alg
        if dh_group is not UNSET:
            field_dict["dh_group"] = dh_group
        if established is not UNSET:
            field_dict["established"] = established
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if child_sas is not UNSET:
            field_dict["child_sas"] = child_sas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_psec_sa_status_child_sas_type_0_item import IPsecSAStatusChildSasType0Item

        d = dict(src_dict)

        def _parse_con_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        con_id = _parse_con_id(d.pop("con_id", UNSET))

        def _parse_uniqueid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        uniqueid = _parse_uniqueid(d.pop("uniqueid", UNSET))

        def _parse_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_local_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_host = _parse_local_host(d.pop("local_host", UNSET))

        def _parse_local_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_port = _parse_local_port(d.pop("local_port", UNSET))

        def _parse_local_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_id = _parse_local_id(d.pop("local_id", UNSET))

        def _parse_remote_host(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_host = _parse_remote_host(d.pop("remote_host", UNSET))

        def _parse_remote_port(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_port = _parse_remote_port(d.pop("remote_port", UNSET))

        def _parse_remote_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_id = _parse_remote_id(d.pop("remote_id", UNSET))

        def _parse_initiator_spi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initiator_spi = _parse_initiator_spi(d.pop("initiator_spi", UNSET))

        def _parse_responder_spi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responder_spi = _parse_responder_spi(d.pop("responder_spi", UNSET))

        def _parse_nat_remote(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        nat_remote = _parse_nat_remote(d.pop("nat_remote", UNSET))

        def _parse_nat_any(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        nat_any = _parse_nat_any(d.pop("nat_any", UNSET))

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

        def _parse_prf_alg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prf_alg = _parse_prf_alg(d.pop("prf_alg", UNSET))

        def _parse_dh_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_group = _parse_dh_group(d.pop("dh_group", UNSET))

        def _parse_established(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        established = _parse_established(d.pop("established", UNSET))

        def _parse_rekey_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rekey_time = _parse_rekey_time(d.pop("rekey_time", UNSET))

        def _parse_child_sas(data: object) -> list[IPsecSAStatusChildSasType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                child_sas_type_0 = []
                _child_sas_type_0 = data
                for child_sas_type_0_item_data in _child_sas_type_0:
                    child_sas_type_0_item = IPsecSAStatusChildSasType0Item.from_dict(child_sas_type_0_item_data)

                    child_sas_type_0.append(child_sas_type_0_item)

                return child_sas_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[IPsecSAStatusChildSasType0Item] | None | Unset, data)

        child_sas = _parse_child_sas(d.pop("child_sas", UNSET))

        i_psec_sa_status = cls(
            con_id=con_id,
            uniqueid=uniqueid,
            version=version,
            state=state,
            local_host=local_host,
            local_port=local_port,
            local_id=local_id,
            remote_host=remote_host,
            remote_port=remote_port,
            remote_id=remote_id,
            initiator_spi=initiator_spi,
            responder_spi=responder_spi,
            nat_remote=nat_remote,
            nat_any=nat_any,
            encr_alg=encr_alg,
            encr_keysize=encr_keysize,
            integ_alg=integ_alg,
            prf_alg=prf_alg,
            dh_group=dh_group,
            established=established,
            rekey_time=rekey_time,
            child_sas=child_sas,
        )

        i_psec_sa_status.additional_properties = d
        return i_psec_sa_status

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
