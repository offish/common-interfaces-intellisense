# flake8: noqa
from common_interfaces.base_types import *
from . import InteractiveMarker

from typing import Any


class InteractiveMarkerInit:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/InteractiveMarkerInit.msg

    Args:
        server_id: No information
        seq_num: No information
        markers: No information
    """
    def __init__(
        self,
        server_id: string | str = None,
        seq_num: uint64 | int = None,
        markers: list[InteractiveMarker] | list[Any] = None,
    ):
        self.server_id: string | str
        self.seq_num: uint64 | int
        self.markers: list[InteractiveMarker] | list[Any]

