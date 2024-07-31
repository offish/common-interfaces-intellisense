# flake8: noqa
from ..common_interfaces.base_types import *
from . import InteractiveMarker
from . import InteractiveMarkerPose

from typing import Any


class InteractiveMarkerUpdate:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/InteractiveMarkerUpdate.msg

    Args:
        server_id: No information
        seq_num: No information
        KEEP_ALIVE: No information
        UPDATE: No information
        type: No information
        markers: No information
        poses: No information
        erases: No information
    """
    def __init__(
        self,
        server_id: string | str = None,
        seq_num: uint64 | int = None,
        KEEP_ALIVE: uint8 | int = None,
        UPDATE: uint8 | int = None,
        type: uint8 | int = None,
        markers: list[InteractiveMarker] | list[Any] = None,
        poses: list[InteractiveMarkerPose] | list[Any] = None,
        erases: list[string] | list[Any] = None,
    ):
        self.server_id: string | str
        self.seq_num: uint64 | int
        self.KEEP_ALIVE: uint8 | int
        self.UPDATE: uint8 | int
        self.type: uint8 | int
        self.markers: list[InteractiveMarker] | list[Any]
        self.poses: list[InteractiveMarkerPose] | list[Any]
        self.erases: list[string] | list[Any]

