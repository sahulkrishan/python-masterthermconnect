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
    URL_BASE,
    URL_LOGIN,
    URL_GET,
    URL_POST,
)
from .exceptions import MasterThermUnsupportedRole

_LOGGER: logging.Logger = logging.getLogger(__package__)


class Device:
    """Mastertherm Device Object."""

    def __init__(self, auth: Auth, module_id, device_id):
        """Initialize the Connection Object."""
        self._auth = auth
        self._module_id = module_id
        self._device_id = device_id
        self._module_name = None
        self._device_name = None
        self._config_file = None
        self._message_id: int = 1
        self._timestamp: int = None
        self._dataLoaded = False
        self._data = {}

    async def getData(self):
        """Get data"""
        self._dataLoaded = False

        response = await self._api.async_get_data()

        if response.status != 200:
            errorMsg = await response.text()
            raise MasterThermConnectionError(str(response.status), errorMsg)

        self._timestamp = response["timestamp"]

        self._config_file = list(response["data"].keys())[0]
        listId = list(response["data"][self._config_file].keys())[0]

        self._data = response["data"][self._config_file][listId]

        self._dataLoaded = True
        return True

    async def async_get_data(self):
        """Get data of MasterTherm device from the API"""
        self._message_id += 1
        url = urljoin(URL_BASE, URL_GET)
        data = f"messageId={self._messageId}&moduleId={self._module_id}&deviceId={self._device_id}&fullRange=true&errorResponse=true&lastUpdateTime=0"
        return await self.api_wrapper("get", url, data)

    async def async_set_data(self, variable_id, variable_value):
        """Post data to MasterTherm device with the API"""
        self._message_id += 1
        url = urljoin(URL_BASE, URL_POST)
        data = f"configFile={self._config_file}&messageId={self._messageId}&moduleId={self._module_id}&deviceId={self._device_id}&variableId={variable_id}&variableValue={variable_value}"
        response = await self.api_wrapper("post", url, data)
        # TO-DO check response
        return True

    def getAttributeValue(self, attribute):
        if not self._dataLoaded:
            self.getData()
        _LOGGER.info(self._data)
        value = self._data[attribute]
        return value
