# flake8: noqa
from ..common_interfaces.base_types import *
from ..geometry_msgs import Transform
from ..geometry_msgs import Twist
from ..geometry_msgs import Twist
from ..builtin_interfaces import Duration

from typing import Any


class MultiDOFJointTrajectoryPoint:
    """
    https://github.com/ros2/common_interfaces/blob/humble/trajectory_msgs/msg/MultiDOFJointTrajectoryPoint.msg

    Args:
        transforms: No information
        velocities: No information
        accelerations: No information
        time_from_start: No information
    """
    def __init__(
        self,
        transforms: list[Transform] | list[Any] = None,
        velocities: list[Twist] | list[Any] = None,
        accelerations: list[Twist] | list[Any] = None,
        time_from_start: Duration | int = None,
    ):
        self.transforms: list[Transform] | list[Any]
        self.velocities: list[Twist] | list[Any]
        self.accelerations: list[Twist] | list[Any]
        self.time_from_start: Duration | int

