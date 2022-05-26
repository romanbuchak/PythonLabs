from models.Brigadier import Brigadier
from models.Manager import Manager
from models.Scientist import Scientist
from models.Working import Working

workers1 = Manager("Ivan", 182, True, 25)
print(workers1)

workers2 = Scientist("Petro", 165, True)
print(workers2)

workers3 = Working("Payl", 187, False)
print(workers3)

workers4 = Brigadier("Ryslan", 177, True, 23)
print(workers4)
