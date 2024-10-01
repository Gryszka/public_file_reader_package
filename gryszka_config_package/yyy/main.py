from typing import Any, Dict


from gryszka_config_package.zzz.read_file import read_yml

def get_env_yml_config(db: str, config_filename: str, file_directory: str = "") -> Dict[str, Any]:
    config = read_yml(config_filename, file_directory)
    return config[db]
