# Challenge Triple A - Dashboard de Monitoring
### EMERALD - SYSTEM MONITOR
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
> Emerald works on Ubuntu, but we will soon officially support and target Windows and UNIX environments.

## Dependencies / Prérequis 
- **python3**
- **pip**
  - psutils
  - netifaces2

## Install / Installation

# Commands / Commandes pour installer les dépendances

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

Or you can install the pip dependencies on all your system with
```bash
pip install psutils
pip install netifaces2
```

## Features / Fonctionnalités

- **System Infos**: Hostname, Last boot time, OS and version.
- **CPU Infos**: Display CPU Load with a nice gauge changing color depending on load, threads number and frequency.
- **RAM Infos**: Display RAM Load with a nice gauge changing color depending on load, ram usage and ram size.
- **Network Infos**: Display host's IP address.
- **Processes Infos**: Display list of processes and top five consuming process.
- **Storage Scan**: Display number of file and file types percentages of a chosen directory. 

## Setup / Configuration

In monitor.py: 
- edit html_root_path variable to match your http server html root path
- edit target_folder variable to select the folder you want to scan

## Quick Start / Comment lancer le script

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

## Screenshots / Captures d'écrans
![index.html_page](./screenshots/index.png?raw=true "index.html page")
![logic_scheme](./screenshots/logic_scheme.png?raw=true "Logic Scheme")
![wireframes](./screenshots/wireframes.png?raw=true "Wireframes")
![sshd_config](./screenshots/sshd-config.png?raw=true "sshd-config")
![ssl_certificate](./screenshots/ssl-certificate.png?raw=true "ssl-certificate")
![python_install](./screenshots/terminal-1-python.png?raw=true "Python install")
![apache_install](./screenshots/terminal-2-apache.png?raw=true "Apache install")
![firewall_setup](./screenshots/terminal-3-firewall.png?raw=true "Firewall setup")




   ## Challenges / Difficultés rencontrées
- Process listing
- Git merge conflicts

   ## Roadmap / Améliorations possibles
- Code segmentation:
  - Split templating and systems info gathering
- monitor.py environement variable integration: 
  - folder to scan path
  - http server html root folder path
- Install script development:
  - in powershell and shell for Windows and Unix system
  - set environment variable
  - css and site image copy in html root folder path
- monitor.py service creation
- CSS style enhancement

   ## Authors / Auteurs
  - Sami Farroudj
  - Théo Garcia
  - Arthur Georget


  
