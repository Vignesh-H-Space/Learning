class Drone:
    def __init__(self, id_num):
        self.id = id_num

    def __del__(self):
        print(f"Drone {self.id} Destroyed!")

