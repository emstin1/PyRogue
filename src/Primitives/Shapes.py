"""functions for getting shapes"""

from . import Line

def get_circle_perimeter(origin_x, origin_y, radius):
    """get_circle_perimiter(origin_x, origin_y, radius)"""
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
    perimeter = get_circle_perimeter(origin_x, origin_y, radius)
    center = (origin_x, origin_y)
    points = []
    points.append(center)

    for p in perimeter:
        for point in Line.get_line(origin_x, origin_y, p[0], p[1]):
            if point != center:
                points.append(point)
    return points
