# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class Point32:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Point32.msg

    Args:
        x: No information
        y: No information
        z: No information
    """
    def __init__(
        self,
        x: float32 | float = None,
        y: float32 | float = None,
        z: float32 | float = None,
    ):
        self.x: float32 | float
        self.y: float32 | float
        self.z: float32 | float

