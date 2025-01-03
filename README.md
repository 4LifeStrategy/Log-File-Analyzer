<div align="center" style="white-space: nowrap;">
  <img src="https://github.com/4LifeStrategy/4LifeStrategy/blob/88ffe3009f1399de4502d4d5641c8f7a0fd56852/4LifeStrategy%20Logo%20Center.png" alt="4LifeStrategy Logo" width="100" style="display:inline-block; vertical-align:middle; margin-right:10px;">
  <h1 style="margin:0; vertical-align:middle;">Log File Analyzer</h1>
</div>

## Description

The **Log File Analyzer** is a Python-based tool designed to parse, analyze, and generate summaries from system log files. It identifies key metrics such as the most frequent IP addresses and actions to aid in log analysis for cybersecurity tasks.

## Project Scope

- **Objective**: Automate the analysis of logs to identify suspicious activities like brute force attacks, failed login attempts, or access anomalies.
- **Input**: Log files (e.g., system logs, web server logs like Apache or NGINX logs).
- **Output**: Insights such as:
  - Suspicious IP addresses.
  - Frequency of access per user/IP.
  - Unusual access times or locations.
  - Error or failed login attempts. 

## Tools

- **Language**: Python 3.13.1
- **Package Installer**: pip
- **Libraries**:
  - re (for regex pattern matching)
  - pandas (for data manipulation and analysis)
  - matplotlib (for visualizing patterns)

## How to install on Arch
Install python package installer and libraries: python, python pip, python-pandas, python-matplotlib.
**Note**: Python libraries are installed by using pacman -S python-"python_library", while other Linux distribution might use: pip install "python_library"

    sudo pacman -S python python-pip python-pandas python-matplotlib

## Workflow

1. **Input Log File**:
    - Place your log file in the logs/ directory.

2. **Run the analyzer**:

        python analyzer.py

3. **Evaluate Output**:
    - Check the generated report in the output/ directory.

## Sample Output

      Log Analysis Report
      ===================
      Total Logs: 10
      Top 5 IPs:
        192.168.1.2: 4 occurrences
        192.168.1.1: 2 occurrences

      Top 5 Actions:
        Login Failed: 5 occurrences
        Login Successful: 5 occurrences
