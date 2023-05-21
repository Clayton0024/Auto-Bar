import serial
import time

#TODO convert to use pymodbus!!

def control_relays(relay_data):
    # Open the serial port
    ser = serial.Serial('COM7', 9600, timeout=1)

    for relay in relay_data:
        # Define the payload bytes for turning on the relay
        slave_id = 1  # Board number
        function = 6  # Control function
        relay_number = relay['relay_number']
        action_on = 1  # Action: 1 = Close (turn on the switch)

        # Construct the payload to turn on the relay
        payload_on = bytearray([slave_id, function, relay_number >> 8, relay_number & 0xFF, action_on, 0, 0, 0])

        # Send the payload to turn on the relay
        ser.write(payload_on)
        time.sleep(0.1)  # Wait for the relay board to process the command

    # Close the serial port temporarily
    ser.close()

    # Wait for the specified durations for each relay
    for relay in relay_data:
        # Open the serial port again
        ser = serial.Serial('COM7', 9600, timeout=1)

        # Define the payload bytes for turning off the relay
        relay_number = relay['relay_number']
        duration = relay['duration']

        # Calculate the CRC values for turning off the relay
        crc = bytearray([slave_id, function, relay_number >> 8, relay_number & 0xFF, 2, duration])
        crc16 = 0xFFFF

        for byte in crc:
            crc16 ^= byte
            for _ in range(8):
                if crc16 & 0x0001:
                    crc16 >>= 1
                    crc16 ^= 0xA001
                else:
                    crc16 >>= 1

        crc_lsb = crc16 & 0xFF
        crc_msb = (crc16 >> 8) & 0xFF

        payload_off = bytearray([slave_id, function, relay_number >> 8, relay_number & 0xFF, 2, duration, crc_lsb, crc_msb])

        # Wait for the specified duration
        time.sleep(duration)

        # Send the payload to turn off the relay
        ser.write(payload_off)
        time.sleep(0.5)  # Increase the delay to allow the relay board to process the command

        # Close the serial port
        ser.close()


# Example usage
relay_data = [
    {'relay_number': 1, 'duration': 3},  # Relay 1 will remain on for 3 seconds
    {'relay_number': 2, 'duration': 5},  # Relay 2 will remain on for 5 seconds
    {'relay_number': 3, 'duration': 2},  # Relay 3 will remain on for 2 seconds
]

control_relays(relay_data)
