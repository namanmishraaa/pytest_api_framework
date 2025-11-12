# This is the data reader module for reading the test data.
import os
from pprint import pprint
import yaml


def load_test_data(file_name):
    """Reads test data from a given file and returns it as a list of lines."""
    file_path = os.path.join(os.path.dirname(__file__), f"../test_data/{file_name}")
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

# pprint(read_test_data("auth_data.yaml"))