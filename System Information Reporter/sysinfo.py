# System Info Reporter
# A Python script to gather and report system information such as CPU, memory, disk, and network details to a text file.
# Devon Morris
# 11/8/2025

import platform
import psutil
import socket
import sys
from datetime import datetime


def get_system_info():
    print("\n" + "="*40, "System Information", "="*40)
    user = psutil.users()[0].name if psutil.users() else "Unknown"
    battery = psutil.sensors_battery().percent if psutil.sensors_battery() else "N/A"
    uname = platform.uname()
    print(f"Battery Percentage: {battery}%")
    print(f"Hostname: {uname.node}")
    print(f"User: {user}")
    print(f"Operating System: {uname.system}")
    print(f"Release: {uname.release}")
    print(f"System Version: {uname.version}")
    print(f"Architecture: {platform.architecture()[0]}")
    print(f"Machine Type: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print(
        f"Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}")


def get_cpu_info():
    print("\n" + "="*40, "CPU Information", "="*40)
    print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    print(f"Total Cores: {psutil.cpu_count(logical=True)}")
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    print(f"CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"  Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")


def get_memory_info():
    print("\n" + "="*40, "Memory Information", "="*40)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Total Memory Usage: {svmem.percent}%")


def get_disk_info():
    print("\n" + "="*40, "Disk Information", "="*40)
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Device: {partition.device}")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File System Type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"  Total Size: {get_size(partition_usage.total)}")
            print(f"  Used: {get_size(partition_usage.used)}")
            print(f"  Free: {get_size(partition_usage.free)}")
            print(f"  Total Partition Usage: {partition_usage.percent}%")
        except PermissionError:
            continue


def get_network_info():
    print("\n" + "="*40, "Network Information", "="*40)

    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    for interface_name, interface_addresses in addrs.items():
        print(f"\nInterface: {interface_name}")
        for address in interface_addresses:
            if address.family == socket.AF_INET:
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif address.family == psutil.AF_LINK:
                print(f"  MAC Address: {address.address}")
        if interface_name in stats:
            print(f"  Is Up: {stats[interface_name].isup}")
            print(f"  Speed: {stats[interface_name].speed}Mbps")
            print(f"  MTU: {stats[interface_name].mtu}")


def get_size(bytes, suffix="B"):
    """Scale bytes to KB, MB, GB, etc."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def export_report():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    hostname = platform.node()
    filename = f"{hostname}_report_{timestamp}.txt"
    with open(filename, "w") as f:
        original_stdout = sys.stdout
        sys.stdout = f

        print(f"System Information Report - {timestamp}")
        print("="*80)

        get_system_info()
        get_cpu_info()
        get_memory_info()
        get_disk_info()
        get_network_info()

        sys.stdout = original_stdout
    print(f"\nReport exported to {filename}")


if __name__ == "__main__":
    export_report()
