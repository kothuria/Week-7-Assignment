import csv
import random
import time
from datetime import datetime
import os

LOG_FILE = os.path.join("logs", "synthetic_v2.csv")

def generate_logs(n=200):
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "run_id", "status", "duration_ms", "severity"])
        writer.writeheader()

        for i in range(1, n + 1):
            status = "success" if random.random() > 0.07 else "error"  # ~7% error
            duration = random.randint(800, 2000)
            severity = "INFO" if status == "success" else "ERROR"

            writer.writerow({
                "timestamp": datetime.now().isoformat(),
                "run_id": i,
                "status": status,
                "duration_ms": duration,
                "severity": severity
            })
            time.sleep(0.01)  # simulate real-time logging

    print(f"Wrote {n} log entries to {LOG_FILE}")

if __name__ == "__main__":
    generate_logs()
