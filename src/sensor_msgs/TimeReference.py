# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from ..builtin_interfaces import Time

from typing import Any


class TimeReference:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/TimeReference.msg

    Args:
        header: No information
        time_ref: No information
        source: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        time_ref: Time | int = None,
        source: string | str = None,
    ):
        self.header: Header | Any
        self.time_ref: Time | int
        self.source: string | str

