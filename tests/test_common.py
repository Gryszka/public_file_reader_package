import pytest
from gryszka_config_package.zzz.read_file import read_yml


@pytest.fixture(autouse=True)
def setup_config_yml():
    mock_config_content = """
    env1:
      key1a: value1a
      key1b: value1b

    env2:
      key2a: value2a
      key2b: value2b
    """
    mock_config_file_name = "mocked_config.yml"
    mock_config_path = "mocked/config/path"
    
    return {
        "content" : mock_config_content,
        "file_name": mock_config_file_name,
        "file_path": mock_config_path,
    }



def test_read_yml(setup_config_yml):
    config = read_yml(setup_config_yml["file_name"], setup_config_yml["file_path"])
    print(config)