from utilities.config_reader import read_config, get_base_url

def test_read_config_returns_base_url():
    config = read_config()
    assert "base_url" in config
    assert get_base_url().startswith("https://")
