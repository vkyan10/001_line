from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if (x0 < x1):
        x = int(x0)
        y = int(y0)
        x1 = int(x1)
        y1 = int(y1)
    else:
        x = int(x1)
        y = int(y1)
        x1 = int(x0)
        y1 = int(y0)

    A = 2 * (y1 - y)
    B = -2 * (x1 - x)

    #vertical line
    if B == 0:
        if y > y1:
            temp = y
            y = y1
            y1 = temp
        while y <= y1:
            plot(screen, color, x, y)
            y += 1

    #horizontal line
    elif A == 0:
        while x <= x1:
            plot(screen, color, x, y)
            x += 1
    else:
        m = -1 * A / B

        # octant 1 and 5:
        if 0 < m <= 1:
            d = A + int(B / 2)
            while x <= x1:
                plot(screen, color, x, y)
                if d > 0:
                    y += 1
                    d += B
                x += 1
                d += A

        # octant 2 and 6
        elif m > 1:
            d = int(A / 2) + B
            while y <= y1:
                plot(screen, color, x, y)
                if d < 0:
                    x += 1
                    d += A
                y += 1
                d += B

        # octant 8 and 4
        elif -1 <= m < 0:
            d = A - int(B/2)
            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y -= 1
                    d -= B
                x += 1
                d += A

        # octant 7 and 3
        else: # m < -1
            d = int(A / 2) - B
            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x += 1
                    d += A
                y -= 1
                d -= B
