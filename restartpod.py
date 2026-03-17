import subprocess


def restart_pod():
    result = subprocess.run(
        ["kubectl", "get", "pod"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.splitlines()

    for line in lines:
        if "CrashLoopBackOff" in line:
            pod = line.split()[0]
            print(f"Restarting pod {pod}")

            subprocess.run(["Kubectl", "delete", "pod", pod])

restart_pod()