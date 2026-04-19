from dataclasses import dataclass

@dataclass
class Commit:
    hash: str
    date: str
    author: str
    message: str

