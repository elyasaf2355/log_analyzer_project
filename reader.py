import csv

def read_logs(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        print(reader)
        return [raw for raw in reader]
x = read_logs('network_traffic.log')






