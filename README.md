# file reader package
The package tests , how to read file form a package.
Tests run with access to the source code or just with the package.

## Installation 

```bash
pip install gryszka-config-package
```

```python
from gryszka_config_package.yyy.ddd.eee.main import get_env_yml_config

print(get_env_yml_config('database2', 'config.yml', 'gryszka_config_package/xxx/rrr/ttt'))
```

```python
from gryszka_config_package.zzz.uuu.ooo.read_file import read_yml

config_filename = 'config.yml'
file_directory = 'gryszka_config_package/xxx/rrr/ttt'

print(read_yml(config_filename, file_directory))
```