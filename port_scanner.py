# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:58:47 2026

@author: dom
"""

import socket
import argparse

parser = argparse.ArgumentParser(description="Simple TCP port scanner")
parser.add_argument("host", help="IP address to scan")
parser.add_argument("--start", type=int, default=1, help="First port to scan")
parser.add_argument("--end", type=int, default=1024, help="Last port to scan")
args = parser.parse_args()

### Check Multiple Ports

def scan_port(host,port):
    sock = socket.socket(socket.AF_INET, 
                         socket.SOCK_STREAM)
    sock.settimeout(0.25)
    result = sock.connect_ex((host,port))
    sock.close()
    return result == 0

for port in range(args.start, args.end + 1):
    if scan_port(args.host, port):
        print(f"Port {port} is open")
        
            





