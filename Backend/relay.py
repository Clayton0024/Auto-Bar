import time

from pymodbus.client import ModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder


class relay:
    def __init__(self, relay_data):
        self.relay_data = relay_data

    def control_relays(self):
        # Connect to the Modbus RTU slave
        client = ModbusSerialClient(method="rtu", port="COM7", baudrate=9600, timeout=1)

        if not client.connect():
            print("Failed to connect to the Modbus RTU slave")
            return

        for relay in self.relay_data:
            # Define the payload bytes for turning on the relay
            slave_id = 1  # Board number
            relay_number = relay["relay_number"]
            action_on = 1  # Action: 1 = Close (turn on the switch)

            # Construct the payload to turn on the relay
            builder = BinaryPayloadBuilder(byteorder=Endian.Big)
            builder.add_8bit_uint(action_on)

            # Send the payload to turn on the relay
            client.write_coil(relay_number, value=bool(builder.to_registers()[0]), unit=slave_id)

            time.sleep(0.1)  # Wait for the relay board to process the command

        # Wait for the specified durations for each relay
        for relay in self.relay_data:
            # Define the payload bytes for turning off the relay
            relay_number = relay["relay_number"]
            duration = relay["duration"]

            # Wait for the specified duration
            time.sleep(duration)

            # Send the payload to turn off the relay
            client.write_coil(relay_number, value=False, unit=slave_id)

            time.sleep(0.5)  # Increase the delay to allow the relay board to process the command

        # Close the connection to the Modbus RTU slave
        client.close()

        data = [(1, 15), (2, 10), (3, 5)]

        # sort the data array to acending order by time
        # while sorting store an array of relay numbers
        # start timer & send multiple relay start command
        # confirm relay start
        # pull first tuple from sorted data array
        # compare current time to specified time
        # send single shutdown command to relay
        # confirm relay shutdown
        # pull next tuple from sorted Data array and repeat time compart process

        # may need to spin up new thread for this process
        # thread will need to communicate with safety process
        # thread will need to communicate with UI process

        # Requirements
        #     abort operation commanded from safety or UI
        #     report progress back to the UI (Running, Stopped, Error, Complete)
        #     report all commands to the safety module (relay state checks redundant in this module)
