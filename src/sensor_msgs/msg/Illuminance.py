# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header

from typing import Any


class Illuminance:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/Illuminance.msg

    Args:
        header: No information
        illuminance: No information
        variance: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        illuminance: float64 | float = None,
        variance: float64 | float = None,
    ):
        self.header: Header | Any
        self.illuminance: float64 | float
        self.variance: float64 | float

