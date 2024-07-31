# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from . import Vector3

from typing import Any


class Vector3Stamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Vector3Stamped.msg

    Args:
        header: No information
        vector: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        vector: Vector3 | Any = None,
    ):
        self.header: Header | Any
        self.vector: Vector3 | Any

