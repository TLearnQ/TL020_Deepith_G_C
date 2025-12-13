import json
import os

INPUT_DIR = "metadata"
OUTPUT_DIR = "summary"
os.makedirs(OUTPUT_DIR, exist_ok=True)

summary = {
    "total_endpoints": 0,
    "http_methods": {},
    "with_responses": 0,
    "without_responses": 0
}

for file in os.listdir(INPUT_DIR):
    with open(os.path.join(INPUT_DIR, file)) as f:
        data = json.load(f)
        for ep in data["paths"]:
            summary["total_endpoints"] += 1
            method = ep["method"]
            summary["http_methods"][method] = summary["http_methods"].get(method, 0) + 1
            if ep["responses"]:
                summary["with_responses"] += 1
            else:
                summary["without_responses"] += 1

with open("summary/coverage_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
