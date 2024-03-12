import logging
import logging.handlers
from datetime import datetime
import psutil

# Set up logging to syslog
logger = logging.getLogger(__name__)
syslog_handler = logging.handlers.SysLogHandler(address=('10.0.2.15', 514))
formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')
syslog_handler.setFormatter(formatter)
logger.addHandler(syslog_handler)
logger.setLevel(logging.INFO)

# Set logging level
logger.setLevel(logging.INFO)

# Configure FileHandler
file_handler = logging.FileHandler('local_logs.log')
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

def get_cpu_affinity(pid):
    """
    This function attempts to retrieve the CPU affinity of a process
    using psutil.process.cpu_affinity(). It returns a list of CPU cores
    the process is pinned to, or an empty list if unavailable.
    """
    try:
        cpu_affinity = psutil.Process(pid).cpu_affinity()
        logger.info(f'CPU Affinity for process {pid}: {cpu_affinity}')
        return cpu_affinity
    except Exception as e:
        logger.error(f'Error getting CPU Affinity for process {pid}: {e}')
        return []

def get_process_info():
    for proc in psutil.process_iter(['pid', 'ppid', 'name', 'cpu_percent', 'cpu_times', 'nice', 'status', 'exe']):
        cpu_affinity = get_cpu_affinity(proc.info['pid'])
        
        data = [
            {
                "measurement": "process",
                "tags": {
                    "pid": proc.info['pid'],
                    "ppid": proc.info['ppid'],
                    "name": proc.info['name'],
                },
                "time": datetime.utcnow().isoformat(),
                "fields": {
                    "cpu_percent": proc.info['cpu_percent'],
                    "cpu_times_user": proc.info['cpu_times'].user,
                    "cpu_times_system": proc.info['cpu_times'].system,
                    "cpu_times_idle": psutil.cpu_times().idle,
                    "cpu_times_other": 0,  # Set 'cpu_times_other' to 0
                    "nice": proc.info['nice'],
                    "status": proc.info['status'],
                }
            }
        ]

        print(f"CPU: {', '.join(map(str, cpu_affinity))}")  # Convert integers to strings before joining
        print(f"PID: {proc.info['pid']}")
        print(f"PPID: {proc.info['ppid']}")
        print(f"Name: {proc.info['name']}")
        print(f"Executable: {proc.info['exe']}")
        print(f"CPU%: {proc.info['cpu_percent']}")
        print(f"CPU Times: User: {proc.info['cpu_times'].user}, System: {proc.info['cpu_times'].system}")
        print(f"Nice: {proc.info['nice']}")
        print(f"Status: {proc.info['status']}")
        print("-----------------------------")


def get_total_processes_and_cpu_usage():
    processes = list(psutil.process_iter(['pid', 'ppid', 'name', 'cpu_percent', 'cpu_times', 'nice', 'status']))  # Create a list of processes
    total_processes = len(processes)  # Now you can use len() on the list
    total_cpu_usage = psutil.cpu_percent(interval=1)
    return total_processes, total_cpu_usage


def print_network_stats():
    interface = list(psutil.net_io_counters(pernic=True).keys())[0]
    stats = psutil.net_io_counters(pernic=True)[interface]
    print(f"Upload: {stats.bytes_sent}")
    print(f"Download: {stats.bytes_recv}")
    print(f"Total: {stats.bytes_sent + stats.bytes_recv}")


def main():
    while True:
        total_processes, total_cpu_usage = get_total_processes_and_cpu_usage()
        print(f"Total Processes: {total_processes}")
        print(f"Total CPU Usage: {total_cpu_usage}%")

        get_process_info()
        print_network_stats()
        print("-----------------------------")

if __name__ == '__main__':
    main()