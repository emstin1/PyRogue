from math import floor

def get_line(x0,y0, x1,y1):
     pts = []
     swapxy = abs(y1-y0) > abs(x1-x0)
     if swapxy:
         tmp = x0
         x0 = y0
         y0 = tmp
         tmp = x1
         x1 = y1
         y1 = tmp
     if (x0 > x1):
         tmp = x0
         x0 = x1
         x1 = tmp
         tmp = y0
         y0  = y1
         y1  = tmp
     deltax = x1 - x0
     deltay = floor(abs(y1 - y0))
     error = floor(deltax / 2)
     y = y0
     if y0 < y1:
         ystep = 1
     else: ystep = -1
     if swapxy:
         for x in range(x0, x1+1):
             pts.append((x,y))
             error -= deltay
             if error < 0:
                 y = y + ystep
                 error = error + deltax
     else:
         for x in range(x0, x1 + 1):
             pts.append((x,y))
             error -= deltay
             if error < 0:
                 y = y + ystep
                 error = error + deltax
     return pts

