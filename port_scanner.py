# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:58:47 2026

@author: dom
"""

import socket

host = "127.0.0.1"
port = 8000

sock = socket.socket(socket.AF_INET, 
                     socket.SOCK_STREAM)

result = sock.connect_ex((host,port))

if result == 0:
    print(f"Port {port} is open")
else:
    print(f"Port {port} is closed")
    
sock.close()