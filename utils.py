import os
import json

def save_json(path: str, data: dict):
    """save json data

    Args:
        path (str): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"json file saved at: {path}")