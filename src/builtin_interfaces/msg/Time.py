from ..common_interfaces.base_types import int32, uint32


class Time:
    def __init__(
        self,
        sec: int32 | int = None,
        nanosec: uint32 | int = None,
    ) -> None:
        """https://docs.ros2.org/galactic/api/builtin_interfaces/msg/Time.html

        Args:
            sec: No information
            nanosec: No information
        """
        self.sec: int32 | int
        self.nanosec: uint32 | int
