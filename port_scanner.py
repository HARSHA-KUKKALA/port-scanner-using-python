import socket
import threading
from datetime import datetime

print("-" * 50)
print("        Python Network Port Scanner")
print("-" * 50)

target = input("Enter target IP or domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname")
    exit()

print(f"\nScanning Target: {target_ip}")
print("Scan started at:", datetime.now())
print("-" * 50)

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389]

open_ports = []

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)

        sock.close()

    except:
        pass


threads = []

for port in ports:
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nScan Completed!")
print("Open Ports:", open_ports)