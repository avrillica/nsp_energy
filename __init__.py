from .const import DOMAIN
async def async_setup_entry(hass, entry):
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    entry.async_on_unload(entry.add_update_listener(update_listener))
    return True
async def update_listener(hass, entry):
    await hass.config_entries.async_reload(entry.entry_id)
async def async_unload_entry(hass, entry):
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])