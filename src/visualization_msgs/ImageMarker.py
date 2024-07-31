# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from ..geometry_msgs import Point
from ..std_msgs import ColorRGBA
from ..std_msgs import ColorRGBA
from ..builtin_interfaces import Duration
from ..geometry_msgs import Point
from ..std_msgs import ColorRGBA

from typing import Any


class ImageMarker:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/ImageMarker.msg

    Args:
        CIRCLE: No information
        LINE_STRIP: No information
        LINE_LIST: No information
        POLYGON: No information
        POINTS: No information
        ADD: No information
        REMOVE: No information
        header: No information
        ns: No information
        id: No information
        type: No information
        action: No information
        position: No information
        scale: No information
        outline_color: No information
        filled: No information
        fill_color: No information
        lifetime: No information
        points: No information
        outline_colors: No information
    """
    def __init__(
        self,
        CIRCLE: int32 | int = None,
        LINE_STRIP: int32 | int = None,
        LINE_LIST: int32 | int = None,
        POLYGON: int32 | int = None,
        POINTS: int32 | int = None,
        ADD: int32 | int = None,
        REMOVE: int32 | int = None,
        header: Header | Any = None,
        ns: string | str = None,
        id: int32 | int = None,
        type: int32 | int = None,
        action: int32 | int = None,
        position: Point | int = None,
        scale: float32 | float = None,
        outline_color: ColorRGBA | Any = None,
        filled: uint8 | int = None,
        fill_color: ColorRGBA | Any = None,
        lifetime: Duration | int = None,
        points: list[Point] | list[int] = None,
        outline_colors: list[ColorRGBA] | list[Any] = None,
    ):
        self.CIRCLE: int32 | int
        self.LINE_STRIP: int32 | int
        self.LINE_LIST: int32 | int
        self.POLYGON: int32 | int
        self.POINTS: int32 | int
        self.ADD: int32 | int
        self.REMOVE: int32 | int
        self.header: Header | Any
        self.ns: string | str
        self.id: int32 | int
        self.type: int32 | int
        self.action: int32 | int
        self.position: Point | int
        self.scale: float32 | float
        self.outline_color: ColorRGBA | Any
        self.filled: uint8 | int
        self.fill_color: ColorRGBA | Any
        self.lifetime: Duration | int
        self.points: list[Point] | list[int]
        self.outline_colors: list[ColorRGBA] | list[Any]

