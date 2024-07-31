# flake8: noqa
from ..common_interfaces.base_types import *
from ..std_msgs import Header

from typing import Any


class BatteryState:
    """
    https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/BatteryState.msg

    Args:
        POWER_SUPPLY_STATUS_UNKNOWN: No information
        POWER_SUPPLY_STATUS_CHARGING: No information
        POWER_SUPPLY_STATUS_DISCHARGING: No information
        POWER_SUPPLY_STATUS_NOT_CHARGING: No information
        POWER_SUPPLY_STATUS_FULL: No information
        POWER_SUPPLY_HEALTH_UNKNOWN: No information
        POWER_SUPPLY_HEALTH_GOOD: No information
        POWER_SUPPLY_HEALTH_OVERHEAT: No information
        POWER_SUPPLY_HEALTH_DEAD: No information
        POWER_SUPPLY_HEALTH_OVERVOLTAGE: No information
        POWER_SUPPLY_HEALTH_UNSPEC_FAILURE: No information
        POWER_SUPPLY_HEALTH_COLD: No information
        POWER_SUPPLY_HEALTH_WATCHDOG_TIMER_EXPIRE: No information
        POWER_SUPPLY_HEALTH_SAFETY_TIMER_EXPIRE: No information
        POWER_SUPPLY_TECHNOLOGY_UNKNOWN: No information
        POWER_SUPPLY_TECHNOLOGY_NIMH: No information
        POWER_SUPPLY_TECHNOLOGY_LION: No information
        POWER_SUPPLY_TECHNOLOGY_LIPO: No information
        POWER_SUPPLY_TECHNOLOGY_LIFE: No information
        POWER_SUPPLY_TECHNOLOGY_NICD: No information
        POWER_SUPPLY_TECHNOLOGY_LIMN: No information
        header: No information
        voltage: No information
        temperature: No information
        current: No information
        charge: No information
        capacity: No information
        design_capacity: No information
        percentage: No information
        power_supply_status: No information
        power_supply_health: No information
        power_supply_technology: No information
        present: No information
        cell_voltage: No information
        cell_temperature: No information
        location: No information
        serial_number: No information
    """
    def __init__(
        self,
        POWER_SUPPLY_STATUS_UNKNOWN: uint8 | int = None,
        POWER_SUPPLY_STATUS_CHARGING: uint8 | int = None,
        POWER_SUPPLY_STATUS_DISCHARGING: uint8 | int = None,
        POWER_SUPPLY_STATUS_NOT_CHARGING: uint8 | int = None,
        POWER_SUPPLY_STATUS_FULL: uint8 | int = None,
        POWER_SUPPLY_HEALTH_UNKNOWN: uint8 | int = None,
        POWER_SUPPLY_HEALTH_GOOD: uint8 | int = None,
        POWER_SUPPLY_HEALTH_OVERHEAT: uint8 | int = None,
        POWER_SUPPLY_HEALTH_DEAD: uint8 | int = None,
        POWER_SUPPLY_HEALTH_OVERVOLTAGE: uint8 | int = None,
        POWER_SUPPLY_HEALTH_UNSPEC_FAILURE: uint8 | int = None,
        POWER_SUPPLY_HEALTH_COLD: uint8 | int = None,
        POWER_SUPPLY_HEALTH_WATCHDOG_TIMER_EXPIRE: uint8 | int = None,
        POWER_SUPPLY_HEALTH_SAFETY_TIMER_EXPIRE: uint8 | int = None,
        POWER_SUPPLY_TECHNOLOGY_UNKNOWN: uint8 | int = None,
        POWER_SUPPLY_TECHNOLOGY_NIMH: uint8 | int = None,
        POWER_SUPPLY_TECHNOLOGY_LION: uint8 | int = None,
        POWER_SUPPLY_TECHNOLOGY_LIPO: uint8 | int = None,
        POWER_SUPPLY_TECHNOLOGY_LIFE: uint8 | int = None,
        POWER_SUPPLY_TECHNOLOGY_NICD: uint8 | int = None,
        POWER_SUPPLY_TECHNOLOGY_LIMN: uint8 | int = None,
        header: Header | Any = None,
        voltage: float32 | float = None,
        temperature: float32 | float = None,
        current: float32 | float = None,
        charge: float32 | float = None,
        capacity: float32 | float = None,
        design_capacity: float32 | float = None,
        percentage: float32 | float = None,
        power_supply_status: uint8 | int = None,
        power_supply_health: uint8 | int = None,
        power_supply_technology: uint8 | int = None,
        present: bool = None,
        cell_voltage: list[float32] | list[float] = None,
        cell_temperature: list[float32] | list[float] = None,
        location: string | str = None,
        serial_number: string | str = None,
    ):
        self.POWER_SUPPLY_STATUS_UNKNOWN: uint8 | int
        self.POWER_SUPPLY_STATUS_CHARGING: uint8 | int
        self.POWER_SUPPLY_STATUS_DISCHARGING: uint8 | int
        self.POWER_SUPPLY_STATUS_NOT_CHARGING: uint8 | int
        self.POWER_SUPPLY_STATUS_FULL: uint8 | int
        self.POWER_SUPPLY_HEALTH_UNKNOWN: uint8 | int
        self.POWER_SUPPLY_HEALTH_GOOD: uint8 | int
        self.POWER_SUPPLY_HEALTH_OVERHEAT: uint8 | int
        self.POWER_SUPPLY_HEALTH_DEAD: uint8 | int
        self.POWER_SUPPLY_HEALTH_OVERVOLTAGE: uint8 | int
        self.POWER_SUPPLY_HEALTH_UNSPEC_FAILURE: uint8 | int
        self.POWER_SUPPLY_HEALTH_COLD: uint8 | int
        self.POWER_SUPPLY_HEALTH_WATCHDOG_TIMER_EXPIRE: uint8 | int
        self.POWER_SUPPLY_HEALTH_SAFETY_TIMER_EXPIRE: uint8 | int
        self.POWER_SUPPLY_TECHNOLOGY_UNKNOWN: uint8 | int
        self.POWER_SUPPLY_TECHNOLOGY_NIMH: uint8 | int
        self.POWER_SUPPLY_TECHNOLOGY_LION: uint8 | int
        self.POWER_SUPPLY_TECHNOLOGY_LIPO: uint8 | int
        self.POWER_SUPPLY_TECHNOLOGY_LIFE: uint8 | int
        self.POWER_SUPPLY_TECHNOLOGY_NICD: uint8 | int
        self.POWER_SUPPLY_TECHNOLOGY_LIMN: uint8 | int
        self.header: Header | Any
        self.voltage: float32 | float
        self.temperature: float32 | float
        self.current: float32 | float
        self.charge: float32 | float
        self.capacity: float32 | float
        self.design_capacity: float32 | float
        self.percentage: float32 | float
        self.power_supply_status: uint8 | int
        self.power_supply_health: uint8 | int
        self.power_supply_technology: uint8 | int
        self.present: bool
        self.cell_voltage: list[float32] | list[float]
        self.cell_temperature: list[float32] | list[float]
        self.location: string | str
        self.serial_number: string | str

