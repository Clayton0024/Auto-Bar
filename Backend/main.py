import time
from autobar_interface import Autobar
from communication_interface import TcpCommunicator

autobar = Autobar()

communicator = TcpCommunicator("127.0.0.1", 6969, autobar.on_message_received)
communicator.start()


while True:
    # main loop.  autobar is now running in the background
    time.sleep(1)