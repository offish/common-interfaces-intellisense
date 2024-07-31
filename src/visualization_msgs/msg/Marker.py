# flake8: noqa
from common_interfaces.base_types import *
from std_msgs.msg import Header
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Vector3
from std_msgs.msg import ColorRGBA
from builtin_interfaces.msg import Duration
from geometry_msgs.msg import Point
from std_msgs.msg import ColorRGBA
from sensor_msgs.msg import CompressedImage
from . import UVCoordinate
from . import MeshFile

from typing import Any


class Marker:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/Marker.msg

    Args:
        ARROW: No information
        CUBE: No information
        SPHERE: No information
        CYLINDER: No information
        LINE_STRIP: No information
        LINE_LIST: No information
        CUBE_LIST: No information
        SPHERE_LIST: No information
        POINTS: No information
        TEXT_VIEW_FACING: No information
        MESH_RESOURCE: No information
        TRIANGLE_LIST: No information
        ADD: No information
        MODIFY: No information
        DELETE: No information
        DELETEALL: No information
        header: No information
        ns: No information
        id: No information
        type: No information
        action: No information
        pose: No information
        scale: No information
        color: No information
        lifetime: No information
        frame_locked: No information
        points: No information
        colors: No information
        texture_resource: No information
        texture: No information
        uv_coordinates: No information
        text: No information
        mesh_resource: No information
        mesh_file: No information
        mesh_use_embedded_materials: No information
    """
    def __init__(
        self,
        ARROW: int32 | int = None,
        CUBE: int32 | int = None,
        SPHERE: int32 | int = None,
        CYLINDER: int32 | int = None,
        LINE_STRIP: int32 | int = None,
        LINE_LIST: int32 | int = None,
        CUBE_LIST: int32 | int = None,
        SPHERE_LIST: int32 | int = None,
        POINTS: int32 | int = None,
        TEXT_VIEW_FACING: int32 | int = None,
        MESH_RESOURCE: int32 | int = None,
        TRIANGLE_LIST: int32 | int = None,
        ADD: int32 | int = None,
        MODIFY: int32 | int = None,
        DELETE: int32 | int = None,
        DELETEALL: int32 | int = None,
        header: Header | Any = None,
        ns: string | str = None,
        id: int32 | int = None,
        type: int32 | int = None,
        action: int32 | int = None,
        pose: Pose | Any = None,
        scale: Vector3 | Any = None,
        color: ColorRGBA | Any = None,
        lifetime: Duration | int = None,
        frame_locked: bool = None,
        points: list[Point] | list[int] = None,
        colors: list[ColorRGBA] | list[Any] = None,
        texture_resource: string | str = None,
        texture: CompressedImage | Any = None,
        uv_coordinates: list[UVCoordinate] | list[Any] = None,
        text: string | str = None,
        mesh_resource: string | str = None,
        mesh_file: MeshFile | Any = None,
        mesh_use_embedded_materials: bool = None,
    ):
        self.ARROW: int32 | int
        self.CUBE: int32 | int
        self.SPHERE: int32 | int
        self.CYLINDER: int32 | int
        self.LINE_STRIP: int32 | int
        self.LINE_LIST: int32 | int
        self.CUBE_LIST: int32 | int
        self.SPHERE_LIST: int32 | int
        self.POINTS: int32 | int
        self.TEXT_VIEW_FACING: int32 | int
        self.MESH_RESOURCE: int32 | int
        self.TRIANGLE_LIST: int32 | int
        self.ADD: int32 | int
        self.MODIFY: int32 | int
        self.DELETE: int32 | int
        self.DELETEALL: int32 | int
        self.header: Header | Any
        self.ns: string | str
        self.id: int32 | int
        self.type: int32 | int
        self.action: int32 | int
        self.pose: Pose | Any
        self.scale: Vector3 | Any
        self.color: ColorRGBA | Any
        self.lifetime: Duration | int
        self.frame_locked: bool
        self.points: list[Point] | list[int]
        self.colors: list[ColorRGBA] | list[Any]
        self.texture_resource: string | str
        self.texture: CompressedImage | Any
        self.uv_coordinates: list[UVCoordinate] | list[Any]
        self.text: string | str
        self.mesh_resource: string | str
        self.mesh_file: MeshFile | Any
        self.mesh_use_embedded_materials: bool

