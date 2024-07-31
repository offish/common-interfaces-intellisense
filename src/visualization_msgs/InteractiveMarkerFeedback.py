# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from ..geometry_msgs import Pose
from ..geometry_msgs import Point

from typing import Any


class InteractiveMarkerFeedback:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/InteractiveMarkerFeedback.msg

    Args:
        header: No information
        client_id: No information
        marker_name: No information
        control_name: No information
        KEEP_ALIVE: No information
        POSE_UPDATE: No information
        MENU_SELECT: No information
        BUTTON_CLICK: No information
        MOUSE_DOWN: No information
        MOUSE_UP: No information
        event_type: No information
        pose: No information
        menu_entry_id: No information
        mouse_point: No information
        mouse_point_valid: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        client_id: string | str = None,
        marker_name: string | str = None,
        control_name: string | str = None,
        KEEP_ALIVE: uint8 | int = None,
        POSE_UPDATE: uint8 | int = None,
        MENU_SELECT: uint8 | int = None,
        BUTTON_CLICK: uint8 | int = None,
        MOUSE_DOWN: uint8 | int = None,
        MOUSE_UP: uint8 | int = None,
        event_type: uint8 | int = None,
        pose: Pose | Any = None,
        menu_entry_id: uint32 | int = None,
        mouse_point: Point | int = None,
        mouse_point_valid: bool = None,
    ):
        self.header: Header | Any
        self.client_id: string | str
        self.marker_name: string | str
        self.control_name: string | str
        self.KEEP_ALIVE: uint8 | int
        self.POSE_UPDATE: uint8 | int
        self.MENU_SELECT: uint8 | int
        self.BUTTON_CLICK: uint8 | int
        self.MOUSE_DOWN: uint8 | int
        self.MOUSE_UP: uint8 | int
        self.event_type: uint8 | int
        self.pose: Pose | Any
        self.menu_entry_id: uint32 | int
        self.mouse_point: Point | int
        self.mouse_point_valid: bool

