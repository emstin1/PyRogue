class TestRoom:
    from random import randint, seed
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.room = None
        self.empty_floor = '.'
        self.rock = '#'

    def __return_random_tile(self):
        val = self.randint(0,1)
        if val == 0:
            return self.empty_floor
        elif val == 1:
            return self.rock

    def init_room(self):
        self.room = [ [self.__return_random_tile() for x in range(self.width)] for y in range(self.height)]

class DbRoom(TestRoom):
    def __init__(self, width, height):
        TestRoom.__init__(self, width, height)


class ForestRoom(TestRoom):
    from random import choice
    from Terrain import ForestTerrain
    def __init__(self, width, height, usr_seed, rng_range):
        TestRoom.__init__(self, width, height)
        self.usr_seed = usr_seed
        self.rng_range = rng_range
        TestRoom.seed(self.usr_seed)

    def init_room(self):
       self.room = [ [self.ForestTerrain.FLOOR.value for x in range(self.width)] for y in range(self.height)] 
    
    def generate(self, tree_number, seeding_radius, seedfall, decay_rate, ground_coverage):
        """Grows our Trees for our forest

           tree_number     = ininital number of trees
           seeding_radius  = radius seeds from trees can travel
           seedfall        = number of seeds that fall from trees
           decay_rate      = rate at which fallen seeds decay, given as a decimal percentage (eg 0.14 is 14%)
           ground_coverage = percentage of the room to be covered in trees (same as above)"""
        seeding_chance = 22
        tree_coords = []
        seed_coords = []
        # inital trees of the room
        for _ in range(tree_number):
            seed_y = self.randint(0, self.height-1)
            seed_x = self.randint(0, self.width-1)
            tree_coords.append( (seed_x, seed_y) )
            self.room[seed_y][seed_x] = self.ForestTerrain.TREE.value
        # growing loop
        while len(tree_coords) < ( (self.height * self.width) * ground_coverage):
            # seeds decay
            seed_coords = [seeds for seeds in seed_coords if self.randint(1, 100) > (ground_coverage * 100)]
            
            # growing seeds
            for x in seed_coords:
                if self.room[x[1]][x[0]] != self.ForestTerrain.TREE.value:
                    if self.randint(1, 100) <= seeding_chance:
                        self.room[x[1]][x[0]] = self.ForestTerrain.TREE.value 
                        tree_coords.append(x)
            # spreading seeds within seeding_radius
            for tree in tree_coords:
                tree_x = tree[0]
                tree_y = tree[1]
                seeding_area = []
