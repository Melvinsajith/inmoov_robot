#!/bin/bash
# Exit if we encounter an error
set -e
# Set permissions for us to access GPIO and I2C from user space
sudo ./scripts/setPermissions.sh $USER
# Then install servokit
sudo apt-get uninstall python3-pip -y
sudo -H pip3 uninstall adafruit-circuitpython-servokit
echo ""
echo "Adafruit CircuitPython ServoKit installed."
echo "Please logoff/logon or reboot in order for I2C permissions to take effect."
echo ""


