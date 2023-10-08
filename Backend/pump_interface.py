from abc import ABC, abstractmethod
from enum import Enum

from libraries.relay_boards.R421A08 import R421A08
from libraries.relay_modbus import Modbus


class RelayStatus(Enum):
    FAULT = 0
    ON = 1
    OFF = 2


class PumpInterface(ABC):
    """
    Defines the interface for a single pump.
    """

    @abstractmethod
    def get_status(self) -> RelayStatus:
        """Get status of relay."""
        pass

    @abstractmethod
    def turn_on(self):
        """Turn on relay."""
        pass

    @abstractmethod
    def turn_off(self):
        """Turn off relay."""
        pass


class PumpR421A08(PumpInterface):
    """
    Defines the interface for a single pump.
    """

    def __init__(self, modbus_obj: Modbus):
        self._relay_board = R421A08(modbus_obj)

    def get_status(self) -> RelayStatus:
        """Get status of relay."""
        status = self._relay_board.get_status()
        if status == -1:
            return RelayStatus.FAULT
        elif status == 0:
            return RelayStatus.OFF
        elif status == 1:
            return RelayStatus.ON

    def turn_on(self):
        """Turn on relay."""
        self._relay_board.on()

    def turn_off(self):
        """Turn off relay."""
        self._relay_board.off()
