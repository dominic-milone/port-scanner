# Port Scanner

A simple TCP port scanner written in Python. It checks a range of ports on a target machine and reports which ones are open, similar to a basic Nmap connect scan.

I built this to learn how ports and TCP connections work, and to practice Python and Git.

> **Note:** Only scan machines you own or have permission to scan. Scanning networks without permission can be illegal.

## How it works

For each port, the scanner tries to open a TCP connection. If the connection succeeds (the TCP three way handshake completes), something is listening on that port, so it's reported as open. If the connection is refused or times out, the port is closed.

## Requirements

* Python 3
* No extra libraries needed (uses the built in `socket` and `argparse` modules)

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
Port 5040 is open
```

## What I learned

* How TCP ports and the three way handshake work
* Using Python's `socket` library to make network connections
* Writing reusable functions and loops
* Taking command line arguments with `argparse`
* Using Git and GitHub to track and share my code

## Planned features

* [ ] Scan multiple ports at once with threads for faster scans
* [ ] Show the common service name for each open port
* [ ] Banner grabbing to identify the software running on a port
* [ ] Save results to a file
