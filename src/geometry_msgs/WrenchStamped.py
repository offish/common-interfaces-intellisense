# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import Wrench

from typing import Any


class WrenchStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/WrenchStamped.msg

    Args:
        header: No information
        wrench: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        wrench: Wrench | Any = None,
    ):
        self.header: Header | Any
        self.wrench: Wrench | Any

