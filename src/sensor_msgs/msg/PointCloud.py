# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from geometry_msgs.msg import Point32
from . import ChannelFloat32

from typing import Any


class PointCloud:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/PointCloud.msg

    Args:
        header: No information
        points: No information
        channels: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        points: list[Point32] | list[int] = None,
        channels: list[ChannelFloat32] | list[Any] = None,
    ):
        self.header: Header | Any
        self.points: list[Point32] | list[int]
        self.channels: list[ChannelFloat32] | list[Any]

