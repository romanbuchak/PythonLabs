from models.Workers import Workers


class Scientist(Workers):

    def __init__(self, name: str, height: float, have_a_patent: bool):
        super(Scientist, self).__init__(name, height)
        self.have_a_patent = have_a_patent

    def get_scientist(self) -> str:
        return f'Name - {self.name}, his height is {self.height}, and he has a patent: {self.have_a_patent}'
