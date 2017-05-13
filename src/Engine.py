"""This class draws the game to the terminal"""

class Engine:
    from sys import exit
    from enum import Enum

    def __init__(self, player, view):
        self.player  = player
        self.view = view

    class Keys(Enum):
        UP         = ord('w')
        DOWN       = ord('s')
        LEFT       = ord('a')
        RIGHT      = ord('d')
        DEBUG_QUIT = ord('Q')

    def draw_play_room(self, screen):
        """This method draws the main game screen during play"""
        #draw 
        for y in range(self.view.height):
            for x in range(self.view.width):
                screen.print_at(self.view.current_view[y][x], x, y)
        screen.print_at("@", 45, 16, colour=161)


    def handle_user_input(self, screen):
        key = screen.get_event()
        
        if key:
            if key.key_code == self.Keys.UP.value:
                self.player.move_up()
            elif key.key_code == self.Keys.DOWN.value:
                self.player.move_down()
            elif key.key_code == self.Keys.LEFT.value:
                self.player.move_left()
            elif key.key_code == self.Keys.RIGHT.value:
                self.player.move_right()
            elif key.key_code == self.Keys.DEBUG_QUIT.value: self.exit()

    def run(self, screen):
        while True:
            self.draw_play_room(screen)
            self.handle_user_input(screen)
            self.view.set_view(self.player.x, self.player.y)
            screen.refresh()
