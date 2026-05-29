from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemStatus")


@_attrs_define
class SystemStatus:
    """
    Attributes:
        platform (None | str | Unset): The verbose name of this system's platform.<br>
        serial (None | str | Unset): The system's unique serial number/ID.<br>
        netgate_id (None | str | Unset): The unique ID issued for this pfSense instance by Netgate.<br>
        uptime (None | str | Unset): The amount of time this system has been up since the last reboot.<br>
        bios_vendor (None | str | Unset): The name of the BIOS vendor.<br>
        bios_version (None | str | Unset): The BIOS version installed on this system.<br>
        bios_date (None | str | Unset): The build date of the BIOS version.<br>
        kernel_pti (bool | None | Unset): Indicates whether kernel PTI is enabled or not.<br>
        mds_mitigation (None | str | Unset): Indicates whether MDS mitigation is enabled or not.<br>
        temp_c (float | None | Unset): The current system temperature in celsius.<br>
        temp_f (float | None | Unset): The current system temperature in fahrenheit.<br>
        cpu_model (None | str | Unset): The model of CPU installed in this system and other CPU info.<br>
        cpu_load_avg (list[float] | None | Unset): The CPU load averages. The first value represents the load average
            for the last minute, the second value represents the load average for the last 5 minutes, and the third value
            represents the load average for the last 15 minutes.<br>
        cpu_count (int | None | Unset): The total number of CPUs cores available on this system.<br>
        cpu_usage (float | None | Unset): The current CPU usage as a whole percentage. Note: This is an approximate
            usage based on the last minute load average and total number of CPU cores. This may not represent exact CPU
            usage.<br>
        mbuf_usage (float | None | Unset): The current MBUF usage as a whole percentage.<br>
        mem_usage (float | None | Unset): The current memory usage as a whole percentage.<br>
        swap_usage (float | None | Unset): The current swap usage as a whole percentage.<br>
        disk_usage (float | None | Unset): The current disk usage as a whole percentage.<br>
    """

    platform: None | str | Unset = UNSET
    serial: None | str | Unset = UNSET
    netgate_id: None | str | Unset = UNSET
    uptime: None | str | Unset = UNSET
    bios_vendor: None | str | Unset = UNSET
    bios_version: None | str | Unset = UNSET
    bios_date: None | str | Unset = UNSET
    kernel_pti: bool | None | Unset = UNSET
    mds_mitigation: None | str | Unset = UNSET
    temp_c: float | None | Unset = UNSET
    temp_f: float | None | Unset = UNSET
    cpu_model: None | str | Unset = UNSET
    cpu_load_avg: list[float] | None | Unset = UNSET
    cpu_count: int | None | Unset = UNSET
    cpu_usage: float | None | Unset = UNSET
    mbuf_usage: float | None | Unset = UNSET
    mem_usage: float | None | Unset = UNSET
    swap_usage: float | None | Unset = UNSET
    disk_usage: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        serial: None | str | Unset
        if isinstance(self.serial, Unset):
            serial = UNSET
        else:
            serial = self.serial

        netgate_id: None | str | Unset
        if isinstance(self.netgate_id, Unset):
            netgate_id = UNSET
        else:
            netgate_id = self.netgate_id

        uptime: None | str | Unset
        if isinstance(self.uptime, Unset):
            uptime = UNSET
        else:
            uptime = self.uptime

        bios_vendor: None | str | Unset
        if isinstance(self.bios_vendor, Unset):
            bios_vendor = UNSET
        else:
            bios_vendor = self.bios_vendor

        bios_version: None | str | Unset
        if isinstance(self.bios_version, Unset):
            bios_version = UNSET
        else:
            bios_version = self.bios_version

        bios_date: None | str | Unset
        if isinstance(self.bios_date, Unset):
            bios_date = UNSET
        else:
            bios_date = self.bios_date

        kernel_pti: bool | None | Unset
        if isinstance(self.kernel_pti, Unset):
            kernel_pti = UNSET
        else:
            kernel_pti = self.kernel_pti

        mds_mitigation: None | str | Unset
        if isinstance(self.mds_mitigation, Unset):
            mds_mitigation = UNSET
        else:
            mds_mitigation = self.mds_mitigation

        temp_c: float | None | Unset
        if isinstance(self.temp_c, Unset):
            temp_c = UNSET
        else:
            temp_c = self.temp_c

        temp_f: float | None | Unset
        if isinstance(self.temp_f, Unset):
            temp_f = UNSET
        else:
            temp_f = self.temp_f

        cpu_model: None | str | Unset
        if isinstance(self.cpu_model, Unset):
            cpu_model = UNSET
        else:
            cpu_model = self.cpu_model

        cpu_load_avg: list[float] | None | Unset
        if isinstance(self.cpu_load_avg, Unset):
            cpu_load_avg = UNSET
        elif isinstance(self.cpu_load_avg, list):
            cpu_load_avg = self.cpu_load_avg

        else:
            cpu_load_avg = self.cpu_load_avg

        cpu_count: int | None | Unset
        if isinstance(self.cpu_count, Unset):
            cpu_count = UNSET
        else:
            cpu_count = self.cpu_count

        cpu_usage: float | None | Unset
        if isinstance(self.cpu_usage, Unset):
            cpu_usage = UNSET
        else:
            cpu_usage = self.cpu_usage

        mbuf_usage: float | None | Unset
        if isinstance(self.mbuf_usage, Unset):
            mbuf_usage = UNSET
        else:
            mbuf_usage = self.mbuf_usage

        mem_usage: float | None | Unset
        if isinstance(self.mem_usage, Unset):
            mem_usage = UNSET
        else:
            mem_usage = self.mem_usage

        swap_usage: float | None | Unset
        if isinstance(self.swap_usage, Unset):
            swap_usage = UNSET
        else:
            swap_usage = self.swap_usage

        disk_usage: float | None | Unset
        if isinstance(self.disk_usage, Unset):
            disk_usage = UNSET
        else:
            disk_usage = self.disk_usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["platform"] = platform
        if serial is not UNSET:
            field_dict["serial"] = serial
        if netgate_id is not UNSET:
            field_dict["netgate_id"] = netgate_id
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if bios_vendor is not UNSET:
            field_dict["bios_vendor"] = bios_vendor
        if bios_version is not UNSET:
            field_dict["bios_version"] = bios_version
        if bios_date is not UNSET:
            field_dict["bios_date"] = bios_date
        if kernel_pti is not UNSET:
            field_dict["kernel_pti"] = kernel_pti
        if mds_mitigation is not UNSET:
            field_dict["mds_mitigation"] = mds_mitigation
        if temp_c is not UNSET:
            field_dict["temp_c"] = temp_c
        if temp_f is not UNSET:
            field_dict["temp_f"] = temp_f
        if cpu_model is not UNSET:
            field_dict["cpu_model"] = cpu_model
        if cpu_load_avg is not UNSET:
            field_dict["cpu_load_avg"] = cpu_load_avg
        if cpu_count is not UNSET:
            field_dict["cpu_count"] = cpu_count
        if cpu_usage is not UNSET:
            field_dict["cpu_usage"] = cpu_usage
        if mbuf_usage is not UNSET:
            field_dict["mbuf_usage"] = mbuf_usage
        if mem_usage is not UNSET:
            field_dict["mem_usage"] = mem_usage
        if swap_usage is not UNSET:
            field_dict["swap_usage"] = swap_usage
        if disk_usage is not UNSET:
            field_dict["disk_usage"] = disk_usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_serial(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial = _parse_serial(d.pop("serial", UNSET))

        def _parse_netgate_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        netgate_id = _parse_netgate_id(d.pop("netgate_id", UNSET))

        def _parse_uptime(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uptime = _parse_uptime(d.pop("uptime", UNSET))

        def _parse_bios_vendor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bios_vendor = _parse_bios_vendor(d.pop("bios_vendor", UNSET))

        def _parse_bios_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bios_version = _parse_bios_version(d.pop("bios_version", UNSET))

        def _parse_bios_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bios_date = _parse_bios_date(d.pop("bios_date", UNSET))

        def _parse_kernel_pti(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        kernel_pti = _parse_kernel_pti(d.pop("kernel_pti", UNSET))

        def _parse_mds_mitigation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mds_mitigation = _parse_mds_mitigation(d.pop("mds_mitigation", UNSET))

        def _parse_temp_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temp_c = _parse_temp_c(d.pop("temp_c", UNSET))

        def _parse_temp_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temp_f = _parse_temp_f(d.pop("temp_f", UNSET))

        def _parse_cpu_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cpu_model = _parse_cpu_model(d.pop("cpu_model", UNSET))

        def _parse_cpu_load_avg(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cpu_load_avg_type_0 = cast(list[float], data)

                return cpu_load_avg_type_0
            except TypeError, ValueError, AttributeError, KeyError:
                pass
            return cast(list[float] | None | Unset, data)

        cpu_load_avg = _parse_cpu_load_avg(d.pop("cpu_load_avg", UNSET))

        def _parse_cpu_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_count = _parse_cpu_count(d.pop("cpu_count", UNSET))

        def _parse_cpu_usage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cpu_usage = _parse_cpu_usage(d.pop("cpu_usage", UNSET))

        def _parse_mbuf_usage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mbuf_usage = _parse_mbuf_usage(d.pop("mbuf_usage", UNSET))

        def _parse_mem_usage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mem_usage = _parse_mem_usage(d.pop("mem_usage", UNSET))

        def _parse_swap_usage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        swap_usage = _parse_swap_usage(d.pop("swap_usage", UNSET))

        def _parse_disk_usage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        disk_usage = _parse_disk_usage(d.pop("disk_usage", UNSET))

        system_status = cls(
            platform=platform,
            serial=serial,
            netgate_id=netgate_id,
            uptime=uptime,
            bios_vendor=bios_vendor,
            bios_version=bios_version,
            bios_date=bios_date,
            kernel_pti=kernel_pti,
            mds_mitigation=mds_mitigation,
            temp_c=temp_c,
            temp_f=temp_f,
            cpu_model=cpu_model,
            cpu_load_avg=cpu_load_avg,
            cpu_count=cpu_count,
            cpu_usage=cpu_usage,
            mbuf_usage=mbuf_usage,
            mem_usage=mem_usage,
            swap_usage=swap_usage,
            disk_usage=disk_usage,
        )

        system_status.additional_properties = d
        return system_status

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
