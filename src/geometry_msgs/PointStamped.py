# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import Point

from typing import Any


class PointStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/PointStamped.msg

    Args:
        header: No information
        point: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        point: Point | int = None,
    ):
        self.header: Header | Any
        self.point: Point | int

