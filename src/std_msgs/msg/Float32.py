# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class Float32:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/Float32.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: float32 | float = None,
    ):
        self.data: float32 | float

