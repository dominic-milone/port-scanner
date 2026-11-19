# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:58:47 2026

@author: dom
"""

import socket

host = "127.0.0.1"

### Check Multiple Ports

def scan_port(host,port):
    sock = socket.socket(socket.AF_INET, 
                         socket.SOCK_STREAM)
    sock.settimeout(0.25)
    result = sock.connect_ex((host,port))
    sock.close()
    return result == 0

for port in range(5000,8001):
    if scan_port(host, port):
        print(f"Port {port} is open")
        
    else:
        print(f"Port {port} is closed")
            





