class Drone:
    def __init__(self, id_num):
        self.id = id_num

    def __del__(self):
        print(f"Drone {self.id} Destroyed!")

d1 = Drone(1)
d2 = Drone(2)

d1 = Drone(3)