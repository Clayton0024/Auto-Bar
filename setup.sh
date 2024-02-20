#!/bin/bash

# Exit in case of error
set -e

# Checking for Python installation
echo "Checking for Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "Python could not be found, please install Python 3."
    exit 1
fi

# Checking for Node.js installation
echo "Checking for Node.js installation..."
if ! command -v node &> /dev/null; then
    echo "Node.js could not be found, please install Node.js."
    exit 1
fi

# Creating and activating Python virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv
echo "Activating virtual environment..."
source venv/bin/activate

# Installing Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Deactivating virtual environment
deactivate


# Installing Node.js dependencies
cd Frontend  # Change to the directory containing package.json
echo "Installing dependencies..."
npm install
echo "Fetching ShadCN Components..."
node install-shadcn-deps.js

# Navigate back to the base directory
cd ..

echo "Setup completed successfully."
