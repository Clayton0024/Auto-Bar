import time

from pymodbus.client.sync import ModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder


def control_relays(relay_data):
    # Connect to the Modbus RTU slave
    client = ModbusSerialClient(method="rtu", port="COM7", baudrate=9600, timeout=1)

    if not client.connect():
        print("Failed to connect to the Modbus RTU slave")
        return

    for relay in relay_data:
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
    for relay in relay_data:
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


# Example usage
relay_data = [
    {"relay_number": 1, "duration": 3},  # Relay 1 will remain on for 3 seconds
    {"relay_number": 2, "duration": 5},  # Relay 2 will remain on for 5 seconds
    {"relay_number": 3, "duration": 2},  # Relay 3 will remain on for 2 seconds
]

control_relays(relay_data)
