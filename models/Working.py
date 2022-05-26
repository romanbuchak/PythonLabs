from models.Workers import Workers


class Working(Workers):

    def __init__(self, name: str, height: float, work_in_saturday: bool):
        super(Working, self).__init__(name, height)
        self.work_in_saturday = work_in_saturday

    def  __str__(self) -> str:
        return f'Name - {self.name}, his height is {self.height}, and he work in Saturday: {self.work_in_saturday}'