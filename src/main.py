from Rooms import *
import Entities
from View import View
from Engine import Engine
from Components import *

cave = CaveRoom(1000, 1000, "this is a seed", 2)
cave.carve_cave(1)
player = Entities.create_entity( Entities.load_entity('mobs', 'player'))
player.coordinates.x = 10
player.coordinates.y = 9
player.input.accepts_input = True

cave.room.entities.append(player)



#debugging entity rendering
"""
with open('view-debug.txt', 'w') as viewdb:
    for row in view.current_view:
        for cell in row:
            viewdb.write("{}\n".format(cell))

"""
view = View(cave.room)
view.set_view(player.coordinates.x, player.coordinates.y, player.vision.visible_cells)


engine = Engine(player, view)
engine.run()
