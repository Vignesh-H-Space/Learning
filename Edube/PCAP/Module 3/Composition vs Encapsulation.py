class Engine:
    def __init__(self):
        self.__status = "Stopped"

    def start(self):
        self.__status = "Running"