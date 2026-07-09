class Engine:
    def __init__(self):
        self.__status = "Stopped"

    def start(self):
        self.__status = "Running"

    def get_status(self):
        return self.__status
