def get_line(x0,y0, x1,y1):
    """get_line(x0, y0, x1, y1)"""
    line = []
    negative_line = False
    swapxy = abs(y1-y0) > abs(x1-x0)
    if swapxy:
        tmp = x0
        x0 = y0
        y0 = tmp
        tmp = x1
        x1 = y1
        y1 = tmp
    if x0 > x1:
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0  = y1
        y1  = tmp
        negative_line = True
    deltax = x1 - x0
    deltay = round(abs(y1 - y0))
    error = round(deltax / 2)
    y = y0
    if y0 < y1:
        ystep = 1
    else: ystep = -1
    if swapxy:
        for x in range(x0, x1+1):
           line.append((x,y))
           error -= deltay
           if error < 0:
              y = y + ystep
              error = error + deltax
    else:
        for x in range(x0, x1 + 1):
           line.append((x,y))
           error -= deltay
           if error < 0:
              y = y + ystep
              error = error + deltax
    if negative_line:
        line = line[::-1]
    return line
