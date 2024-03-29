from abc import ABC, abstractmethod
from enum import Enum

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
    def get_status(self, pump_number: int = None) -> RelayStatus:
        """Get status of relay.  Or if no pump number is specified, status of the relay board."""
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

    def _get_board_status(self) -> RelayStatus:
        """Check if relay board is on."""
        return RelayStatus.ON

    def get_status(self, pump_number: int = None) -> RelayStatus:
        if pump_number is None:
            return self._get_board_status()
        else:
            return self._get_pump_status(pump_number)

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
        self._relay_board.on(pump_number)

    def turn_off(self, pump_number: int):
        self._relay_board.off(pump_number)
