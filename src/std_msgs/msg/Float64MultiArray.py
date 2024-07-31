# flake8: noqa
from common_interfaces.base_types import *
from . import MultiArrayLayout

from typing import Any


class Float64MultiArray:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/Float64MultiArray.msg

    Args:
        layout: No information
        data: No information
    """
    def __init__(
        self,
        layout: MultiArrayLayout | Any = None,
        data: list[float64] | list[float] = None,
    ):
        self.layout: MultiArrayLayout | Any
        self.data: list[float64] | list[float]

