# flake8: noqa
from common_interfaces.base_types import *
from builtin_interfaces.msg import Time

from typing import Any


class GoalID:
    """
    https://github.com/ros2/common_interfaces/blob/humble/actionlib_msgs/msg/GoalID.msg

    Args:
        stamp: No information
        id: No information
    """
    def __init__(
        self,
        stamp: Time | int = None,
        id: string | str = None,
    ):
        self.stamp: Time | int
        self.id: string | str

