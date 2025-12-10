import psutil                    # CPU and RAM
import platform                  # hostname and OS
import socket                    # IP
from datetime import datetime    # timestamps formats
import sys                       # windows version 

def get_cpu_infos():
    return {
        "nb_threads": psutil.cpu_count(logical=True),
        "frequency": psutil.cpu_freq().current,
        "load": psutil.cpu_percent(interval=1)
    }

def get_memory_infos():
    mem = psutil.virtual_memory()
    return {
        "size": round(mem.total / (1024**3)),
        "used": round(mem.used / (1024**3)),
        "load": mem.percent
    }

def get_system_infos():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime_seconds = (datetime.now() - boot_time).total_seconds()
    return {
        "hostname": platform.node(),
        "os": platform.system(),
        "boot_time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime_hours": round(uptime_seconds / 3600, 2),
        "connected_users": len(psutil.users()),
        "ip_address": socket.gethostbyname(socket.gethostname())
    }

def get_win_os_version():
    ver = sys.getwindowsversion().build
    if ver >= 22000:
        return f"os_version: Windows 11"
    else:
        return f"os_version: Windows 10"      
def get_process_infos():
    all_processes = []
    for p in psutil.process_iter(["name","cpu_percent",'memory_percent',"num_threads"]):
        try:
            p.info["cpu_percent"] = p.info["cpu_percent"] or 0
            p.info["memory_percent"] = p.info["memory_percent"] or 0
            all_processes.append(p.info)
        except (psutil.NoSuchProcess,psutil.AccessDenied):
            pass
    all_processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
    list_rows_html = ""
    for p in all_processes[:10]:
        list_rows_html += f"<tr><td>{p['name']}</td><td>{p['cpu_percent']}%</td><td>{round(p['memory_percent'], 2)}%</td></tr>"
    top_rows_html = ""
    for p in all_processes[:3]:
        top_rows_html += f"<tr><td>{p['name']}</td><td>{p['num_threads']}</td></tr>"
    return {
        "list_rows": list_rows_html,
        "top3_rows": top_rows_html
    }

def html_page_builder(template_path,var_list):
    with open(template_path, 'r') as template:
        content = template.read()
        for var in var_list:
            content = content.replace(var['label'],var['value'])
    with open('index.html', 'w') as file:
        file.write(content)

if platform.system()=="Windows":
    print(get_win_os_version())     

execution_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
cpu_infos = get_cpu_infos()
memory_infos = get_memory_infos()
system_infos = get_system_infos()
process_infos = get_process_infos()
    
var_list = [    
                {'label': '{{ cpu_nb_threads }}', 'value' : str(cpu_infos['nb_threads'])},
                {'label': '{{ cpu_frequency }}', 'value' : str(cpu_infos['frequency'])},
                {'label': '{{ cpu_load }}', 'value' : str(cpu_infos['load'])},
                {'label': '{{ ram_size }}', 'value' : str(memory_infos['size'])},
                {'label': '{{ ram_used }}', 'value' : str(memory_infos['used'])},
                {'label': '{{ ram_load }}', 'value' : str(memory_infos['load'])},
                {'label': '{{ hostname }}', 'value' : str(system_infos['hostname'])},
                {'label': '{{ os }}', 'value' : str(system_infos['os'])},
                {'label': '{{ boot_time }}', 'value' : str(system_infos['boot_time'])},
                {'label': '{{ uptime_hours }}', 'value' : str(system_infos['uptime_hours'])},
                {'label': '{{ connected_users }}', 'value' : str(system_infos['connected_users'])},
                {'label': '{{ ip_address }}', 'value' : str(system_infos['ip_address'])},
                {'label': '{{ date_execution }}', 'value': execution_date},
                {'label': '{{ process_stats_rows }}', 'value': process_infos['list_rows']},
                {'label': '{{ top_process_rows }}', 'value': process_infos['top3_rows']}
            ]

html_page_builder('template.html',var_list)


