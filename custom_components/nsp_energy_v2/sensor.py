from datetime import datetime, timedelta
import homeassistant.util.dt as dt_util
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.const import CURRENCY_DOLLAR
from .const import *

async def async_setup_entry(hass, entry, async_add_entities):
    conf = {**entry.data, **entry.options}
    tax = 1.15 if conf.get(CONF_INCLUDE_TAX, True) else 1.0
    
    prices = {
        "Peak": conf.get(CONF_PEAK_PRICE, DEFAULT_PEAK) * tax,
        "Mid-Peak": conf.get(CONF_MID_PEAK_PRICE, DEFAULT_MID) * tax,
        "Off-Peak": conf.get(CONF_OFF_PEAK_PRICE, DEFAULT_OFF) * tax
    }

    async_add_entities([
        NSPPriceSensor(entry, prices, "NSP Current Price", 0),
        NSPStatusSensor(entry, "NSP Current Period", 0),
        NSPStatusSensor(entry, "NSP Next Period", 1),
        NSPPriceSensor(entry, prices, "NSP Next Price", 1),
        NSPTaxSensor(entry, conf.get(CONF_INCLUDE_TAX, True))
    ])

def get_nsp_period(offset_hours=0):
    now = dt_util.now() + timedelta(hours=offset_hours)
    month, hour, day = now.month, now.hour, now.weekday()
    if day >= 5: return "Off-Peak"
    if month in [12, 1, 2]:
        if (7 <= hour < 12) or (16 <= hour < 23): return "Peak"
        if 12 <= hour < 16: return "Mid-Peak"
        return "Off-Peak"
    return "Mid-Peak" if 7 <= hour < 23 else "Off-Peak"

class NSPPriceSensor(SensorEntity):
    def __init__(self, entry, prices, name, offset):
        self._prices, self._attr_name, self._offset = prices, name, offset
        self._attr_unique_id = f"nsp_v2_{entry.entry_id}_{name.lower().replace(' ', '_')}"
        self._attr_native_unit_of_measurement = f"{CURRENCY_DOLLAR}/kWh"
        self._attr_device_class = SensorDeviceClass.MONETARY
    @property
    def native_value(self): 
        return round(self._prices.get(get_nsp_period(self._offset)), 5)

class NSPStatusSensor(SensorEntity):
    def __init__(self, entry, name, offset):
        self._attr_name, self._offset = name, offset
        self._attr_unique_id = f"nsp_v2_{entry.entry_id}_{name.lower().replace(' ', '_')}"
    @property
    def native_value(self): return get_nsp_period(self._offset)

class NSPTaxSensor(SensorEntity):
    def __init__(self, entry, active):
        self._attr_name = "NSP Tax Active"
        self._attr_unique_id = f"nsp_v2_{entry.entry_id}_tax_status"
        self._state = "Yes (15%)" if active else "No"
    @property
    def native_value(self): return self._state