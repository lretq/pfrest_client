from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.i_psec_phase_2_hash_algorithm_option_item import IPsecPhase2HashAlgorithmOptionItem
from ..models.i_psec_phase_2_mode import IPsecPhase2Mode
from ..models.i_psec_phase_2_pfsgroup import IPsecPhase2Pfsgroup
from ..models.i_psec_phase_2_protocol import IPsecPhase2Protocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_psec_phase_2_encryption_algorithm_option_item import IPsecPhase2EncryptionAlgorithmOptionItem


T = TypeVar("T", bound="PutVPNIPsecPhase2SEndpointJsonBodyItem")


@_attrs_define
class PutVPNIPsecPhase2SEndpointJsonBodyItem:
    """
    Attributes:
        ikeid (int): The `ikeid` of the parent IPsec phase 1 entry this IPsec phase 2 entry belongs to.<br>
        mode (IPsecPhase2Mode): The IPsec phase 2 mode this entry will use.<br>
        localid_type (str): The local ID type to use for this phase 2 entry. Valid value options are: an existing
            interface, `address`, `network`. For interface values, the `:ip`  modifier can be appended to the value to use
            the interface's IP address instead of its entire subnet.<br><br>This field is only available when the following
            conditions are met:<br>- `mode` must not be equal to `'transport'`<br>
        localid_address (str): The local network IP component of this IPsec security association.<br><br>This field is
            only available when the following conditions are met:<br>- `localid_type` must be one of [ address, network
            ]<br>
        localid_netbits (int): The subnet bits of the `localid_address` network.<br><br>This field is only available
            when the following conditions are met:<br>- `localid_type` must be equal to `'network'`<br>
        natlocalid_address (str): The NAT/BINAT local network IP component of this IPsec security
            association.<br><br>This field is only available when the following conditions are met:<br>- `natlocalid_type`
            must be one of [ address, network ]<br>
        natlocalid_netbits (int): The subnet bits of the `natlocalid_address` network.<br><br>This field is only
            available when the following conditions are met:<br>- `natlocalid_type` must be equal to `'network'`<br>
        remoteid_type (str): The remote ID type to use for this phase 2 entry. Valid value options are: `address`,
            `network`. For interface values, the `:ip`  modifier can be appended to the value to use the interface's IP
            address instead of its entire subnet.<br><br>This field is only available when the following conditions are
            met:<br>- `mode` must not be equal to `'transport'`<br>
        remoteid_address (str): The remote network IP component of this IPsec security association.<br><br>This field is
            only available when the following conditions are met:<br>- `remoteid_type` must be one of [ address, network
            ]<br>
        remoteid_netbits (int): The subnet bits of the `remoteid_address` network.<br><br>This field is only available
            when the following conditions are met:<br>- `remoteid_type` must be equal to `'network'`<br>
        encryption_algorithm_option (list[IPsecPhase2EncryptionAlgorithmOptionItem]): The encryption algorithms to be
            used by this phase 2 entry.<br><br>This field is only available when the following conditions are met:<br>-
            `protocol` must be equal to `'esp'`<br>
        hash_algorithm_option (list[IPsecPhase2HashAlgorithmOptionItem]): The hashing algorithms used by this IPsec
            phase 2 entry. Note: Hash is ignored with GCM algorithms. SHA1 provides weak security and should be avoided.<br>
        uniqid (None | str | Unset): A unique ID used to identify this IPsec phase2 entry internally. This value is
            automatically set by the system and cannot be changed.<br>
        reqid (int | None | Unset): A unique ID used to identify this IPsec phase2 entry internally. This value is
            automatically set by the system and cannot be changed.<br> Default: 62.
        descr (str | Unset): A description for this IPsec phase 2 entry.<br>
        disabled (bool | Unset): Disables this IPsec phase 2 entry.<br>
        natlocalid_type (None | str | Unset): The NAT/BINAT translation type for this IPsec phase 2 entry. Leave as
            `null` if NAT/BINAT is not needed. Valid value options are: an existing interface, `address`, `network`. For
            interface values, the `:ip`  modifier can be appended to the value to use the interface's IP address instead of
            its entire subnet.<br><br>This field is only available when the following conditions are met:<br>- `mode` must
            not be one of [ transport, vti ]<br>
        protocol (IPsecPhase2Protocol | Unset): the IPsec phase 2 proposal protocol for this entry. Encapsulating
            Security Payload (`esp`) performs encryption and authentication, Authentication Header (`ah`) is authentication
            only.<br> Default: IPsecPhase2Protocol.ESP.
        pfsgroup (IPsecPhase2Pfsgroup | Unset): The PFS key group this IPsec phase 2 entry should use. Note: Groups 1,
            2, 5, 22, 23, and 24 provide weak security and should be avoided.<br> Default: IPsecPhase2Pfsgroup.VALUE_14.
        rekey_time (int | Unset): The amount of time (in seconds) before an IKE SA establishes new keys.<br> Default:
            3240.
        rand_time (int | Unset): A random value up to this amount will be subtracted from the `rekey_time` and
            `reauth_time` to avoid simultaneous renegotiation.<br> Default: 360.
        lifetime (int | Unset): The hard IKE SA lifetime (in seconds) after which the IKE SA will be expired.<br>
            Default: 3600.
        pinghost (str | Unset): The IP address to send an ICMP echo request to inside the tunnel. Can trigger initiation
            of a tunnel mode P2, but does not trigger initiation of a VTI mode P2.<br>
        keepalive (bool | Unset): Enables or disables checking this P2 and initiating if disconnected; does not send
            traffic inside the tunnel. This check ignores the P1 option 'Child SA Start Action' and works for both VTI and
            tunnel mode P2s. For IKEv2 without split connections, this only needs to be enabled on one P2.<br>
    """

    ikeid: int
    mode: IPsecPhase2Mode
    localid_type: str
    localid_address: str
    localid_netbits: int
    natlocalid_address: str
    natlocalid_netbits: int
    remoteid_type: str
    remoteid_address: str
    remoteid_netbits: int
    encryption_algorithm_option: list[IPsecPhase2EncryptionAlgorithmOptionItem]
    hash_algorithm_option: list[IPsecPhase2HashAlgorithmOptionItem]
    uniqid: None | str | Unset = UNSET
    reqid: int | None | Unset = 62
    descr: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    natlocalid_type: None | str | Unset = UNSET
    protocol: IPsecPhase2Protocol | Unset = IPsecPhase2Protocol.ESP
    pfsgroup: IPsecPhase2Pfsgroup | Unset = IPsecPhase2Pfsgroup.VALUE_14
    rekey_time: int | Unset = 3240
    rand_time: int | Unset = 360
    lifetime: int | Unset = 3600
    pinghost: str | Unset = UNSET
    keepalive: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ikeid = self.ikeid

        mode = self.mode.value

        localid_type = self.localid_type

        localid_address = self.localid_address

        localid_netbits = self.localid_netbits

        natlocalid_address = self.natlocalid_address

        natlocalid_netbits = self.natlocalid_netbits

        remoteid_type = self.remoteid_type

        remoteid_address = self.remoteid_address

        remoteid_netbits = self.remoteid_netbits

        encryption_algorithm_option = []
        for encryption_algorithm_option_item_data in self.encryption_algorithm_option:
            encryption_algorithm_option_item = encryption_algorithm_option_item_data.to_dict()
            encryption_algorithm_option.append(encryption_algorithm_option_item)

        hash_algorithm_option = []
        for hash_algorithm_option_item_data in self.hash_algorithm_option:
            hash_algorithm_option_item = hash_algorithm_option_item_data.value
            hash_algorithm_option.append(hash_algorithm_option_item)

        uniqid: None | str | Unset
        if isinstance(self.uniqid, Unset):
            uniqid = UNSET
        else:
            uniqid = self.uniqid

        reqid: int | None | Unset
        if isinstance(self.reqid, Unset):
            reqid = UNSET
        else:
            reqid = self.reqid

        descr = self.descr

        disabled = self.disabled

        natlocalid_type: None | str | Unset
        if isinstance(self.natlocalid_type, Unset):
            natlocalid_type = UNSET
        else:
            natlocalid_type = self.natlocalid_type

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        pfsgroup: int | Unset = UNSET
        if not isinstance(self.pfsgroup, Unset):
            pfsgroup = self.pfsgroup.value

        rekey_time = self.rekey_time

        rand_time = self.rand_time

        lifetime = self.lifetime

        pinghost = self.pinghost

        keepalive = self.keepalive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ikeid": ikeid,
                "mode": mode,
                "localid_type": localid_type,
                "localid_address": localid_address,
                "localid_netbits": localid_netbits,
                "natlocalid_address": natlocalid_address,
                "natlocalid_netbits": natlocalid_netbits,
                "remoteid_type": remoteid_type,
                "remoteid_address": remoteid_address,
                "remoteid_netbits": remoteid_netbits,
                "encryption_algorithm_option": encryption_algorithm_option,
                "hash_algorithm_option": hash_algorithm_option,
            }
        )
        if uniqid is not UNSET:
            field_dict["uniqid"] = uniqid
        if reqid is not UNSET:
            field_dict["reqid"] = reqid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if natlocalid_type is not UNSET:
            field_dict["natlocalid_type"] = natlocalid_type
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if pfsgroup is not UNSET:
            field_dict["pfsgroup"] = pfsgroup
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if rand_time is not UNSET:
            field_dict["rand_time"] = rand_time
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if pinghost is not UNSET:
            field_dict["pinghost"] = pinghost
        if keepalive is not UNSET:
            field_dict["keepalive"] = keepalive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_psec_phase_2_encryption_algorithm_option_item import IPsecPhase2EncryptionAlgorithmOptionItem

        d = dict(src_dict)
        ikeid = d.pop("ikeid")

        mode = IPsecPhase2Mode(d.pop("mode"))

        localid_type = d.pop("localid_type")

        localid_address = d.pop("localid_address")

        localid_netbits = d.pop("localid_netbits")

        natlocalid_address = d.pop("natlocalid_address")

        natlocalid_netbits = d.pop("natlocalid_netbits")

        remoteid_type = d.pop("remoteid_type")

        remoteid_address = d.pop("remoteid_address")

        remoteid_netbits = d.pop("remoteid_netbits")

        encryption_algorithm_option = []
        _encryption_algorithm_option = d.pop("encryption_algorithm_option")
        for encryption_algorithm_option_item_data in _encryption_algorithm_option:
            encryption_algorithm_option_item = IPsecPhase2EncryptionAlgorithmOptionItem.from_dict(
                encryption_algorithm_option_item_data
            )

            encryption_algorithm_option.append(encryption_algorithm_option_item)

        hash_algorithm_option = []
        _hash_algorithm_option = d.pop("hash_algorithm_option")
        for hash_algorithm_option_item_data in _hash_algorithm_option:
            hash_algorithm_option_item = IPsecPhase2HashAlgorithmOptionItem(hash_algorithm_option_item_data)

            hash_algorithm_option.append(hash_algorithm_option_item)

        def _parse_uniqid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uniqid = _parse_uniqid(d.pop("uniqid", UNSET))

        def _parse_reqid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reqid = _parse_reqid(d.pop("reqid", UNSET))

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        def _parse_natlocalid_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        natlocalid_type = _parse_natlocalid_type(d.pop("natlocalid_type", UNSET))

        _protocol = d.pop("protocol", UNSET)
        protocol: IPsecPhase2Protocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = IPsecPhase2Protocol(_protocol)

        _pfsgroup = d.pop("pfsgroup", UNSET)
        pfsgroup: IPsecPhase2Pfsgroup | Unset
        if isinstance(_pfsgroup, Unset):
            pfsgroup = UNSET
        else:
            pfsgroup = IPsecPhase2Pfsgroup(_pfsgroup)

        rekey_time = d.pop("rekey_time", UNSET)

        rand_time = d.pop("rand_time", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        pinghost = d.pop("pinghost", UNSET)

        keepalive = d.pop("keepalive", UNSET)

        put_vpni_psec_phase_2s_endpoint_json_body_item = cls(
            ikeid=ikeid,
            mode=mode,
            localid_type=localid_type,
            localid_address=localid_address,
            localid_netbits=localid_netbits,
            natlocalid_address=natlocalid_address,
            natlocalid_netbits=natlocalid_netbits,
            remoteid_type=remoteid_type,
            remoteid_address=remoteid_address,
            remoteid_netbits=remoteid_netbits,
            encryption_algorithm_option=encryption_algorithm_option,
            hash_algorithm_option=hash_algorithm_option,
            uniqid=uniqid,
            reqid=reqid,
            descr=descr,
            disabled=disabled,
            natlocalid_type=natlocalid_type,
            protocol=protocol,
            pfsgroup=pfsgroup,
            rekey_time=rekey_time,
            rand_time=rand_time,
            lifetime=lifetime,
            pinghost=pinghost,
            keepalive=keepalive,
        )

        put_vpni_psec_phase_2s_endpoint_json_body_item.additional_properties = d
        return put_vpni_psec_phase_2s_endpoint_json_body_item

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
