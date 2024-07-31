# flake8: noqa
from common_interfaces.base_types import *
from builtin_interfaces.msg import Duration

from typing import Any


class JointTrajectoryPoint:
    """
    https://github.com/ros2/common_interfaces/blob/humble/trajectory_msgs/msg/JointTrajectoryPoint.msg

    Args:
        positions: No information
        velocities: No information
        accelerations: No information
        effort: No information
        time_from_start: No information
    """
    def __init__(
        self,
        positions: list[float64] | list[float] = None,
        velocities: list[float64] | list[float] = None,
        accelerations: list[float64] | list[float] = None,
        effort: list[float64] | list[float] = None,
        time_from_start: Duration | int = None,
    ):
        self.positions: list[float64] | list[float]
        self.velocities: list[float64] | list[float]
        self.accelerations: list[float64] | list[float]
        self.effort: list[float64] | list[float]
        self.time_from_start: Duration | int

