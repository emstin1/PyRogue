import pdb
class View:
    from Terrain import GenericTerrain
    def __init__(self, current_room):
        self.current_room = current_room
        self.current_view = []
        self.width = 50
        self.height = 17

    def set_view(self, playerx, playery, player_view):
        self.current_view = []
        view_x = playerx - round(self.width / 2)
        view_y = playery - round(self.height / 2)
        
        for y in range(self.height):
            temp_row = []
            for x in range(self.width):
                current_cell = (view_x + x, view_y + y)
                try:
                    if current_cell in player_view:
                        cell = self.current_room.room[current_cell]
                    else: 
                        cell = self.GenericTerrain.BLANK.value
                except KeyError:
                    self.current_room.room[(view_x + x, view_y + y)] = self.GenericTerrain.WALL.value
                    cell = self.current_room.room[current_cell]

                for entity in self.current_room.entities:
                    if (entity.coordinates.x, entity.coordinates.y) == current_cell:
                        cell = entity.render.body

                temp_row.append(cell)
            self.current_view.append(temp_row)
