import requests
from utils.config_reader import get_base_url
from utils.logger import logger

def test_get_all_bookings():
    """Test to retrieve all bookings."""
    logger.info("Starting test_get_all_bookings")
    base_url = get_base_url()
    logger.info(f"Base URL: {base_url}")
    response = requests.get(f"{base_url}/booking")
    logger.info(f"Request URL: {response.url}")
    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response body: {response.text}")
    assert response.status_code == 200, f"Failed to get bookings: {response.text}"
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    logger.info("Finished test_get_all_bookings")

def test_create_booking():
    """Test to create a new booking."""
    logger.info("Starting test_create_booking")
    base_url = get_base_url()
    logger.info(f"Base URL: {base_url}")
    booking_data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Lunch"
    }
    headers = {"Content-Type": "application/json"}
    logger.info(f"Request body: {booking_data}")
    response = requests.post(f"{base_url}/booking", json=booking_data, headers=headers)
    logger.info(f"Request URL: {response.url}")
    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response body: {response.text}")
    assert response.status_code == 200, f"Failed to create booking: {response.text}"
    response_json = response.json()
    assert "bookingid" in response_json
    assert response_json["booking"]["firstname"] == booking_data["firstname"]
    assert response_json["booking"]["lastname"] == booking_data["lastname"]
    assert response_json["booking"]["totalprice"] == booking_data["totalprice"]
    assert response_json["booking"]["depositpaid"] == booking_data["depositpaid"]
    assert response_json["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response_json["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response_json["booking"]["additionalneeds"] == booking_data["additionalneeds"]
    logger.info("Finished test_create_booking")

def test_create_booking_negative():
    """Negative test to create a new booking with invalid data."""
    logger.info("Starting test_create_booking_negative")
    base_url = get_base_url()
    logger.info(f"Base URL: {base_url}")
    invalid_booking_data = {}  # Empty payload
    headers = {"Content-Type": "application/json"}
    logger.info(f"Request body: {invalid_booking_data}")
    response = requests.post(f"{base_url}/booking", json=invalid_booking_data, headers=headers)
    logger.info(f"Request URL: {response.url}")
    logger.info(f"Response status code: {response.status_code}")
    logger.info(f"Response body: {response.text}")
    assert response.status_code == 500, f"Expected status code 500 for invalid data, but got {response.status_code}. Response: {response.text}"
    logger.info("Finished test_create_booking_negative")
