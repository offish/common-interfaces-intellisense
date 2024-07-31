# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class Int32:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/Int32.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: int32 | int = None,
    ):
        self.data: int32 | int

