# flake8: noqa
from common_interfaces.base_types import *
from . import Point
from . import Quaternion

from typing import Any


class Pose:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Pose.msg

    Args:
        position: No information
        orientation: No information
    """
    def __init__(
        self,
        position: Point | int = None,
        orientation: Quaternion | Any = None,
    ):
        self.position: Point | int
        self.orientation: Quaternion | Any

