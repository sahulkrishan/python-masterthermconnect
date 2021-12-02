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
        self._message_id: int = 0
        self._timestamp: int = None
        self._data_loaded = False
        self._data = {}

    async def getData(self):
        """Get data"""
        self._data_loaded = False

        response = await self.async_get_data()
        responseJSON = await response.json()

        if response.status != 200:
            errorMsg = await response.text()
            raise MasterThermConnectionError(str(response.status), errorMsg)

        self._timestamp = responseJSON["timestamp"]

        self._config_file = list(responseJSON["data"].keys())[0]
        listId = list(responseJSON["data"][self._config_file].keys())[0]

        self._data = responseJSON["data"][self._config_file][listId]

        self._data_loaded = True
        return True

    async def async_get_data(self):
        """Get data of MasterTherm device from the API"""
        self._message_id += 1
        url = urljoin(URL_BASE, URL_GET)
        data = f"messageId={self._message_id}&moduleId={self._module_id}&deviceId={self._device_id}&fullRange=true&errorResponse=true&lastUpdateTime=0"
        response = await self.api_wrapper("get", url, data)
        _LOGGER.debug("async_get_data")
        _LOGGER.debug(data)
        _LOGGER.debug(response)
        return response

    async def async_set_data(self, variable_id, variable_value):
        """Post data to MasterTherm device with the API"""
        self._message_id += 1
        url = urljoin(URL_BASE, URL_POST)
        data = f"configFile={self._config_file}&messageId={self._message_id}&moduleId={self._module_id}&deviceId={self._device_id}&variableId={variable_id}&variableValue={variable_value}"
        response = await self.api_wrapper("post", url, data)
        _LOGGER.debug("async_set_data")
        _LOGGER.debug(data)
        _LOGGER.debug(response)
        # TO-DO check response
        return True

    async def getAttributeValue(self, attribute):
        if not self._dataLoaded:
            await self.getData()
        _LOGGER.info(self._data)
        value = self._data[attribute]
        return value
