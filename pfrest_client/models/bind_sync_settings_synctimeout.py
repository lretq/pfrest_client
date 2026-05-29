from enum import IntEnum


class BINDSyncSettingsSynctimeout(IntEnum):
    VALUE_30 = 30
    VALUE_60 = 60
    VALUE_90 = 90
    VALUE_120 = 120
    VALUE_150 = 150
    VALUE_250 = 250

    def __str__(self) -> str:
        return str(self.value)
