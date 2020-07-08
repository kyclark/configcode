from typing import NamedTuple, List


class Config(NamedTuple):
    version: str
    algorithm_author: List[str]
    algorithm_author_email: List[str]
    algorithm_contributors: List[str]
    algorithm_name: str
    algorithm_description: str
    citation_author: str
    citation_title: str
    citation_year: str
    variable_names: List[str]
    variable_units: List[str]
    variable_labels: List[str]
    write_betydb_csv: bool
    write_geostreams_csv: bool
