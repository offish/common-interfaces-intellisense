# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class Bool:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/Bool.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: bool = None,
    ):
        self.data: bool

