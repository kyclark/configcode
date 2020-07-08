from typing import NamedTuple, List


class Config(NamedTuple):
    version: str
    author: List[str]
    author_email: List[str]
    write_betydb_csv: bool
