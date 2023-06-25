# AutoBar: Automatic Bartender Machine

Welcome to AutoBar, an Automatic Bartender Machine powered by a Raspberry Pi and a Raspad. This state-of-the-art machine uses peristaltic pumps for fluid handling and a 16 relay Modbus RTU control board for managing operations. This project uses KivyMD for the UI and pymodbus for control over a USB to RS485 adapter.

## Hardware Requirements

- Raspberry Pi (Version 3 or higher recommended)
- Raspad 3
- Peristaltic pumps for fluid handling
- 16 relay Modbus RTU control board
- USB to RS485 adapter

## Software Requirements

- Raspbian OS (or any compatible OS)
- Python 3.10 or higher
- KivyMD
- Pymodbus

## Installation

1.  Setup your Raspberry Pi with the Raspad. Instructions for this can be found on the [Raspad documentation site](https://www.raspad.com/).

2.  Install the required Python dependencies. It is recommended to use a virtual environment (may need to set an alias for your specific python version).

        python3 -m venv venv

3.  Activate the venv

        source venv/bin/activate

4.  Install requirements
    ```
    pip install -r requirements.txt
    ```

## Usage

Run the application with the following command:

    python main.py

The UI will appear on the Raspad's screen. Use the search bar to look for your desired cocktail, select it, and AutoBar will take care of the rest!

## Contributing

We welcome contributions to AutoBar!
