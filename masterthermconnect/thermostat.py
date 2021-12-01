"""MasterTherm Controller, for handling MasterTherm Data."""
import logging
import asyncio
import socket
from typing import Optional
import aiohttp
import async_timeout

from datetime import datetime
from hashlib import sha1
import logging
from urllib.parse import urljoin

from .device import Device

from .const import (
    CHAR_MAP,
    DEVICE_DATA_MAP,
    DEVICE_DATA_PADMAP,
    DEVICE_INFO_MAP,
    DEVICE_SWITCH_MAP,
    PAD_MAP,
    SUPPORTED_ROLES,
)
from .exceptions import MasterThermUnsupportedRole

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

    def setTemperature(self, temp):
        """Set a new temperature"""
        variable_id = "A_191"
        variable_value = float(temp)
        response = self._api.async_set_data(
            self._module_id,
            self._device_id,
            self._config_file,
            variable_id,
            variable_value,
        )
        return True

    def getHVACMode(self):
        """Return current mode of MasterTherm device"""
        variable_id = "I_52"
        mode = self.getAttributeValue(variable_id)
        if mode == 0:
            return "heating"
        elif mode == 1:
            return "cooling"
        elif mode == 2:
            return "auto"
        else:
            return "unknown"
