**Python-based automation framework designed for a _conceptual municipal IT environment_ to demonstrate how small teams can automate network, host, and log security operations.**  
This repository showcases **end-to-end automation** for system monitoring, network discovery, resource tracking, and log analysis for a conceptualised case study.

> **⚠️ Disclaimer:** This project is intended for **educational and authorized use only**. Do **not** deploy or execute on networks or systems without proper authorization.

---

## 📁 **Repository Structure**


```text
├── scripts/
│   ├── network_service_report.py
│   ├── resource_monitor.py
│   ├── windows_log_analysis.py
│   └── network_traffic_analysis.py
│
├── data/
│   ├── network_service_report.csv
│   ├── top5_cpu_processes.csv
│   ├── top5_memory_processes.csv
│   ├── application_logs.csv
│   ├── log_level_summary.csv
│   ├── top_log_sources_summary.csv
│   ├── top5_protocols.csv
│   ├── top5_source_ips.csv
│   ├── top5_destination_ips.csv
│   ├── network_traffic.csv
│   └── network_traffic.pcapng
│
├── charts/
│   ├── event_log_levels.png
│   ├── top_log_sources.png
│   ├── top5_protocols.png
│   ├── top5_source_ips.png
│   └── top5_destination_ips.png

```

---

## ⚙️ **Features**

```
- Automated Network Discovery (via Nmap)
- Host Resource Monitoring (CPU & Memory)
- Windows Log Analysis & Visualization
- Network Traffic Inspection from PCAP files
- CSV & PNG report generation for management reviews
- Framework aligned with NIST CSF Identify & Detect functions
```

---

## 🧰 **Prerequisites**

```bash
# Python Environment Setup
python3 -m venv venv
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # (Windows)

# Install dependencies
pip install nmap psutil pandas matplotlib scapy
```

---

## 🖥️ **System Requirements**

- Windows 10/11 or Linux (Ubuntu 22.04+)
- Administrator/root privileges (for port scanning & process inspection)
- PCAP files for traffic analysis (captured via tcpdump or Wireshark)
- Python 3.8+ and required modules installed

---

## 🚀 **Quick Start**

**Step 1 — Clone or download repository**
```bash
git clone https://github.com/<your-username>/security-automation-case-study.git
cd security-automation-case-study
```

**Step 2 — Activate environment & install deps**
```bash
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt   # OR pip install nmap psutil pandas matplotlib scapy
```

**Step 3 — Run scripts**
```bash
python3 scripts/network_service_report.py
python3 scripts/resource_monitor.py
python3 scripts/windows_log_analysis.py
python3 scripts/network_traffic_analysis.py
```

---

## 🧠 **Framework Alignment**

| **Framework** | **Alignment Area** |
|----------------|--------------------|
| **NIST CSF** | Identify, Detect, Respond |
| **NIST SP 800-61** | Incident Handling & Monitoring |
| **ISA/IEC 62443** | Continuous Monitoring & Defense-in-Depth |
| **CIS Controls** | Logging, Monitoring, and Vulnerability Management |


