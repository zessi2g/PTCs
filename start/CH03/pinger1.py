#!/usr/bin/env python3
# First example of pinging from Python
# By Ed, 10/4/21

# Import necessary python modules
import platform
import os

# Assign IP address
ip = "128.0.0.1"
# Craft ping command
ping_cmd = f"ping -c 1 -w 2 {ip} > /dev/null 2>&1"
# run command and capture exit code
exit_code = os.system(ping_cmd)
# Print exit code to screen
print(exit_code)
