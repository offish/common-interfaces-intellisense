# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class NavSatStatus:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/NavSatStatus.msg

    Args:
        STATUS_NO_FIX: No information
        STATUS_FIX: No information
        STATUS_SBAS_FIX: No information
        STATUS_GBAS_FIX: No information
        status: No information
        SERVICE_GPS: No information
        SERVICE_GLONASS: No information
        SERVICE_COMPASS: No information
        SERVICE_GALILEO: No information
        service: No information
    """
    def __init__(
        self,
        STATUS_NO_FIX: int8 | int = None,
        STATUS_FIX: int8 | int = None,
        STATUS_SBAS_FIX: int8 | int = None,
        STATUS_GBAS_FIX: int8 | int = None,
        status: int8 | int = None,
        SERVICE_GPS: uint16 | int = None,
        SERVICE_GLONASS: uint16 | int = None,
        SERVICE_COMPASS: uint16 | int = None,
        SERVICE_GALILEO: uint16 | int = None,
        service: uint16 | int = None,
    ):
        self.STATUS_NO_FIX: int8 | int
        self.STATUS_FIX: int8 | int
        self.STATUS_SBAS_FIX: int8 | int
        self.STATUS_GBAS_FIX: int8 | int
        self.status: int8 | int
        self.SERVICE_GPS: uint16 | int
        self.SERVICE_GLONASS: uint16 | int
        self.SERVICE_COMPASS: uint16 | int
        self.SERVICE_GALILEO: uint16 | int
        self.service: uint16 | int

