# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header

from typing import Any


class FluidPressure:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/FluidPressure.msg

    Args:
        header: No information
        fluid_pressure: No information
        variance: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        fluid_pressure: float64 | float = None,
        variance: float64 | float = None,
    ):
        self.header: Header | Any
        self.fluid_pressure: float64 | float
        self.variance: float64 | float

