# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import Polygon

from typing import Any


class PolygonStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/PolygonStamped.msg

    Args:
        header: No information
        polygon: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        polygon: Polygon | Any = None,
    ):
        self.header: Header | Any
        self.polygon: Polygon | Any

