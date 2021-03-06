#The System part of the Entity-Component-System

class MovementSystem:
    def __init__(self):
        self.entities = []

    def move_entity(self, entity):
        """moves the entity"""
        if entity.movement.move_up:
            entity.coordinates.y -= 1
            entity.movement.move_up = False

        elif entity.movement.move_down:
            entity.coordinates.y += 1
            entity.movement.move_down = False

        elif entity.movement.move_left:
            entity.coordinates.x -= 1
            entity.movement.move_left = False

        elif entity.movement.move_right:
            entity.coordinates.x += 1
            entity.movement.move_right = False



class InputSystem:
    def __init__(self):
        self.entities = []


class CollisionSystem:
    import Tiles

    def __init__(self):
        self.entities = []

    def check_collision(self, current_room, entity):
        """checks if current desired move will cause collision and if so, stop the move"""
        if entity.movement.move_up:
            if current_room[(entity.coordinates.x, entity.coordinates.y - 1)] == self.Tiles.WALL:
                entity.movement.move_up = False
        elif entity.movement.move_down:
            if current_room[(entity.coordinates.x, entity.coordinates.y + 1)] == self.Tiles.WALL:
                entity.movement.move_down = False
        elif entity.movement.move_left:
            if current_room[(entity.coordinates.x - 1, entity.coordinates.y)] == self.Tiles.WALL:
                entity.movement.move_left = False
        elif entity.movement.move_right:
            if current_room[(entity.coordinates.x + 1, entity.coordinates.y)] == self.Tiles.WALL:
                entity.movement.move_right = False

class VisionSystem:
    import Tiles
    from Primitives import Shapes
    
    def __init__(self):
        self.entities = [] 

    def vision_circle(self, entity):
        """generates each point in the vision circle of the entity.  Does not check for blocked vision"""
        entity.vision.vision_circle = self.Shapes.filled_circle(entity.coordinates.x, entity.coordinates.y, entity.vision.los_distance)

    def check_blocked_vision(self, entity, room):
        """checks each ray in the vision circle for vision-blocking points"""
        for ray in entity.vision.vision_circle:
            for point in ray:
                try:
                    if room[point] == self.Tiles.WALL:
                        entity.vision.visible_cells.append(point)
                        break
                    else:
                        entity.vision.visible_cells.append(point)
                except KeyError: entity.vision.visible_cells.append(point)
