from Rooms import *
import Entities
from View import View
from Engine import Engine
from Components import *

cave = DbRoom(1000, 1000)
cave.carve_perimeter()
player = Entities.create_entity( Entities.load_entity('mobs', 'player'))
player.coordinates.x = 25
player.coordinates.y = 50
player.input.accepts_input = True
cave.place_wall(10,10, 5, 10)

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
