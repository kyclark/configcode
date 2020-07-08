import algorithm
from config import Config
from typing import List

def test_config():
    conf = algorithm.config()
    assert conf
    assert type(conf) == Config
    assert type(conf.version) == str
    assert type(conf.algorithm_author) == list
    assert type(conf.algorithm_author_email) == list
    assert type(conf.write_betydb_csv) == bool

