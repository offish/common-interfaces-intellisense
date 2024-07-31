# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header
from ..geometry_msgs import Pose
from . import MenuEntry
from . import InteractiveMarkerControl

from typing import Any


class InteractiveMarker:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/InteractiveMarker.msg

    Args:
        header: No information
        pose: No information
        name: No information
        description: No information
        scale: No information
        menu_entries: No information
        controls: No information
    """
    def __init__(
        self,
        header: Header | Any = None,
        pose: Pose | Any = None,
        name: string | str = None,
        description: string | str = None,
        scale: float32 | float = None,
        menu_entries: list[MenuEntry] | list[Any] = None,
        controls: list[InteractiveMarkerControl] | list[Any] = None,
    ):
        self.header: Header | Any
        self.pose: Pose | Any
        self.name: string | str
        self.description: string | str
        self.scale: float32 | float
        self.menu_entries: list[MenuEntry] | list[Any]
        self.controls: list[InteractiveMarkerControl] | list[Any]

