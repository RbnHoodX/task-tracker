from dataclasses import dataclass


@dataclass
class Task:
    id: int = 0
    title: str = ""
