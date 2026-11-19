# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 21:58:47 2026

@author: dom
"""

import socket
import argparse
import time

count = 0

parser = argparse.ArgumentParser(description="Simple TCP port scanner")
parser.add_argument("host", help="IP address to scan")
parser.add_argument("--start", type=int, default=1, help="First port to scan")
parser.add_argument("--end", type=int, default=1024, help="Last port to scan")
args = parser.parse_args()

### Check Multiple Ports

def scan_port(host,port):
    sock = socket.socket(socket.AF_INET, 
                         socket.SOCK_STREAM)
    sock.settimeout(0.03)
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
        port_details = (f"Port {port} is open ({get_service(port)})")
        print(port_details)

for port in range(args.start, args.end + 1):
    if scan_port(args.host,port):
        count  += 1
        

end_time = time.time()
total_time = end_time - start_time
print(f"Scan complete in {total_time:.2f} seconds")
print("There were a total of", count, "port(s) that were open")

with open("results.txt", "w", encoding="utf-8") as file:
    file.write(port_details)
