# flake8: noqa
from common_interfaces.base_types import *
from . import GoalID

from typing import Any


class GoalStatus:
    """
    https://github.com/ros2/common_interfaces/blob/humble/actionlib_msgs/msg/GoalStatus.msg

    Args:
        goal_id: No information
        status: No information
        PENDING: No information
        ACTIVE: No information
        PREEMPTED: No information
        SUCCEEDED: No information
        ABORTED: No information
        REJECTED: No information
        PREEMPTING: No information
        RECALLING: No information
        RECALLED: No information
        LOST: No information
        text: No information
    """
    def __init__(
        self,
        goal_id: GoalID | Any = None,
        status: uint8 | int = None,
        PENDING: uint8 | int = None,
        ACTIVE: uint8 | int = None,
        PREEMPTED: uint8 | int = None,
        SUCCEEDED: uint8 | int = None,
        ABORTED: uint8 | int = None,
        REJECTED: uint8 | int = None,
        PREEMPTING: uint8 | int = None,
        RECALLING: uint8 | int = None,
        RECALLED: uint8 | int = None,
        LOST: uint8 | int = None,
        text: string | str = None,
    ):
        self.goal_id: GoalID | Any
        self.status: uint8 | int
        self.PENDING: uint8 | int
        self.ACTIVE: uint8 | int
        self.PREEMPTED: uint8 | int
        self.SUCCEEDED: uint8 | int
        self.ABORTED: uint8 | int
        self.REJECTED: uint8 | int
        self.PREEMPTING: uint8 | int
        self.RECALLING: uint8 | int
        self.RECALLED: uint8 | int
        self.LOST: uint8 | int
        self.text: string | str

