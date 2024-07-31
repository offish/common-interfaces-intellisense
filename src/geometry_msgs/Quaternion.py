# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class Quaternion:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Quaternion.msg

    Args:
        x: No information
        y: No information
        z: No information
        w: No information
    """
    def __init__(
        self,
        x: float64 | float = None,
        y: float64 | float = None,
        z: float64 | float = None,
        w: float64 | float = None,
    ):
        self.x: float64 | float
        self.y: float64 | float
        self.z: float64 | float
        self.w: float64 | float

