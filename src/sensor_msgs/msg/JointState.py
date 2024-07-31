# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header

from typing import Any


class JointState:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/JointState.msg

    Args:
        header: No information
        name: No information
        position: No information
        velocity: No information
        effort: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        name: list[string] | list[Any] = None,
        position: list[float64] | list[float] = None,
        velocity: list[float64] | list[float] = None,
        effort: list[float64] | list[float] = None,
    ):
        self.header: Header | Any
        self.name: list[string] | list[Any]
        self.position: list[float64] | list[float]
        self.velocity: list[float64] | list[float]
        self.effort: list[float64] | list[float]

