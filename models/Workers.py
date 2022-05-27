from abc import ABC


class Workers(ABC):

    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height
