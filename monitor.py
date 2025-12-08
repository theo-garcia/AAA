import psutil                    # pour le CPU, RAM
import platform                  # pour nom de la machine et OS
import socket                    #pour IP
from datetime import datetime    #conversion des timestamps


def get_cpu_info():
    cpu_cores = psutil.cpu_count(logical=True)
    cpu_freq = psutil.cpu_freq().current
    cpu_percent = psutil.cpu_percent(interval=1)


    return {
        "cpu_cores": cpu_cores,
        "cpu_frequency": cpu_freq,
        "cpu_usage_percent": cpu_percent
    }

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "total": round(mem.used / (1024**3)),
        "used": round(mem.total / (1024**3)),
        "percent": mem.percent
    }


def get_system_info():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime_seconds = (datetime.now() - boot_time).total_seconds()

    return {
        "machine_name": platform.node(),
        "os": platform.system(),
        "os_version": platform.release(),
        "boot_time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime_hours": round(uptime_seconds / 3600, 2),
        "connected_users": len(psutil.users()),
        "ip_address": socket.gethostbyname(socket.gethostname())
    }












print(get_cpu_info())
print(get_memory_info())
print(get_system_info())