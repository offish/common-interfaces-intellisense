# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from . import GoalStatus

from typing import Any


class GoalStatusArray:
    """
    https://github.com/ros2/common_interfaces/blob/humble/actionlib_msgs/msg/GoalStatusArray.msg

    Args:
        header: No information
        status_list: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        status_list: list[GoalStatus] | list[Any] = None,
    ):
        self.header: Header | Any
        self.status_list: list[GoalStatus] | list[Any]

