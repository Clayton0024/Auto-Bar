import time
from autobar_interface import Autobar
from hardware_interface import HardwareInterface, INTERFACE_ENV

# hardware_interface = HardwareInterface("/dev/ttyUSB0", 9600, INTERFACE_ENV.DESKTOP)
autobar = Autobar()

while True:
    # main loop.  autobar is now running in the background
    time.sleep(1)