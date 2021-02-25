from display import *
from draw import *

s = new_screen()
c = [255, 0, 0]

y = 240
for x in range(133, 367):
    draw_line(x, y, x, y+15, s, c)
    print(c)
    if c[GREEN] != 255 and c[RED] == 255:
        c[GREEN] += 5  # red to yellow
    elif c[RED] != 0 and c[BLUE] == 0:
        c[RED] -= 5    # yellow to green
    elif c[BLUE] != 255:
        c[BLUE] += 5   # green to bright blue
    elif c[GREEN] != 0:
        c[GREEN] -= 5  # bright blue to dark blue
    else:
        c[RED] += 5    # dark blue to purple

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
