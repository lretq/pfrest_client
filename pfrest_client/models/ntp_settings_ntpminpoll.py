from enum import Enum


class NTPSettingsNtpminpoll(str, Enum):
    OMIT = "omit"
    VALUE_0 = ""
    VALUE_1 = "3"
    VALUE_10 = "12"
    VALUE_11 = "13"
    VALUE_12 = "14"
    VALUE_13 = "15"
    VALUE_14 = "16"
    VALUE_15 = "17"
    VALUE_2 = "4"
    VALUE_3 = "5"
    VALUE_4 = "6"
    VALUE_5 = "7"
    VALUE_6 = "8"
    VALUE_7 = "9"
    VALUE_8 = "10"
    VALUE_9 = "11"

    def __str__(self) -> str:
        return str(self.value)
