import json
import os


def config() -> dict:
    file = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(file) as fh:
        return json.load(fh)
