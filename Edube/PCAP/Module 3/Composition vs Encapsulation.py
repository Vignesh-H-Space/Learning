class Engine:
    def __init__(self):
        self.__status = "Stopped"

    def start(self):
        self.__status = "Running"

    def get_status(self):
        return self.__status

class Car:
    def __init__(self):
        # The Car HAS an Engine (Composition), not IS an Engine
        self.engine = Engine()

    def start_car(self):
        self.engine.start()

    def inspect_engine(self):
        # Trap: Trying to peek at the engine's private variable directly!
        try:
            return self.engine.__status
        except AttributeError:
            return "Access Denied"

my_car = Car()
my_car.start_car()
