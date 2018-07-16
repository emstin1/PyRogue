#!/usr/bin/env python3
from Rooms import *
import Entities
from View import View
from Engine import Engine
from Components import *

cave = Room('slum', 'this is a seed')
cave.init_room()
player = Entities.create_entity( Entities.load_entity('mobs', 'player'))
player.coordinates.x = 0
player.coordinates.y = 0
player.input.accepts_input = True

cave.entities.append(player)



#debugging entity rendering
"""
with open('view-debug.txt', 'w') as viewdb:
    for row in view.current_view:
        for cell in row:
            viewdb.write("{}\n".format(cell))

"""
view = View(cave)
view.set_view(player.coordinates.x, player.coordinates.y, player.vision.visible_cells)


engine = Engine(player, view)
engine.run()
