# flake8: noqa
from ..common_interfaces.base_types import *
from ..geometry_msgs import Quaternion
from . import Marker

from typing import Any


class InteractiveMarkerControl:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/InteractiveMarkerControl.msg

    Args:
        name: No information
        orientation: No information
        INHERIT: No information
        FIXED: No information
        VIEW_FACING: No information
        orientation_mode: No information
        NONE: No information
        MENU: No information
        BUTTON: No information
        MOVE_AXIS: No information
        MOVE_PLANE: No information
        ROTATE_AXIS: No information
        MOVE_ROTATE: No information
        MOVE_3D: No information
        ROTATE_3D: No information
        MOVE_ROTATE_3D: No information
        interaction_mode: No information
        always_visible: No information
        markers: No information
        independent_marker_orientation: No information
        description: No information
    """
    def __init__(
        self,
        name: string | str = None,
        orientation: Quaternion | Any = None,
        INHERIT: uint8 | int = None,
        FIXED: uint8 | int = None,
        VIEW_FACING: uint8 | int = None,
        orientation_mode: uint8 | int = None,
        NONE: uint8 | int = None,
        MENU: uint8 | int = None,
        BUTTON: uint8 | int = None,
        MOVE_AXIS: uint8 | int = None,
        MOVE_PLANE: uint8 | int = None,
        ROTATE_AXIS: uint8 | int = None,
        MOVE_ROTATE: uint8 | int = None,
        MOVE_3D: uint8 | int = None,
        ROTATE_3D: uint8 | int = None,
        MOVE_ROTATE_3D: uint8 | int = None,
        interaction_mode: uint8 | int = None,
        always_visible: bool = None,
        markers: list[Marker] | list[Any] = None,
        independent_marker_orientation: bool = None,
        description: string | str = None,
    ):
        self.name: string | str
        self.orientation: Quaternion | Any
        self.INHERIT: uint8 | int
        self.FIXED: uint8 | int
        self.VIEW_FACING: uint8 | int
        self.orientation_mode: uint8 | int
        self.NONE: uint8 | int
        self.MENU: uint8 | int
        self.BUTTON: uint8 | int
        self.MOVE_AXIS: uint8 | int
        self.MOVE_PLANE: uint8 | int
        self.ROTATE_AXIS: uint8 | int
        self.MOVE_ROTATE: uint8 | int
        self.MOVE_3D: uint8 | int
        self.ROTATE_3D: uint8 | int
        self.MOVE_ROTATE_3D: uint8 | int
        self.interaction_mode: uint8 | int
        self.always_visible: bool
        self.markers: list[Marker] | list[Any]
        self.independent_marker_orientation: bool
        self.description: string | str

