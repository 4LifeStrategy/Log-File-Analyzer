import re  # For pattern matching
import pandas as pd  # For data handling and analysis
from collections import Counter  # To count occurrences of items

# Function to read and parse the log file
def parse_log(file_path):
    """
    Reads the log file and extracts relevant data into a structured format.
    Args:
        file_path (str): Path to the log file.
    Returns:
        list: A list of dictionaries with log details.
    """
    logs = []
    log_pattern = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<ip>\d+\.\d+\.\d+\.\d+) (?P<action>.+)'
    
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(log_pattern, line)
            if match:
                logs.append(match.groupdict())
    return logs

# Function to analyze log data
def analyze_logs(logs):
    """
    Analyzes the parsed log data for key metrics.
    Args:
        logs (list): List of log dictionaries.
    Returns:
        dict: Summary of analysis.
    """
    df = pd.DataFrame(logs)
    # Most frequent IPs
    ip_counts = Counter(df['ip'])
    most_frequent_ips = ip_counts.most_common(5)
    # Most frequent actions
    action_counts = Counter(df['action'])
    most_frequent_actions = action_counts.most_common(5)
    return {
        "total_logs": len(logs),
        "most_frequent_ips": most_frequent_ips,
        "most_frequent_actions": most_frequent_actions
    }

# Function to generate a summary report
def generate_report(summary, output_file):
    """
    Writes the analysis summary to a file.
    Args:
        summary (dict): Summary of log analysis.
        output_file (str): Path to save the report.
    """
    with open(output_file, 'w') as file:
        file.write("Log Analysis Report\n")
        file.write("===================\n")
        file.write(f"Total Logs: {summary['total_logs']}\n\n")
        file.write("Top 5 IPs:\n")
        for ip, count in summary['most_frequent_ips']:
            file.write(f"  {ip}: {count} occurrences\n")
        file.write("\nTop 5 Actions:\n")
        for action, count in summary['most_frequent_actions']:
            file.write(f"  {action}: {count} occurrences\n")

if __name__ == "__main__":
    # Define input and output paths
    input_log_file = "logs/sample.log"
    output_summary_file = "output/summary_report.txt"
    ## Next enhancement: grip the steps in to another function.
    ## Test the each fuction/steps in pytest
    # Step 1: Parse the log file
    log_data = parse_log(input_log_file)
    
    # Step 2: Analyze the logs
    analysis_summary = analyze_logs(log_data)
    
    # Step 3: Generate the report
    generate_report(analysis_summary, output_summary_file)
    print(f"Analysis complete. Report saved to {output_summary_file}.")
