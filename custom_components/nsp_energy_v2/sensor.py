from homeassistant.components.sensor import SensorEntity
from datetime import datetime, timedelta
from .const import DOMAIN, CONF_PEAK_PRICE, CONF_MID_PRICE, CONF_OFFPEAK_PRICE, CONF_INCLUDE_TAX

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([
        NSPCurrentPriceSensor(entry),
        NSPCurrentPeriodSensor(entry),
        NSPNextPriceSensor(entry),
        NSPNextPeriodSensor(entry),
        NSPTaxActiveSensor(entry)
    ])

def calculate_period(target_time):
    month, hour = target_time.month, target_time.hour
    is_weekend = target_time.weekday() >= 5
    is_winter = month in [12, 1, 2]
    
    if is_weekend: return "off_peak"
    if is_winter:
        if (7 <= hour < 12) or (16 <= hour < 23): return "peak"
        elif (12 <= hour < 16): return "mid_peak"
        else: return "off_peak"
    else:
        # March-Nov Non-Winter Schedule
        return "mid_peak" if (7 <= hour < 23) else "off_peak"

def get_price(period, entry):
    rates = {
        "peak": entry.options.get(CONF_PEAK_PRICE, 0.23821),
        "mid_peak": entry.options.get(CONF_MID_PRICE, 0.19243),
        "off_peak": entry.options.get(CONF_OFFPEAK_PRICE, 0.11966)
    }
    price = rates.get(period, 0.11966)
    if entry.options.get(CONF_INCLUDE_TAX, True):
        price *= 1.15
    return round(price, 5)

class NSPCurrentPriceSensor(SensorEntity):
    def __init__(self, entry):
        self._entry, self._attr_name = entry, "NSP Current Price"
        self._attr_unique_id, self._attr_unit_of_measurement = f"{entry.entry_id}_curr_price", "$/kWh"
    @property
    def state(self): return get_price(calculate_period(datetime.now()), self._entry)

class NSPCurrentPeriodSensor(SensorEntity):
    def __init__(self, entry):
        self._entry, self._attr_name = entry, "NSP Current Period"
        self._attr_unique_id = f"{entry.entry_id}_curr_period"
    @property
    def state(self): return calculate_period(datetime.now())

class NSPNextPriceSensor(SensorEntity):
    def __init__(self, entry):
        self._entry, self._attr_name = entry, "NSP Next Price"
        self._attr_unique_id, self._attr_unit_of_measurement = f"{entry.entry_id}_next_price", "$/kWh"
    @property
    def state(self): return get_price(calculate_period(datetime.now() + timedelta(hours=1)), self._entry)

class NSPNextPeriodSensor(SensorEntity):
    def __init__(self, entry):
        self._entry, self._attr_name = entry, "NSP Next Period"
        self._attr_unique_id = f"{entry.entry_id}_next_period"
    @property
    def state(self): return calculate_period(datetime.now() + timedelta(hours=1))

class NSPTaxActiveSensor(SensorEntity):
    def __init__(self, entry):
        self._entry, self._attr_name = entry, "NSP Tax Active"
        self._attr_unique_id = f"{entry.entry_id}_tax_active"
    @property
    def state(self): return "Yes" if self._entry.options.get(CONF_INCLUDE_TAX, True) else "No"
