"""MasterTherm Controller, for handling MasterTherm Data."""
import logging
from .device import Device

_LOGGER: logging.Logger = logging.getLogger(__package__)


class Thermostat(Device):
    """Mastertherm HeatPump Object."""

    def __init__(self, auth, module_id, device_id):
        Device.__init__(self, auth, module_id, device_id)

    # TO-DO get variableIDs from const
    def getCurrentTemperature(self):
        """Get the current temparature"""
        variable_id = "A_211"
        return float(self.getAttributeValue(variable_id))

    def getTemperature(self):
        """Get the requested temperature"""
        variable_id = "A_191"
        return float(self.getAttributeValue(variable_id))

    async def setTemperature(self, temp):
        """Set a new temperature"""
        variable_id = "A_191"
        variable_value = float(temp)
        return await self.async_set_data(
            variable_id,
            variable_value,
        )

    def getHVACMode(self):
        """Return current mode of MasterTherm device"""
        variable_id = "I_52"
        mode = self.getAttributeValue(variable_id)
        if mode == "0":
            return "heating"
        if mode == "1":
            return "cooling"
        if mode == "2":
            return "auto"
