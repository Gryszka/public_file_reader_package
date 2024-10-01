import pytest
from gryszka_config_package.yyy.main import get_env_yml_config


def test_get_env_yml_config_valid_db():
    config = get_env_yml_config('database1', 'config.yml', 'gryszka_config_package/xxx')
    assert config['host'] == 'localhost1'
    assert config['port'] == 1111
    assert config['user'] == 'admin1'
    assert config['password'] == 'secret1'

def test_get_env_yml_config_invalid_db():
    with pytest.raises(KeyError):
        get_env_yml_config('invalid_db', 'config.yml', 'gryszka_config_package/xxx')
