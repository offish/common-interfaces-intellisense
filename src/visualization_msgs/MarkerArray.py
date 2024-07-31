# flake8: noqa
from ..common_interfaces.base_types import *
from . import Marker

from typing import Any


class MarkerArray:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/MarkerArray.msg

    Args:
        markers: No information
    """
    def __init__(
        self,
        markers: list[Marker] | list[Any] = None,
    ):
        self.markers: list[Marker] | list[Any]

