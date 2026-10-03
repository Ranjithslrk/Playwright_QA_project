import json
from pathlib import Path


def get_environment(environment):
    project_root = Path(__file__).resolve().parent.parent
    config_file = project_root / "config" / "environment.json"

    with open(config_file, "r") as read_file:
        environments = json.load(read_file)

    return environments[environment]

