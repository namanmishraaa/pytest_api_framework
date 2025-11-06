





def test_authentication(get_token):
    """Test to verify that the authentication token is obtained correctly."""
    assert get_token is not None
    assert isinstance(get_token, str)
    assert len(get_token) > 0