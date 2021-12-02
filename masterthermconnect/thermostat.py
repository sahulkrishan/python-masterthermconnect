"""MasterTherm Controller, for handling MasterTherm Data."""
import logging
from .device import Device

_LOGGER: logging.Logger = logging.getLogger(__package__)


class Thermostat(Device):
    """Mastertherm HeatPump Object."""

    def __init__(self, auth, module_id, device_id):
        Device.__init__(self, auth, module_id, device_id)

    # TO-DO get variableIDs from const
    async def getCurrentTemperature(self):
        """Get the current temparature"""
        variable_id = "A_211"
        return float(await self.getAttributeValue(variable_id))

    async def getTemperature(self):
        """Get the requested temperature"""
        variable_id = "A_191"
        return float(await self.getAttributeValue(variable_id))

    async def setTemperature(self, temp):
        """Set a new temperature"""
        variable_id = "A_191"
        variable_value = float(temp)
        await self.async_set_data(
            variable_id,
            variable_value,
        )
        return True

    async def getHVACMode(self):
        """Return current mode of MasterTherm device"""
        variable_id = "I_52"
        mode = await self.getAttributeValue(variable_id)
        if mode == "0":
            return "heating"
        elif mode == "1":
            return "cooling"
        elif mode == "2":
            return "auto"
        else:
            return "unknown"
