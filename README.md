# Port Scanner

A simple TCP port scanner written in Python. It checks a range of ports on a target machine, reports which ones are open, shows the common service name for each one, and times how long the scan takes, similar to a basic Nmap connect scan.

I built this to learn how ports and TCP connections work, and to practice Python and Git.

> **Note:** Only scan machines you own or have permission to scan. Scanning networks without permission can be illegal.

## How it works

For each port, the scanner tries to open a TCP connection. If the connection succeeds (the TCP three way handshake completes), something is listening on that port, so it's reported as open. If the connection is refused or times out, the port is closed.

For each open port, the scanner looks up the service that normally runs on that port number (for example, 445 is `microsoft-ds`). If the port isn't in the system's list, it shows `unknown`.

When the scan finishes, it prints how long it took.

## Requirements

* Python 3
* No extra libraries needed (uses the built in `socket`, `argparse`, and `time` modules)

## Usage

```
python port_scanner.py <host> [--start PORT] [--end PORT]
```

| Argument | Description | Default |
|---|---|---|
| `host` | IP address to scan (required) | none |
| `--start` | First port to scan | 1 |
| `--end` | Last port to scan | 1024 |

### Examples

Scan ports 1 to 1024 on your own computer:
```
python port_scanner.py 127.0.0.1
```

Scan a custom range:
```
python port_scanner.py 127.0.0.1 --start 5000 --end 5050
```

Show the help menu:
```
python port_scanner.py -h
```

## Example output

```
Scanning 127.0.0.1 ports 1 to 1024...
Port 135 is open (epmap)
Port 445 is open (microsoft-ds)
Port 903 is open (unknown)
Port 913 is open (unknown)
Scan complete in 0.84 seconds
```

Ports marked `unknown` can be traced to the program that owns them. On Windows:
```
netstat -ano | findstr :903
tasklist /svc /FI "PID eq <PID>"
```
In this example, ports 903 and 913 belonged to VMware's Authorization Service.

## What I learned

* How TCP ports and the three way handshake work
* Using Python's `socket` library to make network connections
* Writing reusable functions and loops
* Taking command line arguments with `argparse`
* Handling errors with `try` and `except`
* Timing code with the `time` module and formatting numbers in f-strings
* Why short timeouts can make a scanner miss open ports
* Tracing an open port back to the process that owns it with `netstat` and `tasklist`
* Using Git and GitHub to track and share my code

## Planned features

* [ ] Scan multiple ports at once with threads for faster scans
* [x] Show the common service name for each open port
* [x] Time how long each scan takes
* [ ] Banner grabbing to identify the software running on a port
* [ ] Save results to a file
