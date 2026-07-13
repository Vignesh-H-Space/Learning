class Thermostat:
    def __init__(self):
        self._temp = 20

    @property
    def temp(self):
        return self._temp

