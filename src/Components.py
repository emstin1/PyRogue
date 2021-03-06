#TODO components need to be turned into pure data instead of python objects. 

class ComponentMovement:
    """the movement component.  any entity with this component can move"""
    move_up    = False
    move_down  = False
    move_left  = False
    move_right = False

class ComponentCoordinate:
    """Any Entity with this component exists physically within the world"""
    x = 0
    y = 0

class ComponentInput:
    """Any Entity with this component accepts user input for control"""
    accepts_input = True

class ComponentRender:
    """If it has this component, it gets drawn when in view"""
    visible = True
    body = 0

class ComponentCollision:
    """solid objects collide with walls etc"""
    solid = True


class ComponentAI:
    #TODO: implement each AI type
    pass



class ComponentFOV:
    """Entity with FOV can see stuff around it"""
    #TODO: Field of View Component
    vision = True
    los_distance = 10
    vision_circle = []
    visible_cells = []
