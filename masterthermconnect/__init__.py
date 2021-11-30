"""Python API wrapper for Mastertherm Connect."""
from masterthermconnect.__version__ import __version__
from masterthermconnect.connection import Connection
from masterthermconnect.controller import Controller
from masterthermconnect.auth import Auth
from masterthermconnect.heatpump import HeatPump
from masterthermconnect.exceptions import (
    MasterThermAuthenticationError,
    MasterThermConnectionError,
    MasterThermResponseFormatError,
    MasterThermTokenInvalid,
    MasterThermUnsupportedRole,
)

__all__ = [
    "__version__",
    "Auth",
    "HeatPump",
    "MasterThermAuthenticationError",
    "MasterThermConnectionError",
    "MasterThermResponseFormatError",
    "MasterThermTokenInvalid",
    "MasterThermUnsupportedRole",
]
