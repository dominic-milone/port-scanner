# Port Scanner

A simple TCP port scanner written in Python. It checks a range of ports on a target machine, reports which ones are open, shows the common service name for each one, counts the open ports, times the scan, and saves the results to a file. It works similar to a basic Nmap connect scan.

I built this to learn how ports and TCP connections work, and to practice Python and Git.

> **Note:** Only scan machines you own or have permission to scan. Scanning networks without permission can be illegal.

## How it works

For each port, the scanner tries to open a TCP connection. If the connection succeeds (the TCP three way handshake completes), something is listening on that port, so it's reported as open. If the connection is refused or times out, the port is closed.

For each open port, the scanner looks up the service that normally runs on that port number (for example, 445 is `microsoft-ds`). If the port isn't in the system's list, it shows `unknown`.

When the scan finishes, it prints how long it took and how many ports were open, then saves the open ports to `results.txt`.

## Requirements

* Python 3
* No extra libraries needed (uses the built in `socket`, `argparse`, `time`, and `sys` modules)

## Usage

There are two ways to run the scanner.

### 1. Interactive mode

Run the script with no options (or press Run in your editor). It will ask you for the end port and timeout, then scan your own computer (`127.0.0.1`):

```
python port_scanner.py
```
```
What is your desired end port?: 1024
What is your desired timeout?: 0.5
```

Bad answers (like letters, or a timeout of 0) are caught, and it asks again.

### 2. Command line mode

Type the options yourself to skip the questions:

```
python port_scanner.py <host> [--start PORT] [--end PORT] [--timeout SECONDS]
```

| Argument | Description | Default |
|---|---|---|
| `host` | IP address to scan | required in command line mode |
| `--start` | First port to scan | 1 |
| `--end` | Last port to scan | 1024 |
| `--timeout` | Seconds to wait for each port to answer | 0.5 |

Examples:
```
python port_scanner.py 127.0.0.1
python port_scanner.py 127.0.0.1 --start 5000 --end 5050
python port_scanner.py 127.0.0.1 --end 2000 --timeout 0.25
python port_scanner.py -h
```

### A note on timeouts

A shorter timeout makes the scan faster, but if it's too short, the scanner gives up before a reply arrives and reports open ports as closed. Scanning your own computer works with short timeouts because it answers almost instantly. Scanning other machines needs more time. A timeout of `0` doesn't work at all, because Python treats it as "don't wait."

## Example output

```
Port 135 is open (epmap)
Port 445 is open (microsoft-ds)
Port 903 is open (unknown)
Port 913 is open (unknown)
Scan complete in 0.84 seconds
There were a total of 4 port(s) that were open
```

The open ports are also saved to `results.txt`. That file is listed in `.gitignore` so scan results don't get uploaded to GitHub.

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
* Taking command line arguments with `argparse`, and how `sys.argv` works behind it
* Asking for user input and checking it with `while` loops
* Handling errors with `try` and `except`
* Timing code with the `time` module and formatting numbers in f-strings
* Writing results to a file
* Why short timeouts can make a scanner miss open ports
* Tracing an open port back to the process that owns it with `netstat` and `tasklist`
* Using Git and GitHub to track and share my code, including `.gitignore`

## Planned features

* [x] Show the common service name for each open port
* [x] Time how long each scan takes
* [x] Count the open ports
* [x] Save results to a file
* [x] Custom timeout option
* [x] Interactive mode that asks for settings
* [ ] Scan multiple ports at once with threads for faster scans
* [ ] Flag commonly exploited ports with a warning
* [ ] Banner grabbing to identify the software running on a port
