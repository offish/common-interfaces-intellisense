# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from ..geometry_msgs import Quaternion
from ..geometry_msgs import Vector3
from ..geometry_msgs import Vector3

from typing import Any


class Imu:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/Imu.msg

    Args:
        header: No information
        orientation: No information
        orientation_covariance: 9 elements
        angular_velocity: No information
        angular_velocity_covariance: 9 elements
        linear_acceleration: No information
        linear_acceleration_covariance: 9 elements
    """
    def __init__(
        self,
        header: Header | Any = None,
        orientation: Quaternion | Any = None,
        orientation_covariance: list[float64] | list[float] = None,
        angular_velocity: Vector3 | Any = None,
        angular_velocity_covariance: list[float64] | list[float] = None,
        linear_acceleration: Vector3 | Any = None,
        linear_acceleration_covariance: list[float64] | list[float] = None,
    ):
        self.header: Header | Any
        self.orientation: Quaternion | Any
        self.orientation_covariance: list[float64] | list[float]
        self.angular_velocity: Vector3 | Any
        self.angular_velocity_covariance: list[float64] | list[float]
        self.linear_acceleration: Vector3 | Any
        self.linear_acceleration_covariance: list[float64] | list[float]

