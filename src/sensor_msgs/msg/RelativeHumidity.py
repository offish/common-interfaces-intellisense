# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header

from typing import Any


class RelativeHumidity:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/RelativeHumidity.msg

    Args:
        header: No information
        relative_humidity: No information
        variance: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        relative_humidity: float64 | float = None,
        variance: float64 | float = None,
    ):
        self.header: Header | Any
        self.relative_humidity: float64 | float
        self.variance: float64 | float

