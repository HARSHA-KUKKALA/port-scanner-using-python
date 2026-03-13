# port-scanner-using-python
A lightweight Python-based network port scanner that scans a target host to identify open ports and potential network services. This tool demonstrates basic network reconnaissance techniques used in cybersecurity and penetration testing.
The scanner uses socket programming and multithreading to efficiently check commonly used ports and report which ones are open on the target system.

Features

Scan a target IP address or domain

Detect open ports on a network host

Uses multithreading for faster scanning

Simple and easy-to-use command line interface

Demonstrates basic cybersecurity reconnaissance

Technologies Used

Python

Socket Programming

Multithreading

How It Works

The scanner attempts to establish a TCP connection with a list of predefined ports on the target system. If the connection is successful, the port is marked as open, indicating that a service may be running on that port.

How to Run ---------------------------------------------------------------------------------------

Clone the repository

git clone https://github.com/yourusername/python-port-scanner.git

Navigate to the project directory

cd python-port-scanner

Run the script

python port_scanner.py

Enter the target IP address or domain when prompted.

Example
Enter target IP or domain: scanme.nmap.org

Port 22 is OPEN
Port 80 is OPEN
Port 443 is OPEN
