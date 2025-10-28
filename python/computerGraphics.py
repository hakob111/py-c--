from graph import *
penColor('blue')
brushColor('yellow')


# penColor('red')
# brushColor('green')
# circle(200, 150, 50)


# print("enter the rectagle coedinats ")
# x = int(input("x = "))
# y = int(input("y = "))
# a = 20
# rectangle(x, y, x+a, y+a)
# run()

""" tasks & exercises """

""" task 1  Determine the coordinates of the pixels that make up the segments:
    a) (10, 20) -- (10, 15)  b) (10, 20) -- (15, 21)
    c) (10, 20) -- (5, 15)   d) (10, 20) -- (15, 22) 
    that is, Bresenham's algorithm
    P_0 = 2\Delta y - \Delta x
    """

# x1, y1, x2, y2 = 10, 20, 10, 15

# difx = x2 - x1
# dify = y2 - y1

# x, y = x1, y1
# pixels = [(x, y)]
# P = 2 * dify-difx

# P_inc_y = 2 * (dify - difx)
# p_inc_x = 2 * dify

# for i in range(abs(difx + dify)):
#     x += 1
#     if P < 0:
#         P += p_inc_x
#     else:
#         y += 1
#         p += P_inc_y
#     pixels.append((x, y))

# print(pixels)