from enum import Enum
#TODO:  make these not Enums (regular classes with variables)
class GenericTerrain(Enum):
    FLOOR = '.'
    WALL = '[color=grey][bkcolor=grey]#'
    FONT_FLOOR = ' '
    FONT_WALL = '#'

class ForestTerrain(Enum):
    TREE  =  '[color=green]T'
    FLOOR =  '.'
    ROCK  =  '[color=grey]#'
