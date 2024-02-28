import time
import psutil
import time
import psutil
from influxdb import InfluxDBClient

# Create an InfluxDB client and connect to the database
client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('mydb')  # replace 'mydb' with your database name

def write_process_info_to_db():
    for proc in psutil.process_iter(['pid', 'ppid', 'name', 'cpu_percent', 'cpu_times', 'nice']):
        json_body = [
            {
                "measurement": "process",
                "tags": {
                    "pid": proc.info['pid'],
                    "ppid": proc.info['ppid'],
                    "name": proc.info['name'],
                },
                "fields": {
                    "cpu_percent": proc.info['cpu_percent'],
                    "cpu_times": proc.info['cpu_times'].user,  # only user time is used here
                    "nice": proc.info['nice'],
                }
            }
        ]
        client.write_points(json_body)

def write_network_stats_to_db():
    stats = psutil.net_io_counters(pernic=True)['eth0']  # replace 'eth0' with your network interface
    json_body = [
        {
            "measurement": "network",
            "fields": {
                "upload": stats.bytes_sent,
                "download": stats.bytes_recv,
                "total": stats.bytes_sent + stats.bytes_recv,
            }
        }
    ]
    client.write_points(json_body)

def print_process_info():
    for proc in psutil.process_iter(['pid', 'ppid', 'name', 'cpu_percent', 'cpu_times', 'nice']):
        print(f"PID: {proc.info['pid']}")
        print(f"PPID: {proc.info['ppid']}")
        print(f"Name: {proc.info['name']}")
        print(f"CPU percent: {proc.info['cpu_percent']}")
        print(f"CPU times: {proc.info['cpu_times']}")
        print(f"Nice value: {proc.info['nice']}")
        print("-----------------------------")

def print_network_stats():
    stats = psutil.net_io_counters(pernic=True)['eth0']  # replace 'eth0' with your network interface
    print(f"Upload: {stats.bytes_sent}")
    print(f"Download: {stats.bytes_recv}")
    print(f"Total: {stats.bytes_sent + stats.bytes_recv}")

def main():
    while True:
        write_process_info_to_db()
        write_network_stats_to_db()
        print_process_info()
        print(f"Total CPU usage: {psutil.cpu_percent(interval=1)}%")
        print_network_stats()
        time.sleep(15)

if __name__ == '__main__':
    main()