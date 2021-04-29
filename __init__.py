from math import *
import os
import numpy as np

def point_grapher(
        x_vals:list, y_vals:list,
        x_range:tuple=None,
        y_range:tuple=None,):
    if x_range==None:
        x_range=(min(x_vals),
                 max(x_vals))
    if y_range==None:
        y_range=(min(y_vals),
                 max(y_vals))
    
    cols,rows=os.get_terminal_size()
    cols -= 2
    rows -= 2
    
    print(f" {x_range[0]:<10.0f}"
          f"{x_range[1]:{cols-9}.0f}")
    print(" +"+"-"*(cols-1)+">")
    print(f" ^{y_range[1]:.0f}")
    
    screen=np.int_(
        [[ord(' ')]*cols]*rows)

    points=list(zip(x_vals, y_vals))
    points.sort(key=lambda x: x[0])
    # not necessary but could help
    # with debug

    def normalize(left, right, val):
        return (val-left)/         \
               (right-left)

    for point in points:
        x = normalize(*x_range,
                      point[0])*cols
        y = normalize(*y_range,
                      point[1])*rows
        x = x if x>1 else 1
        y = y if y>1 else 1
        screen[int(y+.5)-1]        \
              [int(x+.5)-1]=ord('*')

    for line in screen[::-1]:
        print(" |",end="")
        for c in line:
            print(chr(c), end='')
        print()
    print(" +"+"-"*(cols-1)+">")
    print(f"{y_range[0]:.0f}")
    print(f" {x_range[0]:<10.0f}"
          f"{x_range[1]:{cols-9}.0f}")
    # print(x_vals, y_vals)


def demo():
    x = list(range(100))
    y = list(map(lambda x: x**2, x))
    point_grapher(x,y)
def draw_circle():
    t = np.array(range(1000))
    x = np.sin(t)
    y = np.cos(t)
    point_grapher(x,y)
    
if __name__ == "__main__":
    demo()
    draw_circle()
