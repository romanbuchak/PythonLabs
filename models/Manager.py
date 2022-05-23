from models.Workers import Workers


class Manager(Workers):

    def __init__(self, name: str, height: float, have_a_good_fee: bool, age: int):
        super(Manager, self).__init__(name, height)
        self.have_a_good_fee = have_a_good_fee
        self.age = age

    def get_manager(self) -> str:
        return f'Name - {self.name}, his height is {self.height}, and he has a good fee: {self.have_a_good_fee}, his ' \
               f'age is {self.age} '
