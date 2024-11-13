import os
import json

def load_users():
    if os.path.exists("data/_users.json"):
        with open("data/_users.json", "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open("data/_users.json", "w") as f:
        json.dump(users, f)