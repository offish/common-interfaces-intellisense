# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from . import Pose

from typing import Any


class PoseStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/PoseStamped.msg

    Args:
        header: No information
        pose: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        pose: Pose | Any = None,
    ):
        self.header: Header | Any
        self.pose: Pose | Any

