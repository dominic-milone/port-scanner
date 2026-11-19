# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:58:47 2026

@author: dom
"""

import socket
import argparse
import time
import subprocess
import sys

count = 0


if len(sys.argv) == 1:
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
        
    sys.argv += ["127.0.0.1", "--end", str(int(end_port)), "--timeout", str(timeout)]


 
        
### Parser
parser = argparse.ArgumentParser(description="Simple TCP port scanner")
parser.add_argument("host", help="IP address to scan")
parser.add_argument("--start", type=int, default=1, help="First port to scan")
parser.add_argument("--end", type=int, default=1024, help="Last port to scan")
parser.add_argument("--timeout", type=float, default=0.5, help="Seconds to wait per port")

args = parser.parse_args()


### Check Multiple Ports
def scan_port(host,port,):
    sock = socket.socket(socket.AF_INET, 
                         socket.SOCK_STREAM)
    sock.settimeout(args.timeout)
    result = sock.connect_ex((host,port))
    sock.close()
    return result == 0


### Start timer
start_time = time.time()


### Find what the port is connected to
def get_service(port):
    try:
       return socket.getservbyport(port,"tcp")
    except OSError:
            return "unknown"

for port in range(args.start, args.end + 1):
    if scan_port(args.host, port):
        port_details = (f"Port {port} is open ({get_service(port)}) ")
        count += 1
        print(port_details)

        

end_time = time.time()
total_time = end_time - start_time
print(f"Scan complete in {total_time:.2f} seconds")
print("There were a total of", count, "port(s) that were open")

with open("results.txt", "w", encoding="utf-8") as file:
    file.write(port_details)
