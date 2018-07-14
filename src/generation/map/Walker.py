class Slum:
    import random
    from Primitives import Shapes, Line, Util
    import Tiles
    """Walker(current_room, current_pos, life_timer=30)
       Slum Walker for slum generation
       current_room = a Room object
       current_pos = (x, y)
    """

    def __init__(self, current_room, current_pos, life_timer=10):
        self.current_room = current_room
        self.current_pos = current_pos
        #TODO:adjust this as necessary
        self.life_timer = life_timer
        self.right = (1,0)
        self.left  = (-1,0)
        self.up    = (0,-1)
        self.down  = (0,1)
        self.directions = [self.right, self.left, self.down, self.up]
        self.current_direction = self.random.choice(self.directions)
        self.previous_pos = None
        #tune to taste
        self.probability_to_stay_course = 96
        self.breeding_chance = 25
        self.carved_floor = []

    def breed(self):
        chance = round(100*self.random.random())
        if chance <= self.breeding_chance:
            return True
        else: return False

    def change_direction(self):
        chance = round(100*self.random.random())
        if chance >= self.probability_to_stay_course:
            new_dir= self.random.choice(self.directions)
            #So new_dir doesn't just come up as current_direction.  We want to actually change direction.
            while new_dir == self.current_direction:
                new_dir= self.random.choice(self.directions)
            self.current_direction = new_dir

    def walk(self):
        self.previous_pos = self.current_pos
        self.current_pos = self.Util.point_add(self.current_pos, self.current_direction)
        self.life_timer -= 1

    def wall_carve(self):
        up_wall = self.Util.point_add(self.current_pos, self.up)
        down_wall = self.Util.point_add(self.current_pos, self.down)
        right_wall = self.Util.point_add(self.current_pos, self.right)
        left_wall = self.Util.point_add(self.current_pos, self.left)
        return (up_wall, down_wall, left_wall, right_wall)

    def hall_carve(self):
        walls = self.wall_carve()
        self.current_room[self.current_pos] = self.Tiles.FLOOR
        self.carved_floor.append(self.current_pos)
        for wall in walls:
            if wall != self.previous_pos:
                if wall not in self.carved_floor:
                    self.current_room[wall] = self.Tiles.WALL
    
    def run(self):
            self.hall_carve()
            self.walk()
            self.change_direction()
