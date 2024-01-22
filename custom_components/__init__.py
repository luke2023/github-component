import json
import logging

import homeassistant.components.mqtt as mqtt
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

DOMAIN = "mqtt_device"


def setup(hass, config):
    """Set up the MQTT Device integration."""
    mqtt.subscribe(hass, "humidity_topic", on_humidity_message)
    mqtt.subscribe(hass, "temperature_topic", on_temperature_message)

    return True


class MQTTDevice(Entity):
    """Representation of an MQTT device."""

    def __init__(self, name, state_topic):
        """Initialize the MQTT device."""
        self._name = name
        self._state = None
        self._state_topic = state_topic

    async def async_added_to_hass(self):
        """Subscribe to MQTT topic when added to Home Assistant."""
        await self._subscribe_topic()

    async def async_will_remove_from_hass(self):
        """Unsubscribe from MQTT topic when removed from Home Assistant."""
        await mqtt.async_unsubscribe(self.hass, self._state_topic)

    async def _subscribe_topic(self):
        """Subscribe to the MQTT topic."""
        await mqtt.async_subscribe(self.hass, self._state_topic, self._handle_message)

    async def _handle_message(self, topic, payload, qos):
        """Handle incoming MQTT message."""
        try:
            self._state = float(payload)
            self.async_write_ha_state()
        except ValueError:
            _LOGGER.warning("Received invalid payload for MQTT device %s", self._name)

    @property
    def name(self):
        """Return the name of the MQTT device."""
        return self._name

    @property
    def state(self):
        """Return the current state of the MQTT device."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement of the MQTT device."""
        return "%"

    @property
    def should_poll(self):
        """Disable polling for the MQTT device."""
        return False
