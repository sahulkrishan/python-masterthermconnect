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

from .auth import Auth
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


class HeatPump:
    """Mastertherm HeatPump Object."""

    def __init__(self, username, password, session):
        """Initialize the Connection Object."""
        self._api = Auth(username, password, session)
        self._modules = []
        self._data = {}
        self._dataLoaded = False

    async def connect(self, updateData=True):
        """Connect to the API, check the supported roles and update if required."""
        response = await self._api.connect()

        # Initialize the Dictionary.
        self._modules = []
        for module in response["modules"]:
            self._module.append(module)

        if updateData:
            return await self.updateData()
        else:
            return True

    async def updateData(self):
        """Update data"""
        self._dataLoaded = False
        if self._modules:
            for module in self._modules:
                for device in module["config"]:
                    module_id = module["id"]
                    module_name = module["module_name"]
                    device_id = device["mb_addr"]
                    device_name = device["mb_name"]

                    response = await self._api.async_get_data(
                        self, module_id, device_id
                    )

                    self._data[module_id] = {
                        device_id: {
                            "info": {
                                "module_id": module_id,
                                "module_name": module_name,
                                "device_id": device_id,
                                "device_name": device_name,
                            },
                            "response": response,
                        },
                    }
        self._dataLoaded = True
        return True

    def getDevices(self):
        """Return a dict of all devices with data."""
        deviceReturn = {}
        for module in self._data:
            for device in module:
                module_id = device["info"]["module_id"]
                deviceReturn[module_id] = device["info"]
        return deviceReturn

    def getAttributeValue(self, module_id, device_id, attribute):
        value = self._data[module_id][device_id]["data"]["response"][0][0][attribute]
        return value

    # TO-DO get variableIDs from const
    def getCurrentTemperature(self, module_id, device_id):
        """Get the current temparature"""
        variable_id = "A_211"
        return float(getAttributeValue(module_id, device_id, variable_id))

    def getTemperature(self, module_id, device_id):
        """Get the requested temperature"""
        variable_id = "A_191"
        return float(getAttributeValue(module_id, device_id, variable_id))

    def setTemperature(self, module_id, device_id, temp):
        """Set a new temperature"""
        config_file = "varfile_mt1_config1"
        variable_id = "A_191"
        variable_value = float(temp)
        response = self._api.async_set_data(
            module_id, device_id, config_file, variable_id, variable_value
        )
        return True

    def getHVACMode(self, module_id, device_id):
        """Return current mode of MasterTherm device"""
        variable_id = "I_52"
        mode = getAttributeValue(module_id, device_id, variable_id)
        if mode == 0:
            return "heating"
        elif mode == 1:
            return "cooling"
        elif mode == 2:
            return "auto"
        else:
            return "unknown"
