"""MasterTherm Connection to the Web API."""
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

from masterthermconnect.const import (
    APP_CLIENTINFO,
    APP_OS,
    APP_VERSION,
    COOKIE_TOKEN,
    DATE_FORMAT,
    HEADER_TOKEN_EXPIRES,
    URL_BASE,
    URL_LOGIN,
    URL_GET,
    URL_POST,
)

from .exceptions import (
    MasterThermAuthenticationError,
    MasterThermConnectionError,
    MasterThermResponseFormatError,
    MasterThermTokenInvalid,
)

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"content-type": "application/x-www-form-urlencoded"}


class Auth:
    """Connection Handler for the MasterTherm API."""

    def __init__(
        self, username: str, password: str, session: aiohttp.ClientSession
    ) -> None:
        """Initiate the Connection API."""
        self._username = username
        self._password = sha1(password.encode("utf-8")).hexdigest()
        self._session = session
        self._clientinfo = APP_CLIENTINFO
        self._token = None
        self._expires = None
        self._isConnected = False
        self._lastUpdateTime = None
        self._messageId = 1

    # async def async_set_title(self, value: str) -> None:
    #     """Get data from the API."""
    #     url = "https://jsonplaceholder.typicode.com/posts/1"
    #     await self.api_wrapper("post", url, data={"title": value}, headers=HEADERS)

    async def connect(self):
        """Authenticate to the API"""
        self._isConnected = False

        url = urljoin(URL_BASE, URL_LOGIN)
        data = f"login=login&uname={self._username}&upwd={self._password}&{self._clientinfo}"
        headers = {"content-type": "application/x-www-form-urlencoded"}
        response = await self.api_wrapper("post", url, data, headers)

        # Response should always be 200 even for login failures.
        if response.status != 200:
            errorMsg = await response.text()
            raise MasterThermConnectionError(str(response.status), errorMsg)

        # Expect that the response is JSON, check the result.
        responseJSON = await response.json()
        if responseJSON["returncode"] != 0:
            raise MasterThermAuthenticationError(
                responseJSON["returncode"], responseJSON["message"]
            )

        # # Check if role is supported
        # if not responseJSON["role"] in SUPPORTED_ROLES:
        #     raise MasterThermUnsupportedRole(
        #         "2", "Unsupported Role " + responseJSON["role"]
        #     )

        # Get or Refresh the Token and Expiry
        self._token = response.cookies[COOKIE_TOKEN].value
        self._expires = datetime.strptime(
            response.headers[HEADER_TOKEN_EXPIRES], DATE_FORMAT
        )

        self._isConnected = True
        return responseJSON

    async def isConnected(self):
        """Check if session is still valid"""
        if _expires <= datetime.now():
            self._isConnected = False
        return self._isConnected

    async def async_get_data(self, module_id, device_id) -> dict:
        """Get data of MasterTherm device from the API"""
        url = urljoin(URL_BASE, URL_GET)
        data = f"messageId={self._messageId}&moduleId={module_id}&deviceId={device_id}&fullRange=true&errorResponse=true&lastUpdateTime=0"
        return await self.api_wrapper("post", url, data, HEADERS)

    async def async_set_data(
        self, module_id, device_id, config_file, variable_id, variable_value
    ) -> dict:
        """Get data of MasterTherm device from the API"""
        url = urljoin(URL_BASE, URL_GET)
        data = f"configFile={config_file}&messageId={self._messageId}&moduleId={module_id}&deviceId={device_id}&variableId={variable_id}&variableValue={variable_value}"
        response = await self.api_wrapper("post", url, data, HEADERS)
        # TO-DO check response
        return True

    async def api_wrapper(
        self, method: str, url: str, data: dict = {}, headers: dict = {}
    ) -> dict:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(TIMEOUT):
                self._messageId += 1
                if not self.isConnected():
                    await self.connect()

                if method == "get":
                    response = await self._session.get(url, headers=headers)
                    return await response

                elif method == "post":
                    response = await self._session.post(url, headers=headers, json=data)
                    return await response

        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Unknown Error")
