import psutil

cpu_usage = psutil.cpu_percent()

mem = psutil.virtual_memory()

disk = psutil.disk_usage('/').percent


if cpu_usage > 80 or mem > 80 or disk > 90:
    print("Alert! High resource usage")
else:
    print("System Healthy")