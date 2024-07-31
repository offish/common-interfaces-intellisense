# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header

from typing import Any


class Joy:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/Joy.msg

    Args:
        header: No information
        axes: No information
        buttons: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        axes: list[float32] | list[float] = None,
        buttons: list[int32] | list[int] = None,
    ):
        self.header: Header | Any
        self.axes: list[float32] | list[float]
        self.buttons: list[int32] | list[int]

