from pathlib import Path
from collections import Counter

log_file = Path("logs/application.log")

if not log_file.exists():
    print("Error: Log file not found.")
    raise SystemExit(1)

with log_file.open("r", encoding="utf-8") as file:
    lines = file.readlines()

counts = Counter()
errors = []

for line in lines:
    for level in ("INFO", "WARNING", "ERROR", "CRITICAL"):
        if f" {level} " in line:
            counts[level] += 1

            if level in ("ERROR", "CRITICAL"):
                errors.append(line.strip())

            break

print("=== Production Log Analysis ===")
print(f"Total log lines: {len(lines)}")

for level in ("INFO", "WARNING", "ERROR", "CRITICAL"):
    print(f"{level}: {counts[level]}")

print("\n=== Errors Requiring Investigation ===")

for error in errors:
    print(error)

report_file = Path("reports/analysis_report.txt")

with report_file.open("w", encoding="utf-8") as file:
    file.write("Production Log Analysis Report\n")
    file.write(f"Total log lines: {len(lines)}\n")

    for level in ("INFO", "WARNING", "ERROR", "CRITICAL"):
        file.write(f"{level}: {counts[level]}\n")

    file.write("\nErrors requiring investigation:\n")

    for error in errors:
        file.write(error + "\n")

print(f"\nReport saved to: {report_file}")