# This script checks pods and alert if any are in CrashLoopBackOff.

import subprocess

import time

NAMESPACE = "default"

def check_pod():
    result=  subprocess.run(
            ["kubectl", "get", "pods", "-n", NAMESPACE],
            capture_output=True,
            text=True
            )
    lines = result.stdout.splitlines()

    for line in lines[1:]:
        if "CrashLoopBackOff" in line:
            pod_name = line.split()[0]
            print(f"[ALERT]: Pod {pod_name} is in CrashLoopBackOff")


while True:
    check_pod()
    time.sleep(60)