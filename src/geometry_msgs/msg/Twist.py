# flake8: noqa
from common_interfaces.base_types import *
from . import Vector3
from . import Vector3

from typing import Any


class Twist:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Twist.msg

    Args:
        linear: No information
        angular: No information
    """
    def __init__(
        self,
        linear: Vector3 | Any = None,
        angular: Vector3 | Any = None,
    ):
        self.linear: Vector3 | Any
        self.angular: Vector3 | Any

