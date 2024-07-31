# flake8: noqa
from ..common_interfaces.base_types import *
from ..geometry_msgs import Vector3

from typing import Any


class Inertia:
    """
    https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Inertia.msg

    Args:
        m: No information
        com: No information
        ixx: No information
        ixy: No information
        ixz: No information
        iyy: No information
        iyz: No information
        izz: No information
    """
    def __init__(
        self,
        m: float64 | float = None,
        com: Vector3 | Any = None,
        ixx: float64 | float = None,
        ixy: float64 | float = None,
        ixz: float64 | float = None,
        iyy: float64 | float = None,
        iyz: float64 | float = None,
        izz: float64 | float = None,
    ):
        self.m: float64 | float
        self.com: Vector3 | Any
        self.ixx: float64 | float
        self.ixy: float64 | float
        self.ixz: float64 | float
        self.iyy: float64 | float
        self.iyz: float64 | float
        self.izz: float64 | float

