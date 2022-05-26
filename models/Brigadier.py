from models.Workers import Workers


class Brigadier(Workers):

    def __init__(self, name: str, height: float, have_a_tractor: bool, experience: int):
        super(Brigadier, self).__init__(name, height)
        self.have_a_tractor = have_a_tractor
        self.experience = experience

    def  __str__(self) -> str:
        return f'Name - {self.name}, his height is {self.height}, and he has a traktor: {self.have_a_tractor}, his ' \
               f'experience : {self.experience} years'
