# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from . import JointTrajectoryPoint

from typing import Any


class JointTrajectory:
    """
    https://github.com/ros2/common_interfaces/blob/humble/trajectory_msgs/msg/JointTrajectory.msg

    Args:
        header: No information
        joint_names: No information
        points: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        joint_names: list[string] | list[Any] = None,
        points: list[JointTrajectoryPoint] | list[int] = None,
    ):
        self.header: Header | Any
        self.joint_names: list[string] | list[Any]
        self.points: list[JointTrajectoryPoint] | list[int]

