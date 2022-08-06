#!/usr/bin/env python3
# Fouth example of pinging from Python
# By Ed, 10/11/21

# Import necessary python modules
import platform
import os

def ping_address(ip_address):
    # Find current OS
    current_os = platform.system().lower()
    # Craft ping command based on OS
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip_address} > nul"
    else:
        ping_cmd = f"ping -c 1 -w 2 {ip_address} > /dev/null 2>&1"
    # run command and capture exit code
    exit_code = os.system(ping_cmd)
    return exit_code

for octet in range(254):
    # Assign IP address
    ip = "127.0.0.{0}".format(octet + 1)
    # Call function
    exit_code = ping_address(ip)
    # Print exit code to screen
    print("{0}: {1}".format(ip,exit_code))
