# flake8: noqa
from common_interfaces.base_types import *
from builtin_interfaces.msg import Time

from typing import Any


class Header:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/Header.msg

    Args:
        stamp: No information
        frame_id: No information
    """
    def __init__(
        self,
        stamp: Time | int = None,
        frame_id: string | str = None,
    ):
        self.stamp: Time | int
        self.frame_id: string | str

