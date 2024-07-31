# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class RegionOfInterest:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/RegionOfInterest.msg

    Args:
        x_offset: No information
        y_offset: No information
        height: No information
        width: No information
        do_rectify: No information
    """
    def __init__(
        self,
        x_offset: uint32 | int = None,
        y_offset: uint32 | int = None,
        height: uint32 | int = None,
        width: uint32 | int = None,
        do_rectify: bool = None,
    ):
        self.x_offset: uint32 | int
        self.y_offset: uint32 | int
        self.height: uint32 | int
        self.width: uint32 | int
        self.do_rectify: bool

