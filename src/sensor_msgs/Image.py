# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header

from typing import Any


class Image:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/Image.msg

    Args:
        header: No information
        height: No information
        width: No information
        encoding: No information
        is_bigendian: No information
        step: No information
        data: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        height: uint32 | int = None,
        width: uint32 | int = None,
        encoding: string | str = None,
        is_bigendian: uint8 | int = None,
        step: uint32 | int = None,
        data: list[uint8] | list[int] = None,
    ):
        self.header: Header | Any
        self.height: uint32 | int
        self.width: uint32 | int
        self.encoding: string | str
        self.is_bigendian: uint8 | int
        self.step: uint32 | int
        self.data: list[uint8] | list[int]

