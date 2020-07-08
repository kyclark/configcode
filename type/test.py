import algorithm
from config import Config
from typing import List

def test_config():
    conf = algorithm.config()
    assert conf
    assert type(conf) == Config
    assert type(conf.version) == str
    assert type(conf.author) == list
    assert type(conf.author_email) == list
    assert type(conf.write_betydb_csv) == bool

