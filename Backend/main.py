import time
from autobar_interface import Autobar
from hardware_interface import HardwareInterface, INTERFACE_ENV
from communication_interface import TcpCommunicator

# hardware_interface = HardwareInterface("/dev/ttyUSB0", 9600, INTERFACE_ENV.DESKTOP)
autobar = Autobar()

communicator = TcpCommunicator("127.0.0.1", 6969, autobar.on_message_received)
communicator.start()


while True:
    # main loop.  autobar is now running in the background
    time.sleep(1)