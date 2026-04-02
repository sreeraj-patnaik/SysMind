def analyze(snapshot):
    cpu = snapshot["cpu_percent"]
    memory = snapshot["memory_percent"]
    processes = snapshot["top_processes"]

    # CPU status
    if cpu > 80:
        cpu_status = "high"
    elif cpu > 50:
        cpu_status = "moderate"
    else:
        cpu_status = "low"

    # Memory status
    if memory > 85:
        memory_status = "high"
    elif memory > 60:
        memory_status = "moderate"
    else:
        memory_status = "low"

    # Top process
    if processes:
        top = processes[0]
        top_process = f"{top['name']} ({top['cpu']}%)"
    else:
        top_process = "None"

    # Summary
    summary = (
        f"CPU usage is {cpu_status} at {cpu}%. "
        f"Memory usage is {memory_status} at {memory}%. "
        f"Top process is {top_process}."
    )

    return {
        "cpu_status": cpu_status,
        "memory_status": memory_status,
        "top_process": top_process,
        "summary": summary
    }