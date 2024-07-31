# flake8: noqa
from ..common_interfaces.base_types import *
from . import Vector3
from . import Vector3

from typing import Any


class Wrench:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Wrench.msg

    Args:
        force: No information
        torque: No information
    """
    def __init__(
        self,
        force: Vector3 | Any = None,
        torque: Vector3 | Any = None,
    ):
        self.force: Vector3 | Any
        self.torque: Vector3 | Any

