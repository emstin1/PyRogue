class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y -= 1 
    def move_down(self):
        self.y += 1
    def move_right(self):
        self.x += 1
    def move_left(self):
        self.x -= 1


class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, x, y)
        self.health = 10 
