# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from ..geometry_msgs import PoseStamped

from typing import Any


class Path:
    """
    https://github.com/ros2/common_interfaces/blob/humble/nav_msgs/msg/Path.msg

    Args:
        header: No information
        poses: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        poses: list[PoseStamped] | list[Any] = None,
    ):
        self.header: Header | Any
        self.poses: list[PoseStamped] | list[Any]

