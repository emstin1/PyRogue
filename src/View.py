class View:
    def __init__(self, current_room):
        self.current_room = current_room
        self.current_view = []
        self.width = 100
        self.height = 35

    def set_view(self, playerx, playery):
        self.current_view = []
        view_x = playerx - self.width 
        view_y = playery - self.height 
        
        for y in range(self.height):
            temp_row = []
            for x in range(self.width):
                temp_row.append( self.current_room[view_y + y][view_x + x] )
            self.current_view.append(temp_row)
