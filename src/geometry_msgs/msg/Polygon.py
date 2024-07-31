# flake8: noqa
from common_interfaces.base_types import *
from . import Point32

from typing import Any


class Polygon:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Polygon.msg

    Args:
        points: No information
    """
    def __init__(
        self,
        points: list[Point32] | list[int] = None,
    ):
        self.points: list[Point32] | list[int]

