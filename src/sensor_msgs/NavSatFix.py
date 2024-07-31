# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import NavSatStatus

from typing import Any


class NavSatFix:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/NavSatFix.msg

    Args:
        header: No information
        status: No information
        latitude: No information
        longitude: No information
        altitude: No information
        position_covariance: 9 elements
        COVARIANCE_TYPE_UNKNOWN: No information
        COVARIANCE_TYPE_APPROXIMATED: No information
        COVARIANCE_TYPE_DIAGONAL_KNOWN: No information
        COVARIANCE_TYPE_KNOWN: No information
        position_covariance_type: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        status: NavSatStatus | Any = None,
        latitude: float64 | float = None,
        longitude: float64 | float = None,
        altitude: float64 | float = None,
        position_covariance: list[float64] | list[float] = None,
        COVARIANCE_TYPE_UNKNOWN: uint8 | int = None,
        COVARIANCE_TYPE_APPROXIMATED: uint8 | int = None,
        COVARIANCE_TYPE_DIAGONAL_KNOWN: uint8 | int = None,
        COVARIANCE_TYPE_KNOWN: uint8 | int = None,
        position_covariance_type: uint8 | int = None,
    ):
        self.header: Header | Any
        self.status: NavSatStatus | Any
        self.latitude: float64 | float
        self.longitude: float64 | float
        self.altitude: float64 | float
        self.position_covariance: list[float64] | list[float]
        self.COVARIANCE_TYPE_UNKNOWN: uint8 | int
        self.COVARIANCE_TYPE_APPROXIMATED: uint8 | int
        self.COVARIANCE_TYPE_DIAGONAL_KNOWN: uint8 | int
        self.COVARIANCE_TYPE_KNOWN: uint8 | int
        self.position_covariance_type: uint8 | int

