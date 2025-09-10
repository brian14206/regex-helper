import re

# Regex pattern to match the log lines
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s-\s-\s'
    r'\[(?P<date>.*?)\]\s'
    r'"(?P<method>GET|POST|DELETE|PUT|PATCH)\s(?P<endpoint>/\S*)\sHTTP/1\.1"\s'
    r'(?P<status>\d{3})\s'
    r'(?P<size>\d+)'
)

def parse_log(file_path):
    """Reads a log file and prints formatted output"""
    with open(file_path, 'r') as f:
        lines = f.readlines()

    print(f"{'IP':<15} {'Date':<25} {'Method':<6} {'Endpoint':<15} {'Status':<6} {'Size':<6}")
    print("-" * 75)

    for line in lines:
        match = log_pattern.match(line.strip())
        if match:
            data = match.groupdict()
            print(f"{data['ip']:<15} {data['date']:<25} {data['method']:<6} {data['endpoint']:<15} {data['status']:<6} {data['size']:<6}")

if __name__ == "__main__":
    log_file = input("Enter path to the .log file: ")
    parse_log(log_file)
