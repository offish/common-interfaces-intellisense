# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class String:
    """
    https://github.com/ros2/common_interfaces/blob/humble/std_msgs/msg/String.msg

    Args:
        data: No information
    """
    def __init__(
        self,
        data: string | str = None,
    ):
        self.data: string | str

