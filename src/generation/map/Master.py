class Master:
    from generation.map import Walker
    import random

    def __init__(self, current_room, room_type, seed):
        self.current_room = current_room
        self.walkers = []
        self.room_type = room_type
        self.seed = seed
        self.random.seed(self.seed)
        #TODO:add more walker types as the created
        self.get_walkers = {'slum': self.Walker.Slum,}
        self.walker_type = self.get_walkers[self.room_type]
        self.breeding_chance = 30
        self.carved_floor = []

    def add_walker(self, pos):
        self.walkers.append(self.walker_type(self.current_room, pos, hash(self.seed) + self.breeding_chance))

    def kill_walkers(self):
        #any walker in the pool gets dropped if it's life time is 0 or less
        self.walkers = [walker for walker in self.walkers if walker.life_timer > 0]

    def run(self):
        while self.walkers != []:
            print(len(self.walkers))
            for walker in self.walkers:
                walker.carved_floor = self.carved_floor
                walker.run()
                self.carved_floor += [x for x in walker.carved_floor if x not in self.carved_floor]
                if walker.breed() and self.random.choice(range(len(self.walkers))) <= self.breeding_chance:
                    self.add_walker(walker.current_pos)
                    self.breeding_chance -= 1
            self.kill_walkers()
