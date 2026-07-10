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