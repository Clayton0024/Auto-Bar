from abc import ABC, abstractmethod
from enum import Enum
from typing import List

import libraries.relay_boards as relay_boards
import libraries.relay_modbus as relay_modbus


class RelayStatus(Enum):
    FAULT = 0
    ON = 1
    OFF = 2


class PumpInterface(ABC):
    """
    Defines the interface for a set of pumps.
    """

    @abstractmethod
    def get_status(self, pump_number: int = None) -> List[RelayStatus]:
        """Get status of relay(s).  If no pump number is specified, return status of all pumps."""
        pass

    @abstractmethod
    def turn_on(self, pump_number: int):
        """Turn on relay."""
        pass

    @abstractmethod
    def turn_off(self, pump_number: int):
        """Turn off relay for `pump_number`"""
        pass


class PumpR421A08(PumpInterface):
    """
    Defines the interface for a set of pumps using a single R421A08 relay board.
    """

    def __init__(self, modbus_obj: relay_modbus.modbus.Modbus):
        self._relay_board = relay_boards.R421A08(modbus_obj)
        self._num_pumps = relay_boards.R421A08.num_relays

    def get_status(self, pump_number: int = None) -> List[RelayStatus]:
        """Get status of relay(s). If no pump number is specified, return status of all pumps."""
        if pump_number is None:
            return [self._get_pump_status(p) for p in range(1, self._num_pumps + 1)]
        else:
            return [self._get_pump_status(pump_number)]

    def _get_pump_status(self, pump_number: int) -> RelayStatus:
        """Get status of a single pump."""
        status = self._relay_board.get_status(pump_number)
        if status == -1:
            return RelayStatus.FAULT
        elif status == 0:
            return RelayStatus.OFF
        elif status == 1:
            return RelayStatus.ON

    def turn_on(self, pump_number: int):
        """Turn on relay for the specified pump."""
        self._relay_board.on(pump_number)

    def turn_off(self, pump_number: int):
        """Turn off relay for the specified pump."""
        self._relay_board.off(pump_number)
