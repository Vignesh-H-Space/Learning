class Score:
    def __init__(self, points):
        self.points = points

    def __str__(self):
        return self.points

my_score = Score(100)

print(my_score)