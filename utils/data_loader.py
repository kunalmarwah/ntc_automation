import json
import os

def load_test_data(filename):
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "test_data", filename)

    with open(file_path) as f:
        return json.load(f)