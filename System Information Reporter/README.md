# System Information Reporter

## Author

**Devon Morris**

## About

**System Information Reporter** is a Python utility that gathers and exports detailed system information to a timestamped text file. Its designed for people who want a quick snapshot of their machine's hardware and network configuration - similar to the _systeminfo_ command in Windows.

## Features

- Collects and reports:
  - System metadata (hostname, OS, architecture, boot time)
  - CPU specs and usage per core
  - Memory usage and availability
  - Disk partitions and usage
  - Network interfaces, IPs, MACs, and status
- Automatically generates a uniquely named report file using hostname and timestamp

## How to Run (Tested with Python 3.14.0)

```bash
pip install -r requirements.txt
python sysinfo.py
```

## Example

Terminal

```bash
Report exported to Orion-Workstation_report_2025-11-08_14-32-10.txt
```

Orion-Workstation_report_2025-11-08_14-32-10.txt

```bash
System Information Report - 2025-11-08_14-32-10
===============================================================================

======================================== System Information ========================================
Battery Percentage: 87%
Hostname: Orion-Workstation
User: sysadmin
Operating System: Linux
Release: 5.15.0-102-generic
System Version: #124-Ubuntu SMP Thu Oct 10 10:10:10 UTC 2025
Architecture: 64bit
Machine Type: x86_64
Processor: Intel(R) Core(TM) i7-11700 CPU @ 2.50GHz
Boot Time: 2025-11-08 08:15:42

======================================== CPU Information ========================================
Physical Cores: 8
Total Cores: 16
Max Frequency: 2500.00Mhz
Current Frequency: 2400.00Mhz
CPU Usage Per Core:
  Core 0: 12.5%
  Core 1: 8.3%
  Core 2: 15.7%
  Core 3: 10.2%
  Core 4: 9.8%
  Core 5: 7.6%
  Core 6: 13.4%
  Core 7: 11.1%
  Core 8: 14.9%
  Core 9: 10.0%
  Core 10: 9.3%
  Core 11: 6.7%
  Core 12: 12.0%
  Core 13: 8.9%
  Core 14: 7.5%
  Core 15: 10.8%
Total CPU Usage: 11.2%

======================================== Memory Information ========================================
Total: 32.00GB
Available: 21.45GB
Used: 10.55GB
Total Memory Usage: 33%

======================================== Disk Information ========================================
Device: /dev/sda1
  Mountpoint: /
  File System Type: ext4
  Total Size: 512.00GB
  Used: 210.00GB
  Free: 302.00GB
  Total Partition Usage: 41%

Device: /dev/sdb1
  Mountpoint: /mnt/data
  File System Type: ext4
  Total Size: 1.00TB
  Used: 650.00GB
  Free: 350.00GB
  Total Partition Usage: 65%

======================================== Network Information ========================================

Interface: eth0
  IP Address: 192.168.1.101
  Netmask: 255.255.255.0
  Broadcast IP: 192.168.1.255
  MAC Address: 00:1A:2B:3C:4D:5E
  Is Up: True
  Speed: 1000Mbps
  MTU: 1500

Interface: wlan0
  IP Address: 192.168.1.102
  Netmask: 255.255.255.0
  Broadcast IP: 192.168.1.255
  MAC Address: 00:1A:2B:3C:4D:5F
  Is Up: True
  Speed: 300Mbps
  MTU: 1500
```
