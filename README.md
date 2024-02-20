

# AutoBar: Automatic Bartender Machine


# AutoBar: Automatic Bartender Machine

Welcome to AutoBar, the forefront of automated bartending technology. At its core, AutoBar utilizes a Raspberry Pi connected to a Raspad touchscreen, orchestrating a system of peristaltic pumps for accurate fluid management. The control over mixing operations is executed through a 16-relay Modbus RTU control board, ensuring precise and efficient drink preparation. For the user interface, AutoBar employs React aong with Shadcn to create an immersive and dynamic UI experience. This front-end framework is harmoniously integrated with a Python-powered backend, providing a solid foundation for mixing operations. This architecture not only enhances the user experience but also ensures that AutoBar operates with efficiency and reliability in automated drink mixing.
  
## Hardware Requirements

- Raspberry Pi (Version 3 or higher recommended)

- Raspad 3

- Peristaltic pumps for fluid handling

- 16 relay Modbus RTU control board

- USB to RS485 adapter

## Software Requirements

- Raspbian OS (or any compatible OS)

- Python 3.10

- React 18.2.0

- Node v18.17.1

- Npm 10.2.5

## Installation

1. Setup your Raspberry Pi with the Raspad. Instructions for this can be found on the [Raspad documentation site](https://www.raspad.com/).

2. Install Python and Node.

```

./setup.sh

```

## Usage

Run the application with the following command:

```

python3 main.py

```

The UI will appear on the Raspad's screen. Use the search bar to look for your desired cocktail, select it, and AutoBar will take care of the rest!

## Contributing

We welcome contributions to AutoBar!
