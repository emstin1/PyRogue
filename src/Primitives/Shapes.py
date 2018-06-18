"""functions for getting shapes"""

from . import Line

def get_circle(origin_x, origin_y, radius):
    """get_circle(origin_x, origin_y, radius)"""
    x = radius
    y = 0
    error = 0
    points = []
    while x >= y:
        points.append((origin_x + x, origin_y + y))
        points.append((origin_x + y, origin_y + x))
        points.append((origin_x - y, origin_y + x))
        points.append((origin_x - x, origin_y + y))
        points.append((origin_x - x, origin_y - y))
        points.append((origin_x - y, origin_y - x))
        points.append((origin_x + y, origin_y - x))
        points.append((origin_x + x, origin_y - y))

        if error <= 0:
            y += 1
            error += (2*y) + 1
        if error > 0:
            x -= 1
            error -= (2*x) + 1

    return points

def filled_circle(origin_x, origin_y, radius):
    """filled_circle(origin_x, origin_y, radius)"""
    perimeter = get_circle(origin_x, origin_y, radius)
    points = []

    for point in perimeter:
        line = Line.get_line(origin_x, origin_y, point[0], point[1])
        points.append(line)
    return points

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
