# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from . import Quaternion

from typing import Any


class QuaternionStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/QuaternionStamped.msg

    Args:
        header: No information
        quaternion: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        quaternion: Quaternion | Any = None,
    ):
        self.header: Header | Any
        self.quaternion: Quaternion | Any

