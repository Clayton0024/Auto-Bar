from .modbus import (FRAME_DELAY, Modbus, SerialOpenException,
                     TransferException, get_frame_str)
from .serial_ports import get_serial_ports

__version__ = "1.0.1"
VERSION = __version__
