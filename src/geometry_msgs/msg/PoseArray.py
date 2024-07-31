# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from . import Pose

from typing import Any


class PoseArray:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/PoseArray.msg

    Args:
        header: No information
        poses: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        poses: list[Pose] | list[Any] = None,
    ):
        self.header: Header | Any
        self.poses: list[Pose] | list[Any]

