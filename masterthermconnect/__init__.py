"""Python API wrapper for Mastertherm Connect."""
from masterthermconnect.__version__ import __version__
from masterthermconnect.connection import Connection
from masterthermconnect.controller import Controller
from masterthermconnect.controller import Auth
from masterthermconnect.controller import HeatPump
from masterthermconnect.exceptions import (
    MasterThermAuthenticationError,
    MasterThermConnectionError,
    MasterThermResponseFormatError,
    MasterThermTokenInvalid,
    MasterThermUnsupportedRole,
)

__all__ = [
    "__version__",
    "Connection",
    "Controller",
    "Auth",
    "HeatPump",
    "MasterThermAuthenticationError",
    "MasterThermConnectionError",
    "MasterThermResponseFormatError",
    "MasterThermTokenInvalid",
    "MasterThermUnsupportedRole",
]
