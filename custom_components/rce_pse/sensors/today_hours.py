from __future__ import annotations

from typing import TYPE_CHECKING

from .base import RCEBaseSensor

if TYPE_CHECKING:
    from ..coordinator import RCEPSEDataUpdateCoordinator


class RCETodayHoursSensor(RCEBaseSensor):

    def __init__(self, coordinator: RCEPSEDataUpdateCoordinator, unique_id: str) -> None:
        super().__init__(coordinator, unique_id)
        self._attr_icon = "mdi:clock"


class RCETodayMaxPriceHourStartSensor(RCETodayHoursSensor):

    def __init__(self, coordinator: RCEPSEDataUpdateCoordinator) -> None:
        super().__init__(coordinator, "today_max_price_hour_start")

    @property
    def native_value(self) -> str | None:
        today_data = self.get_today_data()
        if not today_data:
            return None
        
        max_price_records = self.calculator.find_extreme_price_records(today_data, is_max=True)
        return max_price_records[0]["period"].split(" - ")[0] if max_price_records else None


class RCETodayMaxPriceHourEndSensor(RCETodayHoursSensor):

    def __init__(self, coordinator: RCEPSEDataUpdateCoordinator) -> None:
        super().__init__(coordinator, "today_max_price_hour_end")

    @property
    def native_value(self) -> str | None:
        today_data = self.get_today_data()
        if not today_data:
            return None
        
        max_price_records = self.calculator.find_extreme_price_records(today_data, is_max=True)
        return max_price_records[-1]["period"].split(" - ")[1] if max_price_records else None


class RCETodayMinPriceHourStartSensor(RCETodayHoursSensor):

    def __init__(self, coordinator: RCEPSEDataUpdateCoordinator) -> None:
        super().__init__(coordinator, "today_min_price_hour_start")

    @property
    def native_value(self) -> str | None:
        today_data = self.get_today_data()
        if not today_data:
            return None
        
        min_price_records = self.calculator.find_extreme_price_records(today_data, is_max=False)
        return min_price_records[0]["period"].split(" - ")[0] if min_price_records else None


class RCETodayMinPriceHourEndSensor(RCETodayHoursSensor):

    def __init__(self, coordinator: RCEPSEDataUpdateCoordinator) -> None:
        super().__init__(coordinator, "today_min_price_hour_end")

    @property
    def native_value(self) -> str | None:
        today_data = self.get_today_data()
        if not today_data:
            return None
        
        min_price_records = self.calculator.find_extreme_price_records(today_data, is_max=False)
        return min_price_records[-1]["period"].split(" - ")[1] if min_price_records else None


class RCETodayMinPriceRangeSensor(RCETodayHoursSensor):

    def __init__(self, coordinator: RCEPSEDataUpdateCoordinator) -> None:
        super().__init__(coordinator, "today_min_price_range")
        self._attr_icon = "mdi:clock-time-four"

    @property
    def native_value(self) -> str | None:
        today_data = self.get_today_data()
        if not today_data:
            return None
        
        min_price_records = self.calculator.find_extreme_price_records(today_data, is_max=False)
        if not min_price_records:
            return None
            
        start_time = min_price_records[0]["period"].split(" - ")[0]
        end_time = min_price_records[-1]["period"].split(" - ")[1]
        return f"{start_time} - {end_time}"


class RCETodayMaxPriceRangeSensor(RCETodayHoursSensor):

    def __init__(self, coordinator: RCEPSEDataUpdateCoordinator) -> None:
        super().__init__(coordinator, "today_max_price_range")
        self._attr_icon = "mdi:clock-time-four"

    @property
    def native_value(self) -> str | None:
        today_data = self.get_today_data()
        if not today_data:
            return None
        
        max_price_records = self.calculator.find_extreme_price_records(today_data, is_max=True)
        if not max_price_records:
            return None
            
        start_time = max_price_records[0]["period"].split(" - ")[0]
        end_time = max_price_records[-1]["period"].split(" - ")[1]
        return f"{start_time} - {end_time}" 