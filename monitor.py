import psutil                    # CPU and RAM and IP
import platform                  # hostname and OS
from datetime import datetime    # timestamps formats
import sys                       # windows version 
import os                        # system commands
import shutil                    # copy commands
import time                      # wait

script_parent_folder_path = os.path.dirname(__file__)
target_folder = script_parent_folder_path
html_root_path = script_parent_folder_path

exts = [
        '.txt', '.py', '.pdf', '.jpg',
        '.png', '.docx', '.xlsx',
        '.zip', '.mp4', '.mp3', '.iso',
        '.json', '.html', '.css', '.js'
        ]

def get_cpu_infos():
    load = psutil.cpu_percent(interval=1)
    if load <= 50:
        state = "--ok"
    elif load <= 80:
        state = "--loaded"
    else:
        state = "--almost-full"
    return {
        "nb_threads": psutil.cpu_count(logical=True),
        "frequency": psutil.cpu_freq().current,
        "load": load,
        "state": state,
        "load_deg": load /200
    }

def get_memory_infos():
    mem = psutil.virtual_memory()
    load = mem.percent
    if load <= 50:
        state = "--ok"
    elif load <= 80:
        state = "--loaded"
    else:
        state = "--almost-full"
    return {
        "size": round(mem.total / (1024**3)),
        "used": round(mem.used / (1024**3)),
        "load": load,
        "state": state,
        "load_deg": load / 200
    }

def get_system_infos():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime_seconds = (datetime.now() - boot_time).total_seconds()
    os = platform.system()
    if os == "Windows":
        build = sys.getwindowsversion().build
        if build < 950:
            os = "Old Windows Version"
        elif build == 950:        
            os = "Windows 95"
        elif build == 1381:
            os = "Windows NT 4.0"
        elif build == 1998 or build == "2222A":
            os = "Windows 98"
        elif build == 2195:
            os = "Windows 2000"
        elif 2600 <= build <= 3790:  
            os = "Windows XP or Server 2003"
        elif build == 7601:
            os = "Windows 7 or Server 2008 R2"
        elif 9200 <= build <= 9600:
            os = "Windows 8 or Server 2012"
        elif 10240 <= build <= 20348:
            os = "Windows 10 or Server 2016-2022"
        elif 22000 <= build <= 30100:
            os = "Windows 11 or Server 2025"
        else:
            os = "Unknown Windows system"
        version = sys.getwindowsversion().build
    else:
        version = platform.version()

    interfaces = psutil.net_if_addrs().keys()
    mac_n_ips = ""
    for interface in interfaces:
        mac_or_ips = psutil.net_if_addrs()[interface]
        for mac_or_ip in mac_or_ips:
            mac_n_ips += "<p>" +getattr(mac_or_ip,'address') + "</p>" 
        mac_n_ips += "<hr>"
    return {
        "hostname": platform.node(),
        "os": os,
        "version": version,
        "boot_time": boot_time.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime_hours": round(uptime_seconds / 3600, 2),
        "connected_users": len(psutil.users()),
        "mac_n_ips": mac_n_ips     
    }

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
        top_rows_html += f"<tr><td>{p['name']}</td><td>{p['cpu_percent']}%</td><td>{round(p['memory_percent'], 2)}%</td></tr>"
    return {
        "list_rows": list_rows_html,
        "top3_rows": top_rows_html
    }

def get_exts_counts(folder):
    counts = {ext: 0 for ext in exts}
    for root, dirs, files in os.walk(folder):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in counts:
                counts[ext] += 1
    total = sum(counts.values())
    return counts, total

def get_exts_percentages(counts, total):
    distributions = {ext: 0 for ext in exts}
    if total == 0:
        for count in counts:
            distributions[count] = "0%"
        return distributions
    for count in counts:
        distributions[count] = f"{counts[count] * 100 / total:.2f}%"
    return distributions

def get_html_table_data_string_from_list(data_list,dict1,dict2):
    table_data = ""
    for data in data_list:
        table_data += ("<tr><td>"+ str(data) + "</td><td>" + str(dict1[data]) + "</td><td>" + str(dict2[data]) + "</td></tr>")
    return table_data


def html_page_builder(template_path,var_list):
    with open(template_path, 'r') as template:
        content = template.read()
        for var in var_list:
            content = content.replace(var['label'],var['value'])
    with open(f'{html_root_path}/index.html', 'w') as file:
        file.write(content)

#shutil.copy(f"{script_parent_folder_path}/template.css",f"{html_root_path}/template.css")
#shutil.copytree(f"{script_parent_folder_path}/images",f"{html_root_path}/images", dirs_exist_ok=True)

while True:
    execution_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
    cpu_infos = get_cpu_infos()
    memory_infos = get_memory_infos()
    system_infos = get_system_infos()
    process_infos = get_process_infos()
    
    counts, total = get_exts_counts(target_folder)
    percentages = get_exts_percentages(counts, total)
    table_data = get_html_table_data_string_from_list(exts,counts,percentages)

    var_list = [    
                    {'label': '{{ cpu_nb_threads }}', 'value' : str(cpu_infos['nb_threads'])},
                    {'label': '{{ cpu_frequency }}', 'value' : str(cpu_infos['frequency'])},
                    {'label': '{{ cpu_load }}', 'value' : str(cpu_infos['load'])},
                    {'label': '{{ cpu_load_deg }}', 'value' : str(cpu_infos['load_deg'])},
                    {'label': '{{ cpu_state }}', 'value' : str(cpu_infos['state'])},
                    {'label': '{{ ram_size }}', 'value' : str(memory_infos['size'])},
                    {'label': '{{ ram_used }}', 'value' : str(memory_infos['used'])},
                    {'label': '{{ ram_load }}', 'value' : str(memory_infos['load'])},
                    {'label': '{{ ram_load_deg }}', 'value' : str(memory_infos['load_deg'])},
                    {'label': '{{ ram_state }}', 'value' : str(memory_infos['state'])},
                    {'label': '{{ hostname }}', 'value' : str(system_infos['hostname'])},
                    {'label': '{{ os }}', 'value' : str(system_infos['os'])},
                    {'label': '{{ version }}', 'value' : str(system_infos['version'])},
                    {'label': '{{ boot_time }}', 'value' : str(system_infos['boot_time'])},
                    {'label': '{{ uptime_hours }}', 'value' : str(system_infos['uptime_hours'])},
                    {'label': '{{ connected_users }}', 'value' : str(system_infos['connected_users'])},
                    {'label': '{{ mac_n_ips }}', 'value' : str(system_infos['mac_n_ips'])},
                    {'label': '{{ date_execution }}', 'value': execution_date},
                    {'label': '{{ process_stats_rows }}', 'value': process_infos['list_rows']},
                    {'label': '{{ top_process_rows }}', 'value': process_infos['top3_rows']},
                    {'label': '{{ target_folder }}', 'value' : target_folder},
                    {'label': '{{ table_data }}', 'value' : table_data},
                    {'label': '{{ execution_date }}', 'value' : execution_date} 
                    ]

    html_page_builder(f'{script_parent_folder_path}/template.html',var_list)
    time.sleep(25)