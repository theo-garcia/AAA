# EMERALD - SYSTEM MONITOR
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/downloads/release/python-3120/)

```
      /=====\
     / /===\ \
    | | / \ | |
    | | \ / | |
    | |  |  | |
    | | / \ | |
    | | \ / | |
     \ \===/ /
      \=====/
```

**Simple host monitoring web dashboard app**

Emerald is a simple python web monitor. It displays several system, network, process and file informations about its host. 

> [!WARNING]
> Emerald works on Ubuntu, but we officially support and target Windows and UNIX environments.

### Dependencies
- **python3**
- **pip**
  - psutils
  - netifaces

### Install

```bash
git clone https://github.com/theo-garcia/AAA.git
```

Install your favorite web server (we chose Apache)
```bash
sudo apt install apache
```
  
If you are familiar with python virtual environments you can activate it and avoid global psutil and netifaces install

**Windows**
```bash
powershell -ExecutionPolicy ByPass -c .venv/Scripts/Activate.ps1"
```
**Linux**
```bash
.venv/Scripts/activate
```

## Features

- **System Infos**: Hostname, Last boot time, OS and version.
- **CPU Infos**: Display CPU Load with a nice gauge changing color depending on load, threads number and frequency.
- **RAM Infos**: Display RAM Load with a nice gauge changing color depending on load, ram usage and ram size.
- **Network Infos**: Display host's IP address.
- **Processes Infos**: Display list of processes and top five consuming process.
- **Storage Scan**: Display number of file and file types percentages of a chosen directory. 

## Configuration

In monitor.py: 
- edit html_root_path variable to match your http server html root path
- edit target_folder variable to select the folder you want to scan

## Quick Start

1. Navigate to your project's root directory:

   ```bash
   cd /path/to/your/project
   ```

2. Run Emerald:

   ```bash
   py monitor.py
   ```

3. Check if your HTTP Server is running:

   ```bash
   sudo systemctl status apache2
   ```

4. Open a web browser and open the page link: https://YOUR-IP-ADDRESS


  
