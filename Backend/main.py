import datetime
import logging
import time
import subprocess
from autobar_interface import Autobar
from communication_interface import TcpCommunicator

# set up logging
# to use logging in other files, use the following:
# import logging
# logging.debug("This is a debug message")
# logging.info("Informational message")
# etc.
now = datetime.datetime.now()
subprocess.run(['mkdir', '-p', 'logs'])
log_filename = "autobar_" + now.strftime("%Y%m%d_%H%M%S") + ".log"
log_filepath = "logs/" + log_filename
logging.basicConfig(filename=log_filepath, encoding='utf-8', level=logging.DEBUG)
logging.info("Starting Autobar")

autobar = Autobar()

communicator = TcpCommunicator("127.0.0.1", 6969, autobar.on_message_received)
communicator.start()


while True:
    # main loop.  autobar is now running in the background
    time.sleep(1)