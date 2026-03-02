import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import (
    DOMAIN, 
    CONF_PEAK_PRICE, 
    CONF_MID_PRICE, 
    CONF_OFFPEAK_PRICE, 
    CONF_INCLUDE_TAX, 
    DEFAULT_PEAK, 
    DEFAULT_MID, 
    DEFAULT_OFF
)

class NSPEnergyFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for NSP Energy Monitor."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="NSP Energy Monitor", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_PEAK_PRICE, default=DEFAULT_PEAK): vol.Coerce(float),
                vol.Required(CONF_MID_PRICE, default=DEFAULT_MID): vol.Coerce(float),
                vol.Required(CONF_OFFPEAK_PRICE, default=DEFAULT_OFF): vol.Coerce(float),
                vol.Required(CONF_INCLUDE_TAX, default=True): bool,
            })
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return NSPEnergyOptionsFlowHandler(config_entry)

class NSPEnergyOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for NSP Energy Monitor."""
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Use current options or defaults
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(
                    CONF_PEAK_PRICE, 
                    default=self.config_entry.options.get(CONF_PEAK_PRICE, DEFAULT_PEAK)
                ): vol.Coerce(float),
                vol.Required(
                    CONF_MID_PRICE, 
                    default=self.config_entry.options.get(CONF_MID_PRICE, DEFAULT_MID)
                ): vol.Coerce(float),
                vol.Required(
                    CONF_OFFPEAK_PRICE, 
                    default=self.config_entry.options.get(CONF_OFFPEAK_PRICE, DEFAULT_OFF)
                ): vol.Coerce(float),
                vol.Required(
                    CONF_INCLUDE_TAX, 
                    default=self.config_entry.options.get(CONF_INCLUDE_TAX, True)
                ): bool,
            }),
        )
