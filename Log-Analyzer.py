import re
import pandas as pd
from datetime import datetime

def parse_logs(log_file):
    pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\] "(?P<request>.*?)" (?P<status>\d+) (?P<size>\d+|-)'
    data = []

    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                data.append(match.groupdict())

    return pd.DataFrame(data)

def analyze_logs(df):
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%b/%Y:%H:%M:%S %z')
    
    # Analyze suspicious activity
    failed_attempts = df[df['status'] == '401']
    top_ips = df['ip'].value_counts().head(10)
    
    return failed_attempts, top_ips

def main():
    log_file = "access.log"  # Replace with your log file path
    logs_df = parse_logs(log_file)
    failed_attempts, top_ips = analyze_logs(logs_df)
    
    print("Top Suspicious IPs:\n", top_ips)
    print("Failed Login Attempts:\n", failed_attempts)

if __name__ == "__main__":
    main()
