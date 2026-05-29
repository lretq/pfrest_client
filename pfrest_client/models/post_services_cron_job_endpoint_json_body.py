from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostServicesCronJobEndpointJsonBody")


@_attrs_define
class PostServicesCronJobEndpointJsonBody:
    """
    Attributes:
        minute (str): The minute(s) at which the command will be executed or a special @ event string. (0-59, ranges,
            divided, @ event or delay, *=all). When using a special @ event, such as @reboot, the other time fields must be
            empty.<br>
        hour (str): The hour(s) at which the command will be executed. (0-23, ranges, or divided, *=all)<br><br>This
            field is only available when the following conditions are met:<br>- `minute` must not be one of [ @reboot,
            @yearly, @annually, @monthly, @weekly, @daily, @midnight, @hourly, @every_minute, @every_second ]<br>
        mday (str): The day(s) of the month on which the command will be executed. (1-31, ranges, or divided,
            *=all).<br><br>This field is only available when the following conditions are met:<br>- `minute` must not be one
            of [ @reboot, @yearly, @annually, @monthly, @weekly, @daily, @midnight, @hourly, @every_minute, @every_second
            ]<br>
        month (str): The month(s) of the year in which the command will be executed. (1-31, ranges, or divided,
            *=all).<br><br>This field is only available when the following conditions are met:<br>- `minute` must not be one
            of [ @reboot, @yearly, @annually, @monthly, @weekly, @daily, @midnight, @hourly, @every_minute, @every_second
            ]<br>
        wday (str): The day(s) of the week on which the command will be executed. (0-7, 7=Sun or use names, ranges, or
            divided, *=all).<br><br>This field is only available when the following conditions are met:<br>- `minute` must
            not be one of [ @reboot, @yearly, @annually, @monthly, @weekly, @daily, @midnight, @hourly, @every_minute,
            @every_second ]<br>
        who (str): The OS user to use when cron runs the command.<br>
        command (str): The command to run. Use full file paths for this command and include an command parameters.<br>
    """

    minute: str
    hour: str
    mday: str
    month: str
    wday: str
    who: str
    command: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minute = self.minute

        hour = self.hour

        mday = self.mday

        month = self.month

        wday = self.wday

        who = self.who

        command = self.command

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "minute": minute,
                "hour": hour,
                "mday": mday,
                "month": month,
                "wday": wday,
                "who": who,
                "command": command,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minute = d.pop("minute")

        hour = d.pop("hour")

        mday = d.pop("mday")

        month = d.pop("month")

        wday = d.pop("wday")

        who = d.pop("who")

        command = d.pop("command")

        post_services_cron_job_endpoint_json_body = cls(
            minute=minute,
            hour=hour,
            mday=mday,
            month=month,
            wday=wday,
            who=who,
            command=command,
        )

        post_services_cron_job_endpoint_json_body.additional_properties = d
        return post_services_cron_job_endpoint_json_body

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
