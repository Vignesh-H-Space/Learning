class Thermostat:
    def __init__(self):
        self._temp = 20

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if value < 0:
            self._temp = 0
        else:
            self._temp = value
            
            
ac = Thermostat()

ac.temp = -10

ac._temp = -5

print(ac.temp)