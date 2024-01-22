import logging
from .const import TEMPERATURE_ENTITY_SUFFIX, HUMIDITY_ENTITY_SUFFIX
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the My Custom Integration component."""
    # Register the config flow
    config_flow.MyCustomIntegrationConfigFlow.async_register_implementation(
        hass,
        DOMAIN,
        "My Custom Integration",
        config_entries.CONN_CLASS_LOCAL_PUSH,
    )

    # For each existing entry, create the entities
    for entry in hass.config_entries.async_entries(DOMAIN):
        await async_create_entities(hass, entry)

    return True

hass.config_entries.async_setup(hass, DOMAIN)
async def async_create_entities(hass: HomeAssistant, config_entry: ConfigEntry):
    """Create entities for the device."""
    device_name = config_entry.title
    temperature_entity_name = device_name + TEMPERATURE_ENTITY_SUFFIX
    humidity_entity_name = device_name + HUMIDITY_ENTITY_SUFFIX

    # Register the temperature entity
    hass.states.async_set(
        f"sensor.{temperature_entity_name}",
        "unknown",
        {
            "friendly_name": f"{device_name} Temperature",
            "device_class": "temperature",
        },
    )

    # Register the humidity entity
    hass.states.async_set(
        f"sensor.{humidity_entity_name}",
        "unknown",
        {
            "friendly_name": f"{device_name} Humidity",
            "device_class": "humidity",
        },
    )
