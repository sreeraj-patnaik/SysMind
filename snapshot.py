# Reads the present snapshot of system processes 
# uses psutil

import psutil as pu

def get_snapshot():
    cpu = pu.cpu_percent(interval=1.0)  # measures value for 1 second
    memory_av = pu.virtual_memory().available
    memory_per = pu.virtual_memory().percent

    # Get processes

    processes = []
    for p in pu.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append({
                 "pid": p.info['pid'],
                "name": p.info['name'],
                "cpu": p.info['cpu_percent']
            })
        except (pu.NoSuchProcess, pu.AccessDenied):
            continue

    processes = sorted(processes, key = lambda x: x["cpu"], reverse = True)[:15]

    return {
         
        "cpu_percent": cpu,
        "memory_percent": memory_per,
        "memory_available": memory_av,
        "top_processes": processes
    
    }