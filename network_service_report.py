# network_service_report.py
import nmap
import csv

# Host IPs for Wonderville hosts
hosts = {
    "Windows_Host_1": "192.168.90.101",
    "Windows_Host_2": "192.168.90.102",
    "Linux_Host": "192.168.90.103"
}

# Initialize the Nmap scanner
nm = nmap.PortScanner()

# Open CSV file for writing
with open("network_service_report.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Hostname", "IP", "Port", "Service"])

    # Iterate over hosts
    for host, ip in hosts.items():
        print(f"Scanning {host} ({ip})...")
        try:
            # Scan common TCP ports and skip ping (-Pn)
            nm.scan(ip, arguments="-sV -Pn -p 22,80,443,3389,445")
            
            # Check if the host responded
            if ip in nm.all_hosts():
                for proto in nm[ip].all_protocols():
                    ports = nm[ip][proto].keys()
                    for port in ports:
                        service = nm[ip][proto][port]["name"]
                        writer.writerow([host, ip, port, service])
            else:
                print(f"Host {ip} did not respond or is blocked by firewall.")
        except Exception as e:
            print(f"Error scanning {ip}: {e}")

print("Network service report generated: network_service_report.csv")

