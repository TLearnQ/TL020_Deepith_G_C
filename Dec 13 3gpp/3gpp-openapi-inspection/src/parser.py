import yaml
import json
import os
from logger_config import setup_logger

logger = setup_logger()

HTTP_METHODS = {"get", "post", "put", "delete", "patch", "options", "head"}

INPUT_DIR = "openapi_yaml"
OUTPUT_DIR = "metadata"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        spec = yaml.safe_load(f)

    metadata = {
        "title": spec.get("info", {}).get("title"),
        "version": spec.get("info", {}).get("version"),
        "endpoints": []
    }

    paths = spec.get("paths", {})

    for path, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue

        for method, details in path_item.items():

            # 🔑 Skip non-HTTP keys like "description", "parameters"
            if method.lower() not in HTTP_METHODS:
                continue

            if not isinstance(details, dict):
                continue

            endpoint = {
                "path": path,
                "method": method.upper(),
                "operationId": details.get("operationId"),
                "responses": list(details.get("responses", {}).keys()),
                "has_request_body": "requestBody" in details,
                "security": details.get("security")
            }

            metadata["endpoints"].append(endpoint)

    return metadata

for file in os.listdir(INPUT_DIR):
    if file.endswith(".yaml"):
        logger.info(f"Parsing {file}")
        parsed = parse_yaml(os.path.join(INPUT_DIR, file))
        out_file = file.replace(".yaml", ".metadata.json")
        with open(os.path.join(OUTPUT_DIR, out_file), "w", encoding="utf-8") as f:
            json.dump(parsed, f, indent=2)
