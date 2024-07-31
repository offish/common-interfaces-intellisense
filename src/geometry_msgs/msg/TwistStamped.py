# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from . import Twist

from typing import Any


class TwistStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/TwistStamped.msg

    Args:
        header: No information
        twist: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        twist: Twist | Any = None,
    ):
        self.header: Header | Any
        self.twist: Twist | Any

