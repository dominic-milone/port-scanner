# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:04:54 2026

@author: dom
"""

import subprocess
import sys

while True:
    try:
        end_port = float(input("What is your desired end port?: "))
        if end_port >= 0:
            break
        print("port number must be greater than or equal to 0, try again.")
        if end_port == ".":
            break
    except ValueError:
        print("Invalid number, try again.")


while True:
    try:
        timeout = float(input("What is your desired timeout?: "))
        if timeout > 0:
            break
        print("timeout number must be greater than 0, try again.")
    except ValueError:
        print("Invalid number, try again.")