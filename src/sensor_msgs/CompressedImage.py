# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header

from typing import Any


class CompressedImage:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/CompressedImage.msg

    Args:
        header: No information
        format: No information
        data: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        format: string | str = None,
        data: list[uint8] | list[int] = None,
    ):
        self.header: Header | Any
        self.format: string | str
        self.data: list[uint8] | list[int]

