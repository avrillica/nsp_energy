import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import *

class NSPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="NSP Rates", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_PEAK_PRICE, default=DEFAULT_PEAK): vol.Coerce(float),
                vol.Required(CONF_MID_PEAK_PRICE, default=DEFAULT_MID): vol.Coerce(float),
                vol.Required(CONF_OFF_PEAK_PRICE, default=DEFAULT_OFF): vol.Coerce(float),
                vol.Required(CONF_INCLUDE_TAX, default=True): bool,
            })
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return NSPOptionsFlowHandler(config_entry)

class NSPOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            # This line fixes the 500 error by ensuring data is saved correctly
            return self.async_create_entry(title="", data=user_input)
        
        # Pull from options first, then data, then defaults. This is the safety net.
        current = {**self.config_entry.data, **self.config_entry.options}
        
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(CONF_PEAK_PRICE, default=current.get(CONF_PEAK_PRICE, DEFAULT_PEAK)): vol.Coerce(float),
                vol.Required(CONF_MID_PEAK_PRICE, default=current.get(CONF_MID_PEAK_PRICE, DEFAULT_MID)): vol.Coerce(float),
                vol.Required(CONF_OFF_PEAK_PRICE, default=current.get(CONF_OFF_PEAK_PRICE, DEFAULT_OFF)): vol.Coerce(float),
                vol.Required(CONF_INCLUDE_TAX, default=current.get(CONF_INCLUDE_TAX, True)): bool,
            })
        )