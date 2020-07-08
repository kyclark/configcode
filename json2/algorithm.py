import json
import os
from config import Config


def config() -> Config:
    file = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(file) as fh:
        return Config(**json.load(fh))
