# flake8: noqa
from ..common_interfaces.base_types import *
from . import MeshTriangle
from ..geometry_msgs import Point

from typing import Any


class Mesh:
    """
    https://github.com/ros2/common_interfaces/blob/humble/shape_msgs/msg/Mesh.msg

    Args:
        triangles: No information
        vertices: No information
    """
    def __init__(
        self,
        triangles: list[MeshTriangle] | list[Any] = None,
        vertices: list[Point] | list[int] = None,
    ):
        self.triangles: list[MeshTriangle] | list[Any]
        self.vertices: list[Point] | list[int]

