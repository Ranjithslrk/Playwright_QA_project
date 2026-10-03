import json


def get_login_users():
    with open("test_data/test_data.json", "r") as read_file:
        test_data = json.load(read_file)
        return test_data["login_users"]