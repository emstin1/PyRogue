class Room:
    from Terrain import GenericTerrain
    import Tiles
    from random import randint, seed
    import pickle
    from os import path

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.room = {}
        self.entities = []

    def __return_random_tile(self):
        val = self.randint(0,1)
        if val == 0:
            return self.GenericTerrain.FLOOR.value
        elif val == 1:
            return self.GenericTerrain.WALL.value

    def init_room(self):
        for x in range(self.width):
            for y in range(self.height):
                self.room[(x, y)] = self.Tiles.FLOOR
    def load_room(self, room_name):
        """loads room from pickle file"""
        roomfile = self.path.join('savedata', '{}.p'.format(room_name))
        self.pickle.load(open(roomfile, 'rb'))

    def save_room(self, room_name):
        """saves room to pickle file"""
        roomfile = self.path.join('savedata', '{}.p'.fomrat(room_name))
        self.pickle.dump(self.room, open(roomfile, 'wb'))

class DbRoom:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.room = Room(self.width, self.height)
        self.room.init_room()
    
    def carve_perimeter(self):
        for x in range(self.width):
            self.room.room[(x, 0)] = self.room.Tiles.WALL
            self.room.room[(x, self.height-1)] = self.room.Tiles.WALL
            for y in range(self.height):
                self.room.room[(0, y)] = self.room.Tiles.WALL
                self.room.room[(self.width-1, y)] = self.room.Tiles.WALL

class CaveRoom:
    def __init__(self, width, height, usr_seed, erosion_rate):
        self.width = width
        self.height = height
        self.usr_seed = usr_seed
        self.erosion_rate = erosion_rate
        self.room = Room(self.width, self.height)
        self.room.seed(usr_seed)
        self.room.init_room()

    def carve_cave(self, steps):
        while steps > 0:
            for x in range(self.width):
                for y in range(self.height):
                    neighbors = 0
                    if self.room.room[(x, y)] == self.room.GenericTerrain.WALL.value:
                        try:
                            if self.room.room[(x+1, y)] == self.room.GenericTerrain.WALL.value:
                                neighbors += 1
                        except KeyError: pass

                        try:
                            if self.room.room[(x-1, y)] == self.room.GenericTerrain.WALL.value:
                                neighbors += 1
                        except KeyError: pass

                        try:
                            if self.room.room[(x, y+1)] == self.room.GenericTerrain.WALL.value:
                                neighbors += 1
                        except KeyError: pass

                        try:
                            if self.room.room[(x, y-1)] == self.room.GenericTerrain.WALL.value:
                                neighbors += 1
                        except KeyError: pass

                    if neighbors < self.erosion_rate:
                        self.room.room[(x, y)] = self.room.GenericTerrain.FLOOR.value
            steps -= 1

class DebugMainMenu:
    def __init__(self):
        self.current_line = 1
        self.title = "[color=red]PYROGUE DEBUG MODE"
        self.line1 = "{}{}LOAD MAP"
        self.line2 = "{}{}NEW MAP"

    def display(self, terminal):
        if self.current_line == 1:
            terminal.print(10, 10, self.title)
            terminal.print(10, 11, self.line1.format("color=black", "bkcolor=white"))
            terminal.print(10, 12, self.line2.format("color=white", "bkcolor=black"))
        elif self.current_line == 2:
            termina.print(10, 10, self.title)
            terminal.print(10, 11, self.line1.format("color=white", "bkcolor=black"))
            terminal.print(10, 12, self.line2.format("color=black", "bkcolor=white"))
