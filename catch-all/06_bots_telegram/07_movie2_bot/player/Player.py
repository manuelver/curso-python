class Player:

    id = ''
    points = 0
    name = ''

    def __init__(self, uid):
        self.id = uid

    def get_points(self):
        return self.points

    def set_name(self, name):
        self.name = name

    def add_points(self, points):
        self.points += points
