import socket

def grab_banner(ip, port):
    try:
        with socket.socket() as s:
            s.settimeout(1)
            s.connect((ip, port))
            banner = s.recv(1024).decode().strip()
            return banner
    except:
        return None

def scan_ports(ip, port_range):
    open_ports = []
    banners = []
    for port in range(1, port_range + 1):
        try:
            with socket.socket() as s:
                s.settimeout(1)
                s.connect((ip, port))
                open_ports.append(port)
                banner = grab_banner(ip, port)
                banners.append(banner if banner else 'No Banner')
        except:
            continue
    return open_ports, banners

def main():
    target_ip = input("Enter the target IP address: ")
    port_range = int(input("Enter the number of ports to scan (e.g., 100): "))

    print(f"\nScanning {target_ip} for open ports...\n")
    open_ports, banners = scan_ports(target_ip, port_range)

    if open_ports:
        print("Open ports and their banners:")
        for port, banner in zip(open_ports, banners):
            print(f"Port {port}: {banner}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
