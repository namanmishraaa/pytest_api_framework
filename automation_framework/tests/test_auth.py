
from utils.logger import logger




def test_authentication(get_token):
    """Test to verify that the authentication token is obtained correctly."""
    logger.info("Starting test_authentication")
     # The get_token fixture is expected to provide the authentication token
    logger.debug(get_token)
    logger.info("test_authentication")
    assert get_token is not None
    assert isinstance(get_token, str)
    assert len(get_token) > 0
    logger.info("Finished test_authentication")