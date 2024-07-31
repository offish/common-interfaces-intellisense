# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from . import Inertia

from typing import Any


class InertiaStamped:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/InertiaStamped.msg

    Args:
        header: No information
        inertia: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        inertia: Inertia | Any = None,
    ):
        self.header: Header | Any
        self.inertia: Inertia | Any

