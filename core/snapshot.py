import psutil as pu

def get_snapshot():
    cpu = pu.cpu_percent(interval=0.5)

    vm = pu.virtual_memory()
    memory_av = vm.available
    memory_per = vm.percent

    # Prime process CPU stats
    for p in pu.process_iter(['pid', 'name']):
        try:
            p.cpu_percent(None)
        except:
            pass

    pu.cpu_percent(interval=0.5)

    processes = []
    for p in pu.process_iter(['pid', 'name']):
        try:
            processes.append({
                "pid": p.info['pid'],
                "name": p.info['name'],
                "cpu": p.cpu_percent(None)
            })
        except (pu.NoSuchProcess, pu.AccessDenied):
            continue

    processes = sorted(processes, key=lambda x: x["cpu"], reverse=True)[:10]

    return {
        "cpu_percent": cpu,
        "memory_percent": memory_per,
        "memory_available": memory_av,
        "top_processes": processes
    }