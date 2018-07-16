class Room:
    from generation.map import Master
    def __init__(self, room_type, seed):
        self.room_type = room_type
        self.seed = seed
        self.room = {}
        self.entities = []
        self.walker_master = self.Master.Master(self.room, self.room_type, self.seed)

    def init_room(self):
        self.walker_master.add_walker((0,0))
        self.walker_master.run()

class TestRoom:
    from Terrain import GenericTerrain
    import Tiles

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.room = {}
        self.entities = []

    def init_room(self):
        for x in range(self.width):
            for y in range(self.height):
                self.room[(x, y)] = self.Tiles.FLOOR

class DbRoom:
    from Primitives import Line
    from Primitives import Shapes
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.room = TestRoom(self.width, self.height)
        self.room.init_room()
    
    def carve_perimeter(self):
        for x in range(self.width):
            self.room.room[(x, 0)] = self.room.Tiles.WALL
            self.room.room[(x, self.height-1)] = self.room.Tiles.WALL
            for y in range(self.height):
                self.room.room[(0, y)] = self.room.Tiles.WALL
                self.room.room[(self.width-1, y)] = self.room.Tiles.WALL

    def place_wall(self, start_x, start_y, end_x, end_y):
        wall = self.Line.get_line(start_x, start_y, end_x, end_y)
        for point in wall:
            self.room.room[point] = self.room.Tiles.WALL

    def place_room(self, length, width, origin_x, origin_y):
        rect = self.Shapes.get_rect(length, width, origin_x, origin_y)
        for point in rect:
            self.room.room[point] = self.room.Tiles.WALL
        door = rect[3]
        self.room.room[door] = self.room.Tiles.FLOOR

class CaveRoom:
    def __init__(self, width, height, usr_seed, erosion_rate):
        self.width = width
        self.height = height
        self.usr_seed = usr_seed
        self.erosion_rate = erosion_rate
        self.room = TestRoom(self.width, self.height)
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
