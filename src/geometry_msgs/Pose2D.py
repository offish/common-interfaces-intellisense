# flake8: noqa
from ..common_interfaces.base_types import *

from typing import Any


class Pose2D:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Pose2D.msg

    Args:
        x: No information
        y: No information
        theta: No information
    """
    def __init__(
        self,
        x: float64 | float = None,
        y: float64 | float = None,
        theta: float64 | float = None,
    ):
        self.x: float64 | float
        self.y: float64 | float
        self.theta: float64 | float

