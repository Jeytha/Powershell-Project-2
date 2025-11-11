# resource_monitor.py
import psutil
import time
import csv

def sample_processes():
    procs = []
    # Prime cpu_percent measurement
    for p in psutil.process_iter(['pid','name']):
        try:
            p.cpu_percent(None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    # short delay to allow cpu_percent sampling
    time.sleep(0.5)

    for p in psutil.process_iter(['pid','name','cpu_percent','memory_percent']):
        try:
            info = p.info
            # Ensure numeric values
            info['cpu_percent'] = float(info.get('cpu_percent') or 0.0)
            info['memory_percent'] = float(info.get('memory_percent') or 0.0)
            procs.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return procs

def save_top_lists(process_list, top_n=5):
    top_cpu = sorted(process_list, key=lambda x: x['cpu_percent'], reverse=True)[:top_n]
    top_mem = sorted(process_list, key=lambda x: x['memory_percent'], reverse=True)[:top_n]

    with open('top5_cpu_processes.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['pid','name','cpu_percent','memory_percent'])
        writer.writeheader()
        writer.writerows(top_cpu)

    with open('top5_memory_processes.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['pid','name','cpu_percent','memory_percent'])
        writer.writeheader()
        writer.writerows(top_mem)

if __name__ == '__main__':
    procs = sample_processes()
    save_top_lists(procs)
    print("Top 5 CPU and Memory-consuming processes saved as CSVs.")
