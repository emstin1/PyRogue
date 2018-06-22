"""functions for getting shapes"""

from . import Line
import pdb

def draw_circle(origin_x, origin_y, x, y):
    points = []
    points.append((origin_x + x, origin_y + y)) #bottom right
    points.append((origin_x - x, origin_y + y)) #bottom left
    points.append((origin_x + x, origin_y - y)) #top right
    points.append((origin_x - x, origin_y - y)) #top left
    points.append((origin_x + y, origin_y + x)) #bottom right sliver
    points.append((origin_x - y, origin_y + x)) #bottom left sliver
    points.append((origin_x + y, origin_y - x)) #top right sliver
    points.append((origin_x - x, origin_y - x)) #top left line
    return points


def get_circle(origin_x, origin_y, radius):
    """get_circle(origin_x, origin_y, radius)"""
    x = radius
    y = 0
    error = 1 - radius
    points = draw_circle(origin_x, origin_y, x, y)
    while x >= y:
        if (error <= 0):
            y += 1
            error += 2*y + 1

        else:
            x -= 1
            error -= 2*x + 1
        for point in draw_circle(origin_x, origin_y, x, y):
            points.append(point)

    return points

def filled_circle(origin_x, origin_y, radius):
    """filled_circle(origin_x, origin_y, radius)"""
    perimeter = get_circle(origin_x, origin_y, radius)
    rays = []
    for point in perimeter:
        ray = Line.get_line(origin_x, origin_y, point[0], point[1])
        rays.append(ray)
    return rays
    

def get_rect(length, width, origin_x, origin_y):
    """get_rect(length, width, origin_x, origin_y)"""
    points = []
    for point in Line.get_line(origin_x, origin_y, origin_x, origin_y+width):
        points.append(point)
    for point in Line.get_line(origin_x, origin_y, origin_x+length, origin_y):
        points.append(point)
    for point in Line.get_line(origin_x + length, origin_y, origin_x+length, origin_y+width):
        points.append(point)
    for point in Line.get_line(origin_x, origin_y+width, origin_x+length, origin_y+width):
        points.append(point)
    return points

def filled_rect(length, width, origin_x, origin_y):
    """filled_rect(length, width, origin_x, origin_y)"""
    pass

def get_diamond(origin_x, origin_y, size):
    """get_diamond(origin_x, origin_y, size)
       returns perimeter of diamond"""
    north = (origin_x, origin_y + size)
    south = (origin_x, origin_y - size)
    east  = (origin_x + size, origin_y)
    west  = (origin_x - size, origin_y)

    points = []

    points.append(Line.get_line(north[0], north[1], east[0], east[1]))
    points.append(Line.get_line(north[0], north[1], west[0], west[1]))
    points.append(Line.get_line(south[0], south[1], east[0], east[1]))
    points.append(Line.get_line(south[0], south[1], west[0], west[1]))
    
    return points

def filled_diamond(origin_x, origin_y, size):
    """filled_diamond(origin_x, origin_y, size)
       returns filled diamond, using rays originating from origin"""
    perimeter = get_diamond(origin_x, origin_y, size)
    points = []
    for line in perimeter:
        for point in line:
            line = Line.get_line(origin_x, origin_y, point[0], point[1])
            if line not in points:
                points.append(line)
    return points
