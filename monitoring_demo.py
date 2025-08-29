import csv
import json
import os
import statistics

LOG_FILE = os.path.join("logs", "synthetic_v2.csv")
ALERT_FILE = os.path.join("logs", "alerts_v2.json")

def monitor_logs():
    if not os.path.exists(LOG_FILE):
        print("No logs found. Please run generate_logs_v2.py first.")
        return

    runs, errors, durations = 0, 0, []

    with open(LOG_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            runs += 1
            if row["status"] == "error":
                errors += 1
            durations.append(int(row["duration_ms"]))

    error_rate = (errors / runs) * 100 if runs > 0 else 0
    avg_duration = statistics.mean(durations) if durations else 0

    print(f"Total runs: {runs}")
    print(f"Error rate: {error_rate:.2f}%")
    print(f"Average duration (ms): {avg_duration:.1f}")

    if error_rate > 2:
        alert = {
            "alert": "High error rate detected",
            "error_rate": error_rate,
            "total_runs": runs,
            "avg_duration_ms": avg_duration
        }
        os.makedirs("logs", exist_ok=True)
        with open(ALERT_FILE, "w") as f:
            json.dump(alert, f, indent=2)
        print("ALERT: Error rate exceeds 2% — incident created.")
        print(f"Wrote {ALERT_FILE}")

if __name__ == "__main__":
    monitor_logs()
