from asciimatics.screen import Screen
from Rooms import *
from Entities import *
from View import View
from Engine import Engine

room = DbRoom(1000, 1000)
room.init_room()
player = Player(100, 100)
view = View(room.room)
view.set_view(player.x, player.y)
engine = Engine(player, view)

Screen.wrapper(engine.run)
