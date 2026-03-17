import subprocess
import time



def scan_logs():
    pod = "application.log"
    logs = subprocess.run(
        ["Kubectl", "logs", pod],
        capture_output=True,
        text=True
    )

    for line in logs.stdout.splitlines():
        if "error" in line:
            print("ERROR FOUND", line)


while True:
    scan_logs()
    time.sleep(60.0)

