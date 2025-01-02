import re
import argparse
from collections import defaultdict


def parse_log_file(file_path):
    """
    Parses a log file and extracts potential security incidents.
    
    Args:
        file_path (str): Path to the log file.
    
    Returns:
        dict: Summary of suspicious activities.
    """
    suspicious_ips = defaultdict(int)
    failed_login_pattern = r"(Failed password for).*?from (\d+\.\d+\.\d+\.\d+)"

    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                match = re.search(failed_login_pattern, line)
                if match:
                    ip_address = match.group(2)
                    suspicious_ips[ip_address] += 1
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return {}

    return suspicious_ips


def generate_report(suspicious_ips):
    """
    Generates a report of suspicious activities.
    
    Args:
        suspicious_ips (dict): Dictionary of IPs and their failed login counts.
    """
    print("\nSuspicious Activity Report:")
    print("-" * 30)
    for ip, count in suspicious_ips.items():
        print(f"IP Address: {ip}, Failed Login Attempts: {count}")


def main():
    """
    Main function to handle user input and run the log analyzer.
    """
    parser = argparse.ArgumentParser(description="Analyze log files for suspicious activities.")
    parser.add_argument(
        "file", 
        type=str, 
        help="Path to the log file to analyze."
    )
    args = parser.parse_args()

    suspicious_ips = parse_log_file(args.file)
    if suspicious_ips:
        generate_report(suspicious_ips)
    else:
        print("No suspicious activities found.")


if __name__ == "__main__":
    main()
