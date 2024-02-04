from dataclasses import dataclass


@dataclass
class ProjectInfo:
    header: str
    description: str
    language: str
    url: str
