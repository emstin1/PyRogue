"""This is the main engine class.  Handles turns, drawing and user input"""

#TODO Separate this giant class into seperate subclasses for composition into the larger Engine class

class Engine:
    from bearlibterminal import terminal
    from sys import exit
    from Terrain import GenericTerrain
    from enum import Enum
    import Systems
    
    class States(Enum):
        START  = 0
        DRAW   = 1
        UPDATE = 2
        TURN   = 3

    def __init__(self, player, view):
        self.player  = player
        self.view = view
        self.VERSION = '0.0.1'
        self.current_state = self.States.START
        self.movement_system = self.Systems.MovementSystem()
        self.collision_system = self.Systems.CollisionSystem()
        self.vision_system = self.Systems.VisionSystem()
        self.current_screen = None

    def sort_entities(self):
        """sorts entities into Systems based on which components they have."""
        for entity in self.view.current_room.entities:
            if self.has_component(entity, 'movement'):
                self.movement_system.entities.append(entity)
            if self.has_component(entity, 'collision'):
                self.collision_system.entities.append(entity)
            if self.has_component(entity, 'vision'):
                self.vision_system.entities.append(entity)

    def move(self, entity):
        """processes any movement by entities"""
        if self.has_component(entity, "movement"):
            if self.has_component(entity, "coordinates"):
                self.movement_system.move_entity(entity)

    def fov(self, entity):
        if self.has_component(entity, 'vision'):
            self.vision_system.vision_circle(entity)
            self.vision_system.check_blocked_vision(entity, self.view.current_room.room)

    def has_component(self, entity, component):
        return component in entity.get_components()

    def set_state(self, new_state):
        self.current_state = new_state

    def update(self):
        """right now, this just updates the play-screen."""
        # TODO: once other screens are added, place their update methods here
        #collision check
        for entity in self.collision_system.entities:
            self.collision_system.check_collision(self.view.current_room.room, entity)
        for entity in self.movement_system.entities:
            self.move(entity)
        for entity in self.vision_system.entities:
            self.fov(entity)
        self.view.set_view(self.player.coordinates.x, self.player.coordinates.y, self.player.vision.visible_cells)
        self.player.vision.visible_cells = []
        self.set_state(self.States.DRAW)


    def draw_current_screen(self):
        """Right now, this method only draws the main game screen during play"""
        # TODO: make method able to draw any screen
        for y in range(self.view.height):
            for x in range(self.view.width):
                self.terminal.print(x, y, self.view.current_view[y][x])
        self.terminal.print(75, 0, "X: {}".format(self.player.coordinates.x))
        self.terminal.print(75, 1, "Y: {}".format(self.player.coordinates.y))
        self.terminal.refresh()
        self.set_state(self.States.TURN)

    def draw_gui(self):
        """This will draw the gui on-screen during play."""
        # TODO: get the gui stuff going.
        pass

    def input_loop(self):
        #this needs to block wait for input.  only certain input/actions will change state
        for entity in self.view.current_room.entities:
            if self.has_component(entity, "input"):
                while True:
                    if self.terminal.has_input():
                        key = self.terminal.read()
        
                        if key == self.terminal.TK_W: 
                            entity.movement.move_up = True
                            break

                        elif key == self.terminal.TK_S:
                            entity.movement.move_down = True
                            break

                        elif key == self.terminal.TK_A:
                            entity.movement.move_left = True
                            break

                        elif key == self.terminal.TK_D:
                            entity.movement.move_right = True
                            break

                        elif key == self.terminal.TK_Q:
                            self.exit()
        self.set_state(self.States.UPDATE)

    def initialize_window(self):
        #start up the bearlibterminal window when game first opens
        self.terminal.open()
        self.terminal.set("Window: title='PyRogue version {}', size=80x26".format(self.VERSION))
        self.terminal.refresh()
        self.current_state = self.current_state = self.States.UPDATE


    def run(self):
        self.sort_entities()
        while True:
            if self.current_state == self.States.START:
                self.initialize_window()

            if self.current_state == self.States.UPDATE:
                self.update()

            if self.current_state == self.States.DRAW:
                self.draw_current_screen()
                self.terminal.refresh()

            if self.current_state == self.States.TURN:
                self.input_loop()

