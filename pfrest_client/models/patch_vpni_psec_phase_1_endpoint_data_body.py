from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.i_psec_phase_1_authentication_method import IPsecPhase1AuthenticationMethod
from ..models.i_psec_phase_1_closeaction import IPsecPhase1Closeaction
from ..models.i_psec_phase_1_iketype import IPsecPhase1Iketype
from ..models.i_psec_phase_1_mode import IPsecPhase1Mode
from ..models.i_psec_phase_1_myid_type import IPsecPhase1MyidType
from ..models.i_psec_phase_1_nat_traversal import IPsecPhase1NatTraversal
from ..models.i_psec_phase_1_peerid_type import IPsecPhase1PeeridType
from ..models.i_psec_phase_1_protocol import IPsecPhase1Protocol
from ..models.i_psec_phase_1_startaction import IPsecPhase1Startaction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.i_psec_phase_1_encryption_item import IPsecPhase1EncryptionItem


T = TypeVar("T", bound="PatchVPNIPsecPhase1EndpointDataBody")


@_attrs_define
class PatchVPNIPsecPhase1EndpointDataBody:
    """
    Attributes:
        id (int): The ID of the object or resource to interact with.
        ikeid (int | None | Unset): The unique IKE ID for this phase 1 entry. This value is dynamically set and cannot
            be set or changed by users.<br> Default: 26.
        descr (str | Unset): A description for this IPsec phase 1 entry.<br>
        disabled (bool | Unset): Disables this IPsec phase 1 entry.<br>
        iketype (IPsecPhase1Iketype | Unset): The IKE protocol version this phase 1 entry will use.<br>
        mode (IPsecPhase1Mode | Unset): The IKEv1 negotiation mode this phase 1 entry will use.<br><br>This field is
            only available when the following conditions are met:<br>- `iketype` must be one of [ ikev1, auto ]<br>
        protocol (IPsecPhase1Protocol | Unset): The IP version this phase 1 entry will use.<br>
        interface (str | Unset): The interface for the local endpoint of this phase 1 entry. This should be an interface
            that is reachable by the remote peer.<br>
        remote_gateway (str | Unset): The IP address or hostname of the remote gateway.<br>
        authentication_method (IPsecPhase1AuthenticationMethod | Unset): The IPsec authentication method this tunnel
            will use.<br>
        myid_type (IPsecPhase1MyidType | Unset): The identifier type used by the local end of the tunnel.<br>
        myid_data (str | Unset): The identifier value used by the local end of the tunnel. This must be a value that
            corresponds with the current `myid_type` value.<br><br>This field is only available when the following
            conditions are met:<br>- `myid_type` must not be equal to `'myaddress'`<br>
        peerid_type (IPsecPhase1PeeridType | Unset): The identifier type used by the remote end of the tunnel.<br>
        peerid_data (str | Unset): The identifier value used by the remote end of the tunnel. This must be a value that
            corresponds with the current `peerid_type` value.<br><br>This field is only available when the following
            conditions are met:<br>- `peerid_type` must not be one of [ any, peeraddress ]<br>
        pre_shared_key (str | Unset): The Pre-Shared Key (PSK) value. This key must match on both peers and should be
            long and random to protect the tunnel and its contents. A weak Pre-Shared Key can lead to a tunnel
            compromise.<br><br>This field is only available when the following conditions are met:<br>-
            `authentication_method` must be equal to `'pre_shared_key'`<br>
        certref (str | Unset): The certificate which identifies this system. The certificate must have at least one non-
            wildcard SAN.<br><br>This field is only available when the following conditions are met:<br>-
            `authentication_method` must be equal to `'cert'`<br>
        caref (str | Unset): The certificate authority to use when validating the peer certificate.<br><br>This field is
            only available when the following conditions are met:<br>- `authentication_method` must be equal to `'cert'`<br>
        rekey_time (int | Unset): The amount of time (in seconds) before an child SA establishes new keys.<br> Default:
            25920.
        reauth_time (int | Unset): The amount of time (in seconds) before an child SA is torn down and recreated from
            scratch, including authentication.<br>
        rand_time (int | Unset): A random value up to this amount will be subtracted from the `rekey_time` to avoid
            simultaneous renegotiation.<br> Default: 2880.
        lifetime (int | Unset): The hard child SA lifetime (in seconds) after which the child SA will be expired.<br>
            Default: 28800.
        startaction (IPsecPhase1Startaction | Unset): The option used to force specific initiation/responder behavior
            for child SA (P2) entries.<br>
        closeaction (IPsecPhase1Closeaction | Unset): The option used to control the behavior when the remote peer
            unexpectedly closes a child SA (P2)<br>
        nat_traversal (IPsecPhase1NatTraversal | Unset): The option used to enable the use of NAT-T (i.e. the
            encapsulation of ESP in UDP packets) if needed, which can help with clients that are behind restrictive
            firewalls.<br> Default: IPsecPhase1NatTraversal.ON.
        gw_duplicates (bool | Unset): Enables or disables the allowance of multiple phase 1 configurations with the same
            remote gateway endpoint.<br>
        mobike (bool | Unset): Enables or disables the use of MOBIKE for this tunnel.<br>
        splitconn (bool | Unset): Enables or disables the use split connection entries with multiple phase 2
            configurations. Required for remote endpoints that support only a single traffic selector per child SA.<br>
        prfselect_enable (bool | Unset): Enables or disables manual Pseudo-Random Function (PRF) selection.<br>
        ikeport (str | Unset): The UDP port for IKE on the remote gateway. Valid options are: a TCP/UDP port number<br>
            Default: '500'.
        nattport (str | Unset): The UDP port for NAT-T on the remote gateway. Valid options are: a TCP/UDP port
            number<br> Default: '4500'.
        dpd_delay (int | None | Unset): The delay (in seconds) between sending peer acknowledgement messages.<br>
            Default: 10.
        dpd_maxfail (int | None | Unset): The number of consecutive failures allowed before disconnecting.<br> Default:
            5.
        encryption (list[IPsecPhase1EncryptionItem] | Unset): The encryption algorithms supported by this P1
            encryption.<br>
    """

    id: int
    ikeid: int | None | Unset = 26
    descr: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    iketype: IPsecPhase1Iketype | Unset = UNSET
    mode: IPsecPhase1Mode | Unset = UNSET
    protocol: IPsecPhase1Protocol | Unset = UNSET
    interface: str | Unset = UNSET
    remote_gateway: str | Unset = UNSET
    authentication_method: IPsecPhase1AuthenticationMethod | Unset = UNSET
    myid_type: IPsecPhase1MyidType | Unset = UNSET
    myid_data: str | Unset = UNSET
    peerid_type: IPsecPhase1PeeridType | Unset = UNSET
    peerid_data: str | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    certref: str | Unset = UNSET
    caref: str | Unset = UNSET
    rekey_time: int | Unset = 25920
    reauth_time: int | Unset = UNSET
    rand_time: int | Unset = 2880
    lifetime: int | Unset = 28800
    startaction: IPsecPhase1Startaction | Unset = UNSET
    closeaction: IPsecPhase1Closeaction | Unset = UNSET
    nat_traversal: IPsecPhase1NatTraversal | Unset = IPsecPhase1NatTraversal.ON
    gw_duplicates: bool | Unset = UNSET
    mobike: bool | Unset = UNSET
    splitconn: bool | Unset = UNSET
    prfselect_enable: bool | Unset = UNSET
    ikeport: str | Unset = "500"
    nattport: str | Unset = "4500"
    dpd_delay: int | None | Unset = 10
    dpd_maxfail: int | None | Unset = 5
    encryption: list[IPsecPhase1EncryptionItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ikeid: int | None | Unset
        if isinstance(self.ikeid, Unset):
            ikeid = UNSET
        else:
            ikeid = self.ikeid

        descr = self.descr

        disabled = self.disabled

        iketype: str | Unset = UNSET
        if not isinstance(self.iketype, Unset):
            iketype = self.iketype.value

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        interface = self.interface

        remote_gateway = self.remote_gateway

        authentication_method: str | Unset = UNSET
        if not isinstance(self.authentication_method, Unset):
            authentication_method = self.authentication_method.value

        myid_type: str | Unset = UNSET
        if not isinstance(self.myid_type, Unset):
            myid_type = self.myid_type.value

        myid_data = self.myid_data

        peerid_type: str | Unset = UNSET
        if not isinstance(self.peerid_type, Unset):
            peerid_type = self.peerid_type.value

        peerid_data = self.peerid_data

        pre_shared_key = self.pre_shared_key

        certref = self.certref

        caref = self.caref

        rekey_time = self.rekey_time

        reauth_time = self.reauth_time

        rand_time = self.rand_time

        lifetime = self.lifetime

        startaction: str | Unset = UNSET
        if not isinstance(self.startaction, Unset):
            startaction = self.startaction.value

        closeaction: str | Unset = UNSET
        if not isinstance(self.closeaction, Unset):
            closeaction = self.closeaction.value

        nat_traversal: str | Unset = UNSET
        if not isinstance(self.nat_traversal, Unset):
            nat_traversal = self.nat_traversal.value

        gw_duplicates = self.gw_duplicates

        mobike = self.mobike

        splitconn = self.splitconn

        prfselect_enable = self.prfselect_enable

        ikeport = self.ikeport

        nattport = self.nattport

        dpd_delay: int | None | Unset
        if isinstance(self.dpd_delay, Unset):
            dpd_delay = UNSET
        else:
            dpd_delay = self.dpd_delay

        dpd_maxfail: int | None | Unset
        if isinstance(self.dpd_maxfail, Unset):
            dpd_maxfail = UNSET
        else:
            dpd_maxfail = self.dpd_maxfail

        encryption: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = []
            for encryption_item_data in self.encryption:
                encryption_item = encryption_item_data.to_dict()
                encryption.append(encryption_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if ikeid is not UNSET:
            field_dict["ikeid"] = ikeid
        if descr is not UNSET:
            field_dict["descr"] = descr
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if iketype is not UNSET:
            field_dict["iketype"] = iketype
        if mode is not UNSET:
            field_dict["mode"] = mode
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if interface is not UNSET:
            field_dict["interface"] = interface
        if remote_gateway is not UNSET:
            field_dict["remote_gateway"] = remote_gateway
        if authentication_method is not UNSET:
            field_dict["authentication_method"] = authentication_method
        if myid_type is not UNSET:
            field_dict["myid_type"] = myid_type
        if myid_data is not UNSET:
            field_dict["myid_data"] = myid_data
        if peerid_type is not UNSET:
            field_dict["peerid_type"] = peerid_type
        if peerid_data is not UNSET:
            field_dict["peerid_data"] = peerid_data
        if pre_shared_key is not UNSET:
            field_dict["pre_shared_key"] = pre_shared_key
        if certref is not UNSET:
            field_dict["certref"] = certref
        if caref is not UNSET:
            field_dict["caref"] = caref
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if reauth_time is not UNSET:
            field_dict["reauth_time"] = reauth_time
        if rand_time is not UNSET:
            field_dict["rand_time"] = rand_time
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if startaction is not UNSET:
            field_dict["startaction"] = startaction
        if closeaction is not UNSET:
            field_dict["closeaction"] = closeaction
        if nat_traversal is not UNSET:
            field_dict["nat_traversal"] = nat_traversal
        if gw_duplicates is not UNSET:
            field_dict["gw_duplicates"] = gw_duplicates
        if mobike is not UNSET:
            field_dict["mobike"] = mobike
        if splitconn is not UNSET:
            field_dict["splitconn"] = splitconn
        if prfselect_enable is not UNSET:
            field_dict["prfselect_enable"] = prfselect_enable
        if ikeport is not UNSET:
            field_dict["ikeport"] = ikeport
        if nattport is not UNSET:
            field_dict["nattport"] = nattport
        if dpd_delay is not UNSET:
            field_dict["dpd_delay"] = dpd_delay
        if dpd_maxfail is not UNSET:
            field_dict["dpd_maxfail"] = dpd_maxfail
        if encryption is not UNSET:
            field_dict["encryption"] = encryption

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.i_psec_phase_1_encryption_item import IPsecPhase1EncryptionItem

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_ikeid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ikeid = _parse_ikeid(d.pop("ikeid", UNSET))

        descr = d.pop("descr", UNSET)

        disabled = d.pop("disabled", UNSET)

        _iketype = d.pop("iketype", UNSET)
        iketype: IPsecPhase1Iketype | Unset
        if isinstance(_iketype, Unset):
            iketype = UNSET
        else:
            iketype = IPsecPhase1Iketype(_iketype)

        _mode = d.pop("mode", UNSET)
        mode: IPsecPhase1Mode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = IPsecPhase1Mode(_mode)

        _protocol = d.pop("protocol", UNSET)
        protocol: IPsecPhase1Protocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = IPsecPhase1Protocol(_protocol)

        interface = d.pop("interface", UNSET)

        remote_gateway = d.pop("remote_gateway", UNSET)

        _authentication_method = d.pop("authentication_method", UNSET)
        authentication_method: IPsecPhase1AuthenticationMethod | Unset
        if isinstance(_authentication_method, Unset):
            authentication_method = UNSET
        else:
            authentication_method = IPsecPhase1AuthenticationMethod(_authentication_method)

        _myid_type = d.pop("myid_type", UNSET)
        myid_type: IPsecPhase1MyidType | Unset
        if isinstance(_myid_type, Unset):
            myid_type = UNSET
        else:
            myid_type = IPsecPhase1MyidType(_myid_type)

        myid_data = d.pop("myid_data", UNSET)

        _peerid_type = d.pop("peerid_type", UNSET)
        peerid_type: IPsecPhase1PeeridType | Unset
        if isinstance(_peerid_type, Unset):
            peerid_type = UNSET
        else:
            peerid_type = IPsecPhase1PeeridType(_peerid_type)

        peerid_data = d.pop("peerid_data", UNSET)

        pre_shared_key = d.pop("pre_shared_key", UNSET)

        certref = d.pop("certref", UNSET)

        caref = d.pop("caref", UNSET)

        rekey_time = d.pop("rekey_time", UNSET)

        reauth_time = d.pop("reauth_time", UNSET)

        rand_time = d.pop("rand_time", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        _startaction = d.pop("startaction", UNSET)
        startaction: IPsecPhase1Startaction | Unset
        if isinstance(_startaction, Unset):
            startaction = UNSET
        else:
            startaction = IPsecPhase1Startaction(_startaction)

        _closeaction = d.pop("closeaction", UNSET)
        closeaction: IPsecPhase1Closeaction | Unset
        if isinstance(_closeaction, Unset):
            closeaction = UNSET
        else:
            closeaction = IPsecPhase1Closeaction(_closeaction)

        _nat_traversal = d.pop("nat_traversal", UNSET)
        nat_traversal: IPsecPhase1NatTraversal | Unset
        if isinstance(_nat_traversal, Unset):
            nat_traversal = UNSET
        else:
            nat_traversal = IPsecPhase1NatTraversal(_nat_traversal)

        gw_duplicates = d.pop("gw_duplicates", UNSET)

        mobike = d.pop("mobike", UNSET)

        splitconn = d.pop("splitconn", UNSET)

        prfselect_enable = d.pop("prfselect_enable", UNSET)

        ikeport = d.pop("ikeport", UNSET)

        nattport = d.pop("nattport", UNSET)

        def _parse_dpd_delay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dpd_delay = _parse_dpd_delay(d.pop("dpd_delay", UNSET))

        def _parse_dpd_maxfail(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dpd_maxfail = _parse_dpd_maxfail(d.pop("dpd_maxfail", UNSET))

        _encryption = d.pop("encryption", UNSET)
        encryption: list[IPsecPhase1EncryptionItem] | Unset = UNSET
        if _encryption is not UNSET:
            encryption = []
            for encryption_item_data in _encryption:
                encryption_item = IPsecPhase1EncryptionItem.from_dict(encryption_item_data)

                encryption.append(encryption_item)

        patch_vpni_psec_phase_1_endpoint_data_body = cls(
            id=id,
            ikeid=ikeid,
            descr=descr,
            disabled=disabled,
            iketype=iketype,
            mode=mode,
            protocol=protocol,
            interface=interface,
            remote_gateway=remote_gateway,
            authentication_method=authentication_method,
            myid_type=myid_type,
            myid_data=myid_data,
            peerid_type=peerid_type,
            peerid_data=peerid_data,
            pre_shared_key=pre_shared_key,
            certref=certref,
            caref=caref,
            rekey_time=rekey_time,
            reauth_time=reauth_time,
            rand_time=rand_time,
            lifetime=lifetime,
            startaction=startaction,
            closeaction=closeaction,
            nat_traversal=nat_traversal,
            gw_duplicates=gw_duplicates,
            mobike=mobike,
            splitconn=splitconn,
            prfselect_enable=prfselect_enable,
            ikeport=ikeport,
            nattport=nattport,
            dpd_delay=dpd_delay,
            dpd_maxfail=dpd_maxfail,
            encryption=encryption,
        )

        patch_vpni_psec_phase_1_endpoint_data_body.additional_properties = d
        return patch_vpni_psec_phase_1_endpoint_data_body

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
