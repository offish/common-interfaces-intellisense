# flake8: noqa
from common_interfaces.base_types import *

from typing import Any


class MenuEntry:
    """
    https://github.com/ros2/common_interfaces/blob/humble/visualization_msgs/msg/MenuEntry.msg

    Args:
        id: No information
        parent_id: No information
        title: No information
        command: No information
        FEEDBACK: No information
        ROSRUN: No information
        ROSLAUNCH: No information
        command_type: No information
    """
    def __init__(
        self,
        id: uint32 | int = None,
        parent_id: uint32 | int = None,
        title: string | str = None,
        command: string | str = None,
        FEEDBACK: uint8 | int = None,
        ROSRUN: uint8 | int = None,
        ROSLAUNCH: uint8 | int = None,
        command_type: uint8 | int = None,
    ):
        self.id: uint32 | int
        self.parent_id: uint32 | int
        self.title: string | str
        self.command: string | str
        self.FEEDBACK: uint8 | int
        self.ROSRUN: uint8 | int
        self.ROSLAUNCH: uint8 | int
        self.command_type: uint8 | int

