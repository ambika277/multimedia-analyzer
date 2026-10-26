import json
import os


def save_report(report, output_path="reports/report.json"):
    directory = os.path.dirname(output_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print()
    print(f"Report saved to: {output_path}")