import Components
import os
import json

class Entity:
    def __init__(self, **cmps):
        self.__dict__.update(cmps)
        self.components = cmps

    def add_component(self, **cmps):
        self.__dict__.update(cmps)
        self.components.update(cmps)

    def get_components(self):
        """returns a list of the component names"""
        return list(self.components.keys())

def create_entity(entity_dict):
    """creates entities from given params"""
    entity = Entity()
    if entity_dict['has movement']:
        entity.add_component(movement=Components.ComponentMovement())
    if entity_dict['has coordinates']:
        entity.add_component(coordinates=Components.ComponentCoordinate())
    if entity_dict['has rendering']:
        entity.add_component(render=Components.ComponentRender())
        entity.render.body = entity_dict['body']
    if entity_dict['has input']:
        entity.add_component(input=Components.ComponentInput())
    if entity_dict['has collision']:
        entity.add_component(collision=Components.ComponentCollision())
    if entity_dict['has vision']:
        entity.add_component(vision=Components.ComponentFOV())
    return entity

def load_entity(entity_type, name):
    """creates entity from coresponding entity file"""
    f = os.path.join('content', entity_type, "{}.json".format(name))
    with open(f, 'r') as entity_file:
        entity = entity_file.read()
    return json.loads(entity)
