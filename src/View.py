class View:
    from Terrain import GenericTerrain
    def __init__(self, current_room):
        self.current_room = current_room
        self.current_view = []
        self.width = 50
        self.height = 17

    def set_view(self, playerx, playery):
        self.current_view = []
        view_x = playerx - int(self.width / 2)
        view_y = playery - int(self.height / 2)
        
        for y in range(self.height):
            temp_row = []
            for x in range(self.width):
                try:
                    cell = self.current_room.room[(view_x + x, view_y + y)]
                except KeyError:
                    self.current_room.room[(view_x + x, view_y + y)] = self.GenericTerrain.WALL.value
                    cell = self.current_room.room[(view_x + x, view_y + y)]

                for entity in self.current_room.entities:
                    if entity.coordinates.x == view_x + x and entity.coordinates.y == view_y + y:
                        cell = entity.render.body

                temp_row.append(cell)
            self.current_view.append(temp_row)