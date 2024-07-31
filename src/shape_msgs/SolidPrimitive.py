# flake8: noqa
from ..common_interfaces.base_types import *
from ..geometry_msgs import Polygon

from typing import Any


class SolidPrimitive:
    """
    https://github.com/ros2/common_interfaces/blob/humble/shape_msgs/msg/SolidPrimitive.msg

    Args:
        BOX: No information
        SPHERE: No information
        CYLINDER: No information
        CONE: No information
        PRISM: No information
        type: No information
        dimensions: No information
        BOX_X: No information
        BOX_Y: No information
        BOX_Z: No information
        SPHERE_RADIUS: No information
        CYLINDER_HEIGHT: No information
        CYLINDER_RADIUS: No information
        CONE_HEIGHT: No information
        CONE_RADIUS: No information
        PRISM_HEIGHT: No information
        polygon: No information
    """
    def __init__(
        self,
        BOX: uint8 | int = None,
        SPHERE: uint8 | int = None,
        CYLINDER: uint8 | int = None,
        CONE: uint8 | int = None,
        PRISM: uint8 | int = None,
        type: uint8 | int = None,
        dimensions: list[float64] | list[float] = None,
        BOX_X: uint8 | int = None,
        BOX_Y: uint8 | int = None,
        BOX_Z: uint8 | int = None,
        SPHERE_RADIUS: uint8 | int = None,
        CYLINDER_HEIGHT: uint8 | int = None,
        CYLINDER_RADIUS: uint8 | int = None,
        CONE_HEIGHT: uint8 | int = None,
        CONE_RADIUS: uint8 | int = None,
        PRISM_HEIGHT: uint8 | int = None,
        polygon: Polygon | Any = None,
    ):
        self.BOX: uint8 | int
        self.SPHERE: uint8 | int
        self.CYLINDER: uint8 | int
        self.CONE: uint8 | int
        self.PRISM: uint8 | int
        self.type: uint8 | int
        self.dimensions: list[float64] | list[float]
        self.BOX_X: uint8 | int
        self.BOX_Y: uint8 | int
        self.BOX_Z: uint8 | int
        self.SPHERE_RADIUS: uint8 | int
        self.CYLINDER_HEIGHT: uint8 | int
        self.CYLINDER_RADIUS: uint8 | int
        self.CONE_HEIGHT: uint8 | int
        self.CONE_RADIUS: uint8 | int
        self.PRISM_HEIGHT: uint8 | int
        self.polygon: Polygon | Any

