#TODO: turn temp_row.append(cell) into a list comprehension.  Should offer some speedup
import pdb
class View:
    from Terrain import GenericTerrain
    import Tiles
    def __init__(self, current_room):
        self.current_room = current_room
        self.current_view = []
        self.width = 75
        self.height = 17
        self.int_to_tile = {self.Tiles.WALL: self.GenericTerrain.WALL.value, self.Tiles.FLOOR: self.GenericTerrain.FLOOR.value,
                            self.Tiles.BLANK: self.GenericTerrain.BLANK.value}

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
                        #turning our Tile int to the Rendering character
                        cell = self.int_to_tile[self.current_room.room[current_cell]]
                    else: 
                        cell = self.int_to_tile[self.Tiles.BLANK]
                except KeyError:
                    self.current_room.room[(view_x + x, view_y + y)] = self.Tiles.WALL
                    cell = self.int_to_tile[self.current_room.room[current_cell]]

                for entity in self.current_room.entities:
                    if (entity.coordinates.x, entity.coordinates.y) == current_cell:
                        cell = entity.render.body

                temp_row.append(cell)
            self.current_view.append(temp_row)
