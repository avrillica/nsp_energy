from homeassistant.components.sensor import SensorEntity
from datetime import datetime
from .const import DOMAIN, CONF_PEAK_PRICE, CONF_MID_PRICE, CONF_OFFPEAK_PRICE, CONF_INCLUDE_TAX

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([NSPRateSensor(entry), NSPPeriodSensor(entry)])

def calculate_nsp_period():
    now = datetime.now()
    month = now.month
    hour = now.hour
    is_weekend = now.weekday() >= 5 # Sat=5, Sun=6
    
    # 2026 Seasonality: Winter is Dec, Jan, Feb
    is_winter = month in [12, 1, 2]
    
    if is_weekend:
        return "off_peak"

    if is_winter:
        # Winter Weekdays: Peak (7-12, 16-23), Mid (12-16), Off (23-7)
        if (7 <= hour < 12) or (16 <= hour < 23):
            return "peak"
        elif (12 <= hour < 16):
            return "mid_peak"
        else:
            return "off_peak"
    else:
        # Non-Winter (March - Nov): Mid (7-23), Off (23-7)
        # Note: Peak rate does not apply in non-winter months
        if (7 <= hour < 23):
            return "mid_peak"
        else:
            return "off_peak"

class NSPRateSensor(SensorEntity):
    def __init__(self, entry):
        self._entry = entry
        self._attr_name = "NSP Current Rate"
        self._attr_unique_id = f"{entry.entry_id}_rate"
        self._attr_unit_of_measurement = "$/kWh"
        self._attr_icon = "mdi:currency-usd"

    @property
    def state(self):
        period = calculate_nsp_period()
        
        # Pull rates from options (saved in the UI)
        rates = {
            "peak": self._entry.options.get(CONF_PEAK_PRICE, 0.23821),
            "mid_peak": self._entry.options.get(CONF_MID_PRICE, 0.19243),
            "off_peak": self._entry.options.get(CONF_OFFPEAK_PRICE, 0.11966)
        }
        
        price = rates.get(period, 0.11966)
        
        # Apply 15% HST if toggled ON
        if self._entry.options.get(CONF_INCLUDE_TAX, True):
            price = price * 1.15
            
        return round(price, 5)

class NSPPeriodSensor(SensorEntity):
    def __init__(self, entry):
        self._entry = entry
        self._attr_name = "NSP Current Period"
        self._attr_unique_id = f"{entry.entry_id}_period"
        self._attr_icon = "mdi:clock-outline"

    @property
    def state(self):
        return calculate_nsp_period()
