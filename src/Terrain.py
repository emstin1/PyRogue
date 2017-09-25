from enum import Enum
#TODO:  make these not Enums (regular classes with variables)
class GenericTerrain(Enum):
    FLOOR = '[bkcolor=black] '
    WALL = '[color=grey][bkcolor=grey]#'

class ForestTerrain(Enum):
    TREE  =  '[color=green]T'
    FLOOR =  '.'
    ROCK  =  '[color=grey]#'
