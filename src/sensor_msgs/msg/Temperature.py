# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header

from typing import Any


class Temperature:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/Temperature.msg

    Args:
        header: No information
        temperature: No information
        variance: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        temperature: float64 | float = None,
        variance: float64 | float = None,
    ):
        self.header: Header | Any
        self.temperature: float64 | float
        self.variance: float64 | float

