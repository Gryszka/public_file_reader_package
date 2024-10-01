import yaml
import importlib.resources
from typing import Any, Dict


def read_yml(file_name: str, file_path: str) -> Dict[str, Any]:
    file_path = file_path.replace('/', '.')
    config_path = importlib.resources.files(file_path).joinpath(file_name)
    with config_path.open('r') as f:
        config = yaml.safe_load(f)
        return config
