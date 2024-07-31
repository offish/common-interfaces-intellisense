# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from ..geometry_msgs import Transform
from ..geometry_msgs import Twist
from ..geometry_msgs import Wrench

from typing import Any


class MultiDOFJointState:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/MultiDOFJointState.msg

    Args:
        header: No information
        joint_names: No information
        transforms: No information
        twist: No information
        wrench: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        joint_names: list[string] | list[Any] = None,
        transforms: list[Transform] | list[Any] = None,
        twist: list[Twist] | list[Any] = None,
        wrench: list[Wrench] | list[Any] = None,
    ):
        self.header: Header | Any
        self.joint_names: list[string] | list[Any]
        self.transforms: list[Transform] | list[Any]
        self.twist: list[Twist] | list[Any]
        self.wrench: list[Wrench] | list[Any]

